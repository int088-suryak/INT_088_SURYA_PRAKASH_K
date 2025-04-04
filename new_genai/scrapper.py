from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options 

chrome_options = Options()
chrome_options.add_argument("--disable-gpu")  # Disable GPU rendering
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--allow-running-insecure-content")

# chrome_options.add_argument("--headless")  # Run without opening browser (optional)

driver = webdriver.Chrome(options=chrome_options)
# List of websites to scrape
websites = [
    "https://www.gucci.com",
    "https://www.pradagroup.com",
    "https://www.burberry.com"
]

# Setup WebDriver (use Chrome, Edge, or Firefox)
driver = webdriver.Chrome()

def extract_links():
    """Extract navbar and footer links from the current page."""
    navbar_links = driver.find_elements(By.CSS_SELECTOR, "nav a")
    footer_links = driver.find_elements(By.CSS_SELECTOR, "footer a")

    navbar_urls = [link.get_attribute("href") for link in navbar_links if link.get_attribute("href")]
    footer_urls = [link.get_attribute("href") for link in footer_links if link.get_attribute("href")]

    return set(navbar_urls + footer_urls)

def extract_page_data(url):
    """Extract all visible text from a webpage."""
    driver.get(url)
    time.sleep(2)  # Wait for the page to load
    try:
        return driver.find_element(By.TAG_NAME, "body").text  # Extract visible text
    except:
        return "Could not extract data."

# Iterate through all websites
for website in websites:
    driver.get(website)
    time.sleep(3)  # Wait for page load

    all_urls = extract_links()

    # Output file for each website
    domain_name = website.split("//")[-1].replace(".", "_")  # Format filename
    output_file = f"{domain_name}_scraped_data.txt"

    # Scrape each linked page
    with open(output_file, "w", encoding="utf-8") as file:
        for url in all_urls:
            page_content = extract_page_data(url)
            file.write(f"Page: {url}\nContent:\n{page_content}\n" + "="*80 + "\n")

    print(f"Scraped data saved to {output_file}")

# Close the browser
driver.quit()
