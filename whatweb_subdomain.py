import subprocess
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os

def process_urls_from(file_path, html_report):
    screenshot_dir = "screenshots"
    os.makedirs(screenshot_dir, exist_ok=True)
    with open(html_report, 'w') as report:
        report.write("<html><head><title>Subdomain Report </title></head><body>")
        report.write("<h1>Subdomain Scan Report</h1>")
        try:
            with open(file_path, 'r') as file:
                for line in file:
                    url = line.strip()
                    if not url:
                    	continue
                    status, whatweb_output, screenshot_filename = check_url_status(url,screenshot_dir)
                    report.write(f"<h2>{url}</h2>")
                    report.write(f"<p>Status: {status}</p>")
                    report.write(f"<pre>{whatweb_output}</pre>")
                    if screenshot_filename and os.path.exists(screenshot_filename): 
                        rel_path = os.path.relpath(screenshot_filename, os.path.dirname(html_report))
                        report.write(f'<img src="{rel_path}" width="600"><br>')
                    else: 
                        report.write("<p>No screenshot available.</p>")
        except FileNotFoundError:
            report.write(f"<p>Error: File not found: {file_path}</p>")
        except Exception as e:
            report.write(f"<p>An error occurred: {e}</p>")
        report.write("</body></html>")


def check_url_status(url, screenshot_dir):
    status = ""
    whatweb_output = ""
    screenshot_filename = ""
    try: 
        response = requests.get(url, allow_redirects=False, timeout=10)
        status = f"{response.status_code} {response.reason}"
        if response.status_code == 200:
            whatweb_output = run_whatweb(url)
            screenshot_filename = take_screenshot(url, screenshot_dir)
        elif response.status_code == 301 or response.status_code == 302:
            status = f"{response.status_code} Redirect"
            redirect_url = response.headers.get('Location')
            if redirect_url: 
                status += f"(Redirecting to: {redirect_url})"
                return check_url_status(redirect_url, screenshot_dir)
            else: 
                status += "(Redirect URL not found)"
        elif response.status_code == 404: 
            status  = "404 Not Found"
        else: 
            status = f"{response.status_code} {response.reason}"
    except requests.exceptions.RequestException as e:
        status = f"Error accessing {url}: {e}" 
    return status, whatweb_output, screenshot_filename  

def run_whatweb(url): 
    try: 
        result = subprocess.run(['whatweb', url], capture_output=True, text=True, check=True)
        return result.stdout
    except Exception as e: 
        return f"Error running whatweb: {e}"
def take_screenshot(url, screenshot_dir): 
    try: 
        options = Options()
        options.headless = True 
        driver = webdriver.Chrome(options=options)
        driver.set_window_size(1200, 800)
        driver.get(url)
        safe_url = url.replace("://", "_").replace("/", "_")
        screenshot_filename = os.path.join(screenshot_dir, f"screenshot_{safe_url}.png")
        driver.save_screenshot(screenshot_filename)
        driver.quit()
        return screenshot_filename
    except Exception as e: 
        return ""

if __name__ == "__main__":
    file_path = input("Enter the filename containing URLs: ")
    html_report = "report.html"
    process_urls_from(file_path, html_report)
    print(f"Report generated: {html_report}") 


