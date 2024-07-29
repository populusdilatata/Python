from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

chrome_drive_path = r"C:\Development\chromedriver-win64\chromedriver.exe"
service = Service(chrome_drive_path)
url = "https://en.wikipedia.org/wiki/Main_Page"
try:
    driver = webdriver.Chrome(service=service)
    driver.get(url)

    # Wait for the price element to be present

    wait = WebDriverWait(driver, 10)
    article_count_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#articlecount a")))

    # Print the text of the element
    print(article_count_element.text)

finally:
    # Keep the browser open for 10 seconds to observe the result
    time.sleep(10)
    # Close the browser
    driver.quit()