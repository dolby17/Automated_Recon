import requests
from validators.base_validator import BaseValidator

class PayloadReflectionValidator(BaseValidator):
    """
    Confirms reflected payloads in HTTP responses.
    """

    def validate(self, finding):
        url = finding.get("url")
        payload = finding.get("payload")

        if not url or not payload:
            return False, finding

        try:
            response = requests.get(url, timeout=5)
        except requests.RequestException:
            return False, finding

        if payload in response.text:
            finding["validated"] = True
            finding["confidence"] = 0.8
            return True, finding

        return False, finding
