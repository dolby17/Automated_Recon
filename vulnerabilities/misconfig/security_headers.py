import requests
from vulnerabilities.templates.base_check import BaseVulnCheck

class SecurityHeadersCheck(BaseVulnCheck):
    name = "Missing Security Headers"
    severity = "low"

    REQUIRED_HEADERS = [
        "Content-Security-Policy",
        "X-Frame-Options",
        "X-Content-Type-Options",
        "Referrer-Policy"
    ]

    def run(self):
        findings = []

        try:
            response = requests.get(self.target, timeout=5)
        except requests.RequestException:
            return findings

        for header in self.REQUIRED_HEADERS:
            if header not in response.headers:
                findings.append({
                    "vulnerability": self.name,
                    "missing_header": header,
                    "severity": self.severity
                })

        return findings
