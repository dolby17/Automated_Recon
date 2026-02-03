import requests
from typing import Set

from modules.base import ReconModule
from core.context import ReconContext


class SubdomainEnumerationModule(ReconModule):
    """
    Passive subdomain enumeration using Certificate Transparency logs.
    """

    name = "subdomain_enumeration"

    CRTSH_URL = "https://crt.sh/?q={domain}&output=json"

    def run(self, context: ReconContext) -> None:
        domain = context.target
        discovered: Set[str] = set()

        try:
            response = requests.get(
                self.CRTSH_URL.format(domain=domain),
                timeout=10,
            )
            response.raise_for_status()

            data = response.json()

            for entry in data:
                names = entry.get("name_value", "")
                for name in names.splitlines():
                    name = name.strip().lower().rstrip(".")
                    if name.endswith(domain):
                        discovered.add(name)

        except Exception:
            # Fail safe: no subdomains discovered
            pass

        context.domains.update(discovered)
