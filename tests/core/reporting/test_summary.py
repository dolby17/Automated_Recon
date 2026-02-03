from core.reporting.summary import SummaryBuilder


def test_summary_builder_basic():
    report = {
        "target": "example.com",
        "domains": ["example.com", "www.example.com"],
        "ips": ["93.184.216.34"],
        "open_ports": {
            "93.184.216.34": [80, 443]
        },
    }

    lines = SummaryBuilder.build(report)

    assert "Target        : example.com" in lines
    assert "Domains found : 2" in lines
    assert "IPs resolved  : 1" in lines
    assert "Hosts scanned : 1" in lines
    assert "93.184.216.34 -> 80, 443" in lines


def test_summary_builder_no_open_ports():
    report = {
        "target": "example.com",
        "domains": ["example.com"],
        "ips": [],
        "open_ports": {},
    }

    lines = SummaryBuilder.build(report)

    assert "Open Ports:" not in lines
