from core.context import ReconContext
from core.reporting.builder import ReportBuilder


def test_report_builder_generates_valid_report():
    context = ReconContext(target="example.com")
    context.domains.update({"www.example.com", "api.example.com"})
    context.ips.update({"93.184.216.34"})
    context.open_ports = {"93.184.216.34": [80, 443]}

    report = ReportBuilder.build(context)

    assert report["target"] == "example.com"
    assert "domains" in report
    assert "ips" in report
    assert "open_ports" in report
    assert report["metadata"]["domain_count"] == 3
    assert report["metadata"]["ip_count"] == 1
