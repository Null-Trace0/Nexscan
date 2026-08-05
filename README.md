# NexScan

NexScan is a lightweight network reconnaissance and vulnerability assessment tool built in Python.

It performs service discovery using Nmap, analyzes detected services for common security risks, calculates a risk score, generates remediation recommendations, and exports a professional HTML report.

---

## Features

- TCP Port Scanning
- Service & Version Detection
- Risk Score Calculation
- Vulnerability Analysis
- Security Recommendations
- HTML Report Generation

---

## Requirements

- Python 3
- Nmap

Install Python dependencies:

```bash
pip install -r requirements.txt
```

---

## Usage

```bash
python nexscan.py
```

Enter the target:

```text
scanme.nmap.org
```

The HTML report will be generated inside:

```
exports/report.html
```

---

## Example Output

- Open Ports
- Detected Services
- Risk Level
- Vulnerability Analysis
- Security Recommendations
- HTML Report

---

## Project Structure

```
NexScan/
├── banner.py
├── scanner.py
├── parser.py
├── vuln.py
├── report.py
├── risk.py
├── recommendations.py
├── nexscan.py
├── exports/
├── scans/
└── README.md
```

---

## Disclaimer

This tool is intended for educational purposes and authorized security testing only.
