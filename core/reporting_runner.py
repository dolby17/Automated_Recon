from core.report_writer import write_json_report
from core.html_report import generate_html_report


def generate_reports(findings):
    """
    Generate all reports.
    """
    json_path = write_json_report(findings)
    html_path = generate_html_report(findings)

    return {
        "json": json_path,
        "html": html_path
    }
