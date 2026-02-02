#!/usr/bin/env python3

import argparse
from core.runner import run


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

    return parser.parse_args()


def main():
    args = parse_arguments()

    # ----------------------------
    # 1. Prepare targets
    # ----------------------------
    targets = [args.target]

    # ----------------------------
    # 2. Execute runner
    # ----------------------------
    if args.recon:
        results = run(targets, vars(args))
    else:
        print("[!] No action specified")
        return

    # ----------------------------
    # 3. Print results
    # ----------------------------
    if not results:
        print("[!] No results returned")
        return

    for target, outputs in results.items():
        print(f"\n[+] Recon results for {target}")
        for output in outputs:
            print(output)


if __name__ == "__main__":
    main()
