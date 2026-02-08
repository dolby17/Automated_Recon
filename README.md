🛡️ AREVA – Automated Recon & Vulnerability Assessment

AREVA is a command-line based automated reconnaissance and vulnerability assessment framework built for authorized security testing and learning purposes.

It automates the early phases of a security assessment by performing:

•Domain reconnaissance

•DNS and IP resolution

•Port scanning

•Basic vulnerability analysis and generates structured reports that can be reviewed or extended further.


✨ Features


🔍 Reconnaissance

•DNS enumeration

•Subdomain discovery

•IP resolution

•Host validation

🚪 Port Scanning

•Identifies open ports on discovered hosts

🧪 Vulnerability Assessment

•Builds vulnerability context from recon data

•Runs basic vulnerability checks

📄 Reporting

•Human-readable console summaries

•Structured JSON reports for further analysis

•Pluggable exporter architecture

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


🛠️ Requirements

•Python 3.8+
•No external Python dependencies


🚀 Installation

git clone https://github.com/<your-username>/automated-recon
cd automated-recon
pip install -r requirements.txt


▶️ How to Use AREVA (Step-by-Step)

1️⃣ Basic Recon (console output only)

python areva.py -t demo.testfire.net --recon


What this does:
•Runs full recon + vulnerability pipeline

•Prints a structured summary to the terminal

•Does not save a file unless output is specified


2️⃣ Recon + Save Report to Disk (recommended)

python areva.py -t demo.testfire.net --recon --output reports


What this does:

•Runs the full pipeline

•Prints summary

•Saves a JSON report to reports/


After running:
ls reports/

You will see:
demo.testfire.net.json


3️⃣ View the Generated Report
cat reports/demo.testfire.net.json

4️⃣ Check Available CLI Options

python areva.py --help

<img width="637" height="236" alt="image" src="https://github.com/user-attachments/assets/d46e6967-6303-4952-96b3-c153a7ab6bea" />




📄 Example Output



Console Summary


<img width="545" height="288" alt="image" src="https://github.com/user-attachments/assets/79b9c20a-5415-4e05-937d-55530c882753" />

JSON Report


<img width="482" height="865" alt="image" src="https://github.com/user-attachments/assets/2282f59b-35da-49f8-9e45-0d9568d84291" />


🧪 Authorized Test Targets

Use AREVA only on systems you own or are explicitly allowed to test.

Safe public test targets:

•demo.testfire.net

•portswigger.net

•tryhackme.com

•owasp.org

❌ Do not scan random companies, banks, government websites, or live production systems.



🔐 Ethical Usage

This project follows ethical hacking principles.
By using AREVA, you agree to:

•Test only authorized targets

•Respect applicable laws and policies

•Use results for learning and defensive purposes


🧩 Future Improvements

•Service fingerprinting

•HTTP security header analysis

•TLS configuration checks

•HTML / CSV report exporters

•Parallel scanning











