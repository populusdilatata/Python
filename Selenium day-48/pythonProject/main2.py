from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

chrome_drive_path = r"C:\Development\chromedriver-win64\chromedriver.exe"
service = Service(chrome_drive_path)

try:
    driver = webdriver.Chrome(service=service)
    driver.get("https://www.amazon.com/Instant-Pot-Electric-Multi-Cooker-Pressure/dp/B0B4PQDFCL/ref=sr_1_1_sspa?dib=eyJ2IjoiMSJ9.y4LLAMvRXyF-GJBFF44Yph6GT7wWDQNlade-fcUVha5S3eT4ffdoT3gwxUwLiULYDIpU0GG2iuCnBJ9mWPNh5vHt3QdH_7iQHSQmGmoKE-8wEr9Sgjx8P3wA0kt6fl03aqPtZSTnCJ9siq2NgIB8mHnqRZHeFuuPUilntAVgc0qsp_zXGlKMx8r6n3aRsX4PUCFjzAygAiaZKXulzBQ0JRa7OxgAaeQ_ocn5-M3lse0.-GApLDmaLvk184ue5G4aNMuHv43bjgt3tbJkBfKKK6w&dib_tag=se&keywords=instant-pot&qid=1721894628&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1")

    # Wait for the price element to be present
    wait = WebDriverWait(driver, 10)
    #price_element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "a-offscreen")))

    # Get all elements with the class name
    price_element = driver.find_element(By.CLASS_NAME, "a-price")
    print(price_element.text)


finally:
    # Close the browser
    driver.quit()
