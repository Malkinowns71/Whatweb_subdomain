# ReconDash 🚀
**Automated Web Reconnaissance & Visual Triage Framework**

[![Python 3.x](https://img.shields.io/badge/python-3.x-blue.svg)](https://www.python.org/)
[![Selenium](https://img.shields.io/badge/Engine-Selenium-green.svg)](https://www.selenium.dev/)
[![WhatWeb](https://img.shields.io/badge/Recon-WhatWeb-red.svg)](https://github.com/urbanadventurer/WhatWeb)

## 📖 Overview
**ReconDash** is a specialized offensive security utility designed to eliminate the bottleneck between automated subdomain enumeration and manual target verification. 

While traditional tools provide text-heavy outputs, ReconDash performs **Visual Triage**. It leverages a headless Chrome engine to render pages and capture high-fidelity snapshots while simultaneously fingerprinting the technology stack using `WhatWeb`. The result is a single, portable HTML dashboard that allows Red Teamers to identify high-value targets (login portals, misconfigured dashboards, etc.) in seconds.

## ✨ Key Features
* **Headless Browser Rendering:** Uses Selenium to render modern JavaScript-heavy sites that basic `requests`-based tools often miss.
* **Technology Fingerprinting:** Deep-dive analysis via `WhatWeb` integration for server, CMS, and framework identification.
* **Consolidated Intelligence:** Maps HTTP response status codes, technology headers, and visual snapshots into one UI.
* **Engineered for Performance:** Implements a persistent browser session to minimize CPU/Memory overhead during large-scale scans.
* **Portable Output:** Generated reports use relative pathing, making them ideal for zipping and sharing as part of a penetration testing deliverable.

## 🛠️ System Architecture
ReconDash is built with a focus on modularity and error resiliency:
1. **Orchestrator:** Manages the input stream and directory structure.
2. **Recon Engine:** Executes `WhatWeb` subprocesses for header analysis.
3. **Capture Engine:** Utilizes a persistent Selenium WebDriver to navigate and snapshot targets.
4. **Reporter:** Compiles raw JSON/Text data into a sanitized, responsive HTML report.

## 🚀 Installation

### 1. Prerequisites
* **Python 3.x**
* **WhatWeb:** `sudo apt install whatweb`
* **Chrome & ChromeDriver:** Ensure Google Chrome and the matching `chromedriver` are installed in your PATH.

### 2. Dependencies
```bash
pip install selenium requests
3. Setup
Bash
git clone [https://github.com/Malkinowns71/ReconDash.git](https://github.com/Malkinowns71/ReconDash.git)
cd ReconDash
📋 Usage
Prepare a targets.txt file with one URL per line (including http:// or https://).

Run the framework:

Bash
python3 recondash.py
Follow the prompt to enter your target filename.

Open recon_report.html to view your findings.

🛡️ Legal Disclaimer
This tool is intended for authorized security testing and educational purposes only. The author assumes no liability for misuse of this tool. Always ensure you have explicit written permission before scanning any infrastructure.
