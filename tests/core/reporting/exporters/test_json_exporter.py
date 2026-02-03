import json
from pathlib import Path

from core.reporting.exporters.json_exporter import JSONExporter


def test_json_exporter_creates_file(tmp_path: Path):
    report = {
        "target": "example.com",
        "domains": ["example.com"],
        "ips": [],
        "open_ports": {},
        "metadata": {},
    }

    output_dir = tmp_path / "reports"
    filename = "example.com.json"

    file_path = JSONExporter.export(
        report=report,
        output_dir=output_dir,
        filename=filename,
    )

    assert file_path.exists()
    assert file_path.name == filename


def test_json_exporter_writes_valid_json(tmp_path: Path):
    report = {"key": "value"}

    file_path = JSONExporter.export(
        report=report,
        output_dir=tmp_path,
        filename="test.json",
    )

    with file_path.open("r", encoding="utf-8") as f:
        data = json.load(f)

    assert data == report
