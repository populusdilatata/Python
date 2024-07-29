from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

chrome_drive_path = r"C:\Development\chromedriver-win64\chromedriver.exe"
service = Service(chrome_drive_path)
url = "https://www.python.org"
try:
    driver = webdriver.Chrome(service=service)
    driver.get(url)

    # Wait for the price element to be present

    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".event-widget time")))
    #price_element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "a-offscreen")))

    # Get all elements with the class name
    event_times = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
    event_names = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")

    for event_time, event_name in zip(event_times, event_names):
        print(f"{event_time.text}: {event_name.text}")




finally:
    # Keep the browser open for 10 seconds to observe the result
    time.sleep(10)
    # Close the browser
    driver.quit()