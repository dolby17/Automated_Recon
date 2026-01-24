#!/usr/bin/env python3
# Makes the script executable like a real Linux tool later

import argparse   # Industry-standard CLI argument parser
import sys        # Required for clean exits and error handling


def parse_arguments():

    parser = argparse.ArgumentParser(
        description="AREVA - Automated Recon & Vulnerability Assessment Tool"
    )

    parser.add_argument(
        "-t", "--target",
        help="Target domain or IP address",
        required=True
    )

    parser.add_argument(
        "--recon",
        help="Run reconnaissance phase",
        action="store_true"
    )

    parser.add_argument(
        "--scan",
        help="Run scanning phase",
        action="store_true"
    )

    parser.add_argument(
        "--vuln",
        help="Run vulnerability assessment phase",
        action="store_true"
    )

    parser.add_argument(
        "--full",
        help="Run full reconnaissance and vulnerability assessment",
        action="store_true"
    )

    return parser.parse_args()


def main():
    args = parse_arguments()

    if not (args.recon or args.scan or args.vuln or args.full):
        print("[!] No action specified. Use --recon, --scan, --vuln, or --full")
        sys.exit(1)

    print("[+] Target:", args.target)

    if args.full:
        print("[+] Running full assessment")
    else:
        if args.recon:
            print("[+] Running reconnaissance phase")
        if args.scan:
            print("[+] Running scanning phase")
        if args.vuln:
            print("[+] Running vulnerability assessment phase")


if __name__ == "__main__":
    main()
