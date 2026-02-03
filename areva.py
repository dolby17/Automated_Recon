#!/usr/bin/env python3

import argparse
import sys
from core.runner import run
from pathlib import Path

from core.reporting.builder import ReportBuilder
from core.reporting.summary import SummaryBuilder
from core.reporting.exporters.json_exporter import JSONExporter



def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Automated Recon & Vulnerability Assessment Framework"
    )

    parser.add_argument(
        "-t", "--target",
        required=True,
        help="Target domain (e.g. example.com)"
    )

    parser.add_argument(
        "--recon",
        action="store_true",
        help="Run reconnaissance phase"
    )

    parser.add_argument(
        "--output",
        type=str,
        default=None,
        help="Directory to save recon reports",
    )

    parser.add_argument(
        "--format",
        choices=["json"],
        default="json",
        help="Report output format",
    )

    return parser.parse_args()


def main():
    args = parse_arguments()

    if not args.recon:
        print("[!] No action specified. Use --recon")
        sys.exit(1)

    targets = [args.target]

    # ----------------------------
    # Execute recon
    # ----------------------------
    results = run(targets, vars(args))

    if not results:
        print("[!] No results returned")
        return

    # ----------------------------
    # Reporting & Output
    # ----------------------------
    for target, context in results.items():
        # Phase 2.5.3 — Step 3
        report = ReportBuilder.build(context)

        # Phase 2.5.3 — Step 4
        print("\nRecon Summary")
        print("-" * 40)
        for line in SummaryBuilder.build(report):
            print(line)
        print("-" * 40)

        # Phase 2.5.3 — Step 5
        if args.output:
            output_dir = Path(args.output)
            filename = f"{target}.json"

            JSONExporter.export(
                report=report,
                output_dir=output_dir,
                filename=filename
            )

            print(f"[+] Report saved to: {output_dir / filename}")


if __name__ == "__main__":
    main()
    sys.exit(0)
