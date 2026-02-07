import os
from datetime import datetime
from core.executive_summary import generate_executive_summary


def generate_html_report(findings, output_dir="output", filename="report.html"):
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, filename)

    summary = generate_executive_summary(findings)

    rows = ""
    for f in findings:
        rows += f"""
        <tr>
            <td>{f.get("vulnerability")}</td>
            <td>{f.get("url", "-")}</td>
            <td>{f.get("risk_level")}</td>
            <td>{f.get("risk_score")}</td>
            <td>{f.get("confidence")}</td>
        </tr>
        """

    html = f"""
    <html>
    <head>
        <title>AREVA Vulnerability Report</title>
        <style>
            body {{ font-family: Arial; }}
            table {{ border-collapse: collapse; width: 100%; }}
            th, td {{ border: 1px solid #ccc; padding: 8px; }}
            th {{ background: #333; color: #fff; }}
        </style>
    </head>
    <body>
        <h1>AREVA Vulnerability Report</h1>
        <p>Generated at: {datetime.utcnow().isoformat()}Z</p>

        <h2>Executive Summary</h2>
        <ul>
            <li>Total Findings: {summary["total"]}</li>
            <li>Critical: {summary["critical"]}</li>
            <li>High: {summary["high"]}</li>
            <li>Medium: {summary["medium"]}</li>
            <li>Low: {summary["low"]}</li>
        </ul>

        <h2>Findings</h2>
        <table>
            <tr>
                <th>Vulnerability</th>
                <th>URL</th>
                <th>Risk Level</th>
                <th>Risk Score</th>
                <th>Confidence</th>
            </tr>
            {rows}
        </table>
    </body>
    </html>
    """

    with open(path, "w") as f:
        f.write(html)

    return path
