from dataclasses import dataclass, field
from typing import Dict, List, Set, Any
from datetime import datetime, timezone


@dataclass
class ReconContext:

    target: str

    
    domains: Set[str] = field(default_factory=set)
    ips: Set[str] = field(default_factory=set)

    
    dns_records: Dict[str, Any] = field(default_factory=dict)
    open_ports: Dict[str, List[int]] = field(default_factory=dict)

    ports: List[int] = field(default_factory=list)
    urls: List[str] = field(default_factory=list)

    metadata: Dict[str, Any] = field(default_factory=dict)

    def __post_init__(self) -> None:
        self.domains.add(self.target)
        self.metadata["scan_started"] = datetime.now(timezone.utc).isoformat()
        self.metadata["modules_run"] = []

    def finalize(self) -> None:
        port_set = set()

        for _, ports in self.open_ports.items():
            port_set.update(ports)

        self.ports = sorted(port_set)

        if 80 in self.ports and f"http://{self.target}" not in self.urls:
            self.urls.append(f"http://{self.target}")


        if 443 in self.ports and f"https://{self.target}" not in self.urls:
            self.urls.append(f"https://{self.target}")


    

        finished = datetime.now(timezone.utc)
        self.metadata["scan_finished"] = finished.isoformat()

        started = datetime.fromisoformat(self.metadata["scan_started"])
        self.metadata["duration_seconds"] = round(
            (finished - started).total_seconds(), 2
        )

    def mark_finished(self) -> None:
        self.finalize()


