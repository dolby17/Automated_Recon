from validators.payload_reflection import PayloadReflectionValidator
from validators.http_validator import HTTPStatusValidator

def validate_findings(findings):
    """
    Runs validators on detected findings.
    """

    validators = [
        HTTPStatusValidator(),
        PayloadReflectionValidator(),
    ]

    validated = []

    for finding in findings:
        is_valid = True
        enriched = finding

        for validator in validators:
            ok, enriched = validator.validate(enriched)
            if not ok:
                is_valid = False
                break

        if is_valid:
            validated.append(enriched)

    return validated
