import requests
from validators.base_validator import BaseValidator

class HTTPStatusValidator(BaseValidator):
    """
    Ensures vulnerability exists on valid HTTP responses.
    """

    def validate(self, finding):
        url = finding.get("url")
        if not url:
            return False, finding

        try:
            response = requests.get(url, timeout=5)
        except requests.RequestException:
            return False, finding

        if response.status_code < 400:
            finding["http_status"] = response.status_code
            return True, finding

        return False, finding
