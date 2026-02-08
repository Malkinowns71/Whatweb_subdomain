
Whatweb_subdomain 🚀
**Automated Attack Surface Mapping & Visual Triage**

[![Python 3.x](https://img.shields.io/badge/python-3.x-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Offensive Security](https://img.shields.io/badge/Focus-Offensive%20Security-red.svg)](#)

## 📖 Overview
`Whatweb_subdomain` is an offensive security utility designed to bridge the gap between **subdomain enumeration** and **manual triage**. In large-scale enterprise engagements, verify hundreds of potential targets is a major bottleneck. 

This tool automates the ingestion of discovered subdomains, utilizes `WhatWeb` for technology fingerprinting, and generates a centralized **HTML Visual Report**. This allows Red Teamers to quickly identify high-value targets based on visual cues and HTTP response metadata.

## ✨ Key Features
* **Visual Triage:** Captures snapshots of live subdomains for rapid manual review.
* **Technology Fingerprinting:** Leverages `WhatWeb` to identify CMS, web servers, and underlying frameworks.
* **HTTP Metadata Parsing:** Extracts and displays response status codes (200, 403, 401, etc.) to prioritize targets.
* **Automated Reporting:** Generates a clean, portable HTML report suitable for team collaboration or internal documentation.

## 🛠️ Technical Workflow
1. **Input:** Ingests a list of subdomains (formatted with `http://` or `https://`).
2. **Analysis:** Runs concurrent `WhatWeb` instances to gather headers and server info.
3. **Capture:** Triggers a snapshot of the rendered page.
4. **Compilation:** Packages data into a responsive HTML dashboard.

## 🚀 Installation & Requirements

### Prerequisites
* **WhatWeb:** Must be installed and available in your system `$PATH`.
* **Python 3.x**

  git clone [https://github.com/Malkinowns71/Whatweb_subdomain.git](https://github.com/Malkinowns71/Whatweb_subdomain.git)
cd Whatweb_subdomain

