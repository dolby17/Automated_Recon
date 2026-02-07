import uuid
import dns.resolver
from concurrent.futures import ThreadPoolExecutor

from core.phases.phase3.base import Phase3Module

def detect_wildcard(domain):
    random_sub = f"{uuid.uuid4().hex}.{domain}"
    try:
        answers = dns.resolver.resolve(random_sub, "A")
        return {a.to_text() for a in answers}
    except:
        return set()

def load_wordlist(path):
    with open(path, "r") as f:
        return [line.strip() for line in f if line.strip()]

def generate_candidates(domain, words):
    return [f"{w}.{domain}" for w in words]


def resolve_domain(domain, wildcard_ips):
    try:
        answers = dns.resolver.resolve(domain, "A")
        ips = {a.to_text() for a in answers}

        if not ips:
            return None

        if wildcard_ips and ips.issubset(wildcard_ips):
            return None

        return ips
    except:
        return None



class ActiveSubdomainDiscovery(Phase3Module):

    def __init__(self, target, config):
        super().__init__(target, config)
        self.discovered = {}
        self.wildcard_ips = set()

    def run(self):
        self.wildcard_ips = detect_wildcard(self.target)

        wordlist_path = self.config.get("subdomain_wordlist")
        words = load_wordlist(wordlist_path)
        candidates = generate_candidates(self.target, words)

        with ThreadPoolExecutor(max_workers=20) as executor:
            results = executor.map(
                lambda sub: (sub, resolve_domain(sub, self.wildcard_ips)),
                candidates
            )

        for sub, ips in results:
            if ips:
                self.discovered[sub] = list(ips)


        


    def results(self):
        return {
            "phase": 3,
            "step": "3.1",
            "module": "active_subdomain_discovery",
            "count": len(self.discovered),
            "subdomains": self.discovered
        }
