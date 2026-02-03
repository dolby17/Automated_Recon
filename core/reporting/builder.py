from typing import Dict, Any
from datetime import datetime, timezone

from core.context import ReconContext


class ReportBuilder:
    """
    Builds structured reports from ReconContext.
    """

    @staticmethod
    def build(context: ReconContext) -> Dict[str, Any]:
        return {
            "target": context.target,
            "domains": sorted(context.domains),
            "ips": sorted(context.ips),
            "dns_records": context.dns_records,
            "open_ports": context.open_ports,
            "metadata": {
                **context.metadata,
                "report_generated": datetime.now(timezone.utc).isoformat(),
                "domain_count": len(context.domains),
                "ip_count": len(context.ips),
                "host_count": len(context.open_ports),
            },
        }
