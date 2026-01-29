#!/usr/bin/env python3

import argparse
from core.runner import run


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
        action="store_true",
        help="Run reconnaissance phase"
    )

    return parser.parse_args()


def main():
    args = parse_arguments()

    print("[+] Target:", args.target)

    if args.recon:
        print("[+] Running reconnaissance phase")
        run(args)   


if __name__ == "__main__":
    main()
