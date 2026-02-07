from vulnerabilities.web.xss import XSSCheck
from vulnerabilities.misconfig.security_headers import SecurityHeadersCheck

from core.validation_runner import validate_findings
from core.scoring_runner import score_findings


def run_vuln_scan(target, context):
    """
    Executes all vulnerability checks,
    validates findings, scores them,
    and removes duplicates.
    """

    # 🔹 Register vulnerability checks here
    checks = [
        XSSCheck(target, context),
        SecurityHeadersCheck(target, context),
    ]

    results = []

    # 🔹 Phase 1: Detection
    for check in checks:
        try:
            findings = check.run()
            if findings:
                results.extend(findings)
        except Exception as e:
            print(f"[!] {check.name} failed: {e}")

    # 🔹 Phase 2: Validation
    validated = validate_findings(results)

    # 🔹 Phase 3: Severity, confidence, risk, deduplication
    final_results = score_findings(validated)

    return final_results
