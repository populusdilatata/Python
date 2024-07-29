from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

chrome_drive_path = r"C:\Development\chromedriver-win64\chromedriver.exe"
service = Service(chrome_drive_path)

try:
    driver = webdriver.Chrome(service=service)
    driver.get("https://www.python.org")

    # Attempt to find the price element by its class name
    try:
        element = driver.find_element(By.CSS_SELECTOR, ".documentation-widget a")
        element_text = element.text
        print(f"Element found: {element_text}")
    except Exception as e:
        print(f"Element not found. Error: {e}")

    # Keep the browser open for 10 seconds to observe the result
    time.sleep(10)

finally:
    # Close the browser
    driver.quit()
