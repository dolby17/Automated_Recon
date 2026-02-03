from dataclasses import dataclass, field
from typing import Dict, List, Set, Any
from datetime import datetime, timezone


@dataclass
class ReconContext:
    """
    Shared state across all recon modules.
    """

    target: str

    # Core assets
    domains: Set[str] = field(default_factory=set)
    ips: Set[str] = field(default_factory=set)

    # Structured recon data
    dns_records: Dict[str, Any] = field(default_factory=dict)
    open_ports: Dict[str, List[int]] = field(default_factory=dict)

    # Metadata
    metadata: Dict[str, Any] = field(default_factory=dict)

    def __post_init__(self) -> None:
        """
        Post-initialization hook for dataclass.
        Ensures base invariants.
        """
        self.domains.add(self.target)
        self.metadata["scan_started"] = datetime.now(timezone.utc).isoformat()
        self.metadata["modules_run"] = []

    def mark_finished(self) -> None:

        finished = datetime.now(timezone.utc)
        self.metadata["scan_finished"] = finished.isoformat()

        started = datetime.fromisoformat(self.metadata["scan_started"])
        self.metadata["duration_seconds"] = round(
            (finished - started).total_seconds(), 2
        )


