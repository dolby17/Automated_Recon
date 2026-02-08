🛡️ AREVA – Automated Recon & Vulnerability Assessment

AREVA is a command-line based automated reconnaissance and vulnerability assessment framework built for authorized security testing and learning purposes.

It automates the early phases of a security assessment by performing:

Domain reconnaissance

DNS and IP resolution

Port scanning

Basic vulnerability analysis
and generates structured reports that can be reviewed or extended further.


✨ Features
🔍 Reconnaissance

DNS enumeration

Subdomain discovery

IP resolution

Host validation

🚪 Port Scanning

Identifies open ports on discovered hosts

🧪 Vulnerability Assessment

Builds vulnerability context from recon data

Runs basic vulnerability checks

📄 Reporting

Human-readable console summaries

Structured JSON reports for further analysis

Pluggable exporter architecture

🧠 Project Architecture

areva.py                     # CLI entry point
│
├── core/
│   ├── runner.py            # Recon pipeline execution
│   ├── vuln_runner.py       # Vulnerability scan engine
│   ├── vuln_context.py      # Context passed to vuln checks
│   └── reporting/
│       ├── builder.py       # Builds final report object
│       ├── summary.py       # Console summary generator
│       └── exporters/
│           └── json_exporter.py
│
├── modules/
│   ├── dns_enum.py
│   ├── subdomain_enum.py
│   ├── ip_resolution.py
│   └── port_scan.py
│
└── reports/                 # Generated reports (optional)

