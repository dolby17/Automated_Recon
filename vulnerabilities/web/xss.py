import requests
from vulnerabilities.templates.base_check import BaseVulnCheck
from core.payload_loader import PayloadLoader

class XSSCheck(BaseVulnCheck):
    name = "Reflected XSS"
    severity = "medium"

    def run(self):
        findings = []
        loader = PayloadLoader()
        payloads = loader.load("xss")

        for url in self.context.urls:
            for payload in payloads:
                test_url = f"{url}?q={payload}"

                try:
                    response = requests.get(test_url, timeout=5)
                except requests.RequestException:
                    continue

                if payload in response.text:
                    findings.append({
                        "vulnerability": self.name,
                        "url": test_url,
                        "payload": payload,
                        "severity": self.severity
                    })

        return findings
