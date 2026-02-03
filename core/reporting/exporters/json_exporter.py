import json
from pathlib import Path
from typing import Dict, Any


class JSONExporter:
    """
    Exports recon reports to JSON files.
    """

    @staticmethod
    def export(
        report: Dict[str, Any],
        output_dir: Path,
        filename: str,
    ) -> Path:
        """
        Write report to a JSON file.

        Returns the path to the created file.
        """
        output_dir.mkdir(parents=True, exist_ok=True)

        file_path = output_dir / filename

        with file_path.open("w", encoding="utf-8") as f:
            json.dump(report, f, indent=2, sort_keys=True)

        return file_path
