def calculate_risk(finding):
    """
    Compute final risk rating.
    """

    severity = finding.get("severity_score", 1.0)
    confidence = finding.get("confidence", 0.5)

    risk_score = round(severity * confidence, 2)

    if risk_score >= 8:
        level = "Critical"
    elif risk_score >= 6:
        level = "High"
    elif risk_score >= 3:
        level = "Medium"
    else:
        level = "Low"

    finding["risk_score"] = risk_score
    finding["risk_level"] = level

    return finding
