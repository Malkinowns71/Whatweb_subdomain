Automated Web Reconnaissance & Visual Triage Framework

📖 Overview
Whatweb_subdomain is a Python-based automation framework designed to streamline the reconnaissance phase of penetration tests. Unlike standard enumeration tools that provide raw text output, this utility performs Visual Triage—capturing high-fidelity screenshots using a headless Chrome instance while concurrently fingerprinting technologies and HTTP response metadata.

This tool is purpose-built for Red Teamers who need to quickly sift through hundreds of subdomains to identify high-value targets (e.g., login portals, unauthenticated dashboards, or deprecated internal systems).

✨ Key Features
Headless Browser Integration: Uses Selenium and Chrome to render pages exactly as a user would, capturing JavaScript-heavy content that basic requests miss.

Unified Recon Report: Generates a standalone HTML dashboard containing:

HTTP Status Codes & Reasons (e.g., 200 OK, 403 Forbidden).

Technology Fingerprinting: Deep-dive analysis via WhatWeb integration.

Visual Snapshots: 1200x800 high-resolution screenshots.

Session Optimization: Initializes a single browser instance for the entire scan to minimize memory overhead and CPU usage.

Portable Reporting: Uses relative pathing for image assets, making the output folder easy to compress and share with stakeholders.

🛠️ Technical Workflow
Ingestion: Reads a list of target URLs from a flat file.

Validation: Performs a synchronous requests check to verify connectivity and capture status codes.

Fingerprinting: Triggers WhatWeb as a subprocess to extract server headers and CMS details.

Capture: Directs the Selenium headless driver to the target for a visual snapshot.

Reporting: Appends data into a formatted HTML document with a clean UI.

🚀 Installation
1. Prerequisites
Python 3.x

WhatWeb: sudo apt install whatweb

Chrome & ChromeDriver: Ensure Google Chrome and the matching chromedriver are installed.

2. Python Dependencies
Bash
pip install selenium requests
3. Setup
Bash
git clone https://github.com/Malkinowns71/Whatweb_subdomain.git
cd Whatweb_subdomain
📋 Usage
Create a file (e.g., targets.txt) with one URL per line (ensure http:// or https:// is included).

Execute the script:

Bash
python3 whatweb_subdomain.py
When prompted, enter the filename: targets.txt.

Open recon_report.html in any browser to review results.

🛡️ Legal Disclaimer
This tool is intended for authorized security testing and educational purposes only. The author assumes no liability for misuse of this tool. Always ensure you have explicit written permission before scanning any infrastructure.
