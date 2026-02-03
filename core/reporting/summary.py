from typing import Dict, Any, List


class SummaryBuilder:
    """
    Builds human-readable summaries from reports.
    """

    @staticmethod
    def build(report: Dict[str, Any]) -> List[str]:
        lines: List[str] = []

        metadata = report.get("metadata", {})

        lines.append(f"Target        : {report.get('target')}")

        duration = metadata.get("duration_seconds")
        if duration is not None:
            lines.append(f"Scan duration : {duration} seconds")

        domains = report.get("domains", [])
        ips = report.get("ips", [])
        open_ports = report.get("open_ports", {})

        lines.append(f"Domains found : {len(domains)}")
        lines.append(f"IPs resolved  : {len(ips)}")
        lines.append(f"Hosts scanned : {len(open_ports)}")

        if open_ports:
            lines.append("")
            lines.append("Open Ports:")
            for ip, ports in open_ports.items():
                ports_str = ", ".join(str(p) for p in sorted(ports))
                lines.append(f"{ip} -> {ports_str}")

        return lines
