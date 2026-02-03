import socket
from typing import List

from modules.base import ReconModule
from core.context import ReconContext


class PortScanModule(ReconModule):
    """
    Safe TCP connect port scanner.
    """

    name = "port_scan"

    # Conservative default ports
    DEFAULT_PORTS: List[int] = [
        21, 22, 23, 25,
        53, 80, 110, 143,
        443, 445, 3306,
        3389, 8080,
    ]

    TIMEOUT = 1.0  # seconds

    def run(self, context: ReconContext) -> None:
        results = {}

        for ip in context.ips:
            open_ports = []

            for port in self.DEFAULT_PORTS:
                try:
                    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                        sock.settimeout(self.TIMEOUT)
                        result = sock.connect_ex((ip, port))

                        if result == 0:
                            open_ports.append(port)

                except Exception:
                    # Fail safe: ignore port
                    continue

            if open_ports:
                results[ip] = open_ports

        context.open_ports.update(results)
