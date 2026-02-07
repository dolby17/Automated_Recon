from core.severity_scoring import calculate_severity
from core.confidence_scoring import calculate_confidence
from core.risk_rating import calculate_risk
from core.deduplicator import deduplicate

def score_findings(findings):
    """
    Apply severity, confidence, risk, and deduplication.
    """

    scored = []

    for finding in findings:
        finding = calculate_severity(finding)
        finding = calculate_confidence(finding)
        finding = calculate_risk(finding)
        scored.append(finding)

    return deduplicate(scored)
