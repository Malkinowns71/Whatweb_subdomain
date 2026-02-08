import subprocess
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import sys

def setup_browser():
    """Initializes the headless Chrome driver once for the entire session."""
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")  # Vital for running in Linux environments
    chrome_options.add_argument("--disable-dev-shm-usage")
    # Some sites block bot-like headers; setting a User-Agent helps
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36")
    
    try:
        driver = webdriver.Chrome(options=chrome_options)
        driver.set_page_load_timeout(15)
        return driver
    except Exception as e:
        print(f"Error starting Chrome: {e}")
        return None

def run_whatweb(url):
    """Executes the external WhatWeb tool for additional reconnaissance data."""
    try:
        result = subprocess.run(['whatweb', url], capture_output=True, text=True, check=True, timeout=10)
        return result.stdout
    except Exception:
        return "WhatWeb scan failed or tool not found."

def take_screenshot(url, driver, screenshot_dir):
    """Uses the existing driver to capture a site screenshot and returns the relative path."""
    try:
        # Create a safe filename from the URL
        safe_url = url.replace("://", "_").replace("/", "_").replace(".", "_")
        filename = f"{safe_url}.png"
        full_path = os.path.join(screenshot_dir, filename)
        
        driver.get(url)
        driver.set_window_size(1200, 800)
        driver.save_screenshot(full_path)
        
        # Use relative path for HTML compatibility
        return f"screenshots/{filename}"
    except Exception:
        return None

def process_urls(file_path, html_report_name):
    # Setup directories relative to current working directory
    base_dir = os.getcwd()
    screenshot_dir = os.path.join(base_dir, "screenshots")
    os.makedirs(screenshot_dir, exist_ok=True)
    
    html_report_path = os.path.join(base_dir, html_report_name)
    driver = setup_browser()
    
    if not driver:
        print("Aborting: Could not initialize browser.")
        return

    print(f"Processing URLs from {file_path}...")
    
    try:
        with open(html_report_path, 'w') as report:
            report.write("<html><head><title>Recon Report</title><style>body{font-family:sans-serif;margin:40px;} img{border:1px solid #ccc; margin-top:10px;} pre{background:#f4f4f4;padding:10px;}</style></head><body>")
            report.write("<h1>Subdomain Scan Report</h1>")

            with open(file_path, 'r') as file:
                for line in file:
                    url = line.strip()
                    if not url: continue
                    
                    print(f"Scanning: {url}")
                    try:
                        response = requests.get(url, timeout=10, allow_redirects=True)
                        status = f"{response.status_code} {response.reason}"
                        
                        whatweb_info = run_whatweb(url)
                        relative_img_path = take_screenshot(url, driver, screenshot_dir)

                        report.write(f"<h3>{url}</h3>")
                        report.write(f"<p><strong>Status:</strong> {status}</p>")
                        report.write(f"<pre>{whatweb_info}</pre>")
                        
                        if relative_img_path:
                            # Using relative path so the folder can be moved/zipped
                            report.write(f'<img src="{relative_img_path}" width="600"><br>')
                        else:
                            report.write("<p><em>Screenshot failed.</em></p>")
                        report.write("<hr>")
                        
                    except Exception as e:
                        report.write(f"<h3>{url}</h3><p>Error: {e}</p><hr>")

            report.write("</body></html>")
        print(f"Success! Report generated at: {html_report_path}")
        
    finally:
        driver.quit()

if __name__ == "__main__":
    target_file = input("Enter filename with URLs: ")
    if os.path.exists(target_file):
        process_urls(target_file, "recon_report.html")
    else:
        print("File not found.")
