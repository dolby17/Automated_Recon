from core.phases.phase3.discovery.active_subdomains import ActiveSubdomainDiscovery

module = ActiveSubdomainDiscovery(
    target="example.com",
    config={
        "subdomain_wordlist": "core/data/subdomains.txt"
    }
)

module.run()
print(module.results())
