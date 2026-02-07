def calculate_confidence(finding):
    """
    Normalize confidence score between 0 and 1.
    """

    confidence = finding.get("confidence")

    if confidence is None:
        confidence = 0.5  # default for unvalidated but plausible findings

    confidence = max(0.0, min(confidence, 1.0))
    finding["confidence"] = confidence

    return finding
