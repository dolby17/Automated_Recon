import json
import os
from datetime import datetime


def write_json_report(findings, output_dir="output", filename="vulnerabilities.json"):
    """
    Write findings to a JSON report.
    """
    os.makedirs(output_dir, exist_ok=True)

    path = os.path.join(output_dir, filename)

    report = {
        "generated_at": datetime.utcnow().isoformat() + "Z",
        "total_findings": len(findings),
        "findings": findings,
    }

    with open(path, "w") as f:
        json.dump(report, f, indent=4)

    return path
