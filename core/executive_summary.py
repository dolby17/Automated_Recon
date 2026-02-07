from collections import Counter


def generate_executive_summary(findings):
    """
    Create a high-level summary for management.
    """

    severity_counts = Counter(
        f.get("risk_level", "Unknown") for f in findings
    )

    summary = {
        "total": len(findings),
        "critical": severity_counts.get("Critical", 0),
        "high": severity_counts.get("High", 0),
        "medium": severity_counts.get("Medium", 0),
        "low": severity_counts.get("Low", 0),
    }

    return summary
