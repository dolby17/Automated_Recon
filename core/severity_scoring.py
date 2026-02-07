SEVERITY_MAP = {
    "info": 1.0,
    "low": 3.0,
    "medium": 6.0,
    "high": 8.5,
    "critical": 9.5
}

def calculate_severity(finding):
    """
    Convert severity label to numeric score.
    """
    label = finding.get("severity", "info").lower()
    score = SEVERITY_MAP.get(label, 1.0)

    finding["severity_score"] = score
    return finding
