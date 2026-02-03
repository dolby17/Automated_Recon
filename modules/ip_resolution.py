import socket
import ipaddress
from typing import Set

from modules.base import ReconModule
from core.context import ReconContext


class IPResolutionModule(ReconModule):
    """
    Resolves domains to public IP addresses.
    """

    name = "ip_resolution"

    def run(self, context: ReconContext) -> None:
        resolved_ips: Set[str] = set()

        for domain in context.domains:
            try:
                addr_info = socket.getaddrinfo(domain, None)

                for entry in addr_info:
                    ip = entry[4][0]
                    ip_obj = ipaddress.ip_address(ip)

                    # Only keep public IPs (external recon)
                    if ip_obj.is_global:
                        resolved_ips.add(str(ip_obj))

            except Exception:
                # Fail safe: ignore resolution errors
                continue

        context.ips.update(resolved_ips)
