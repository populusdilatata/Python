from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

chrome_drive_path = r"C:\Development\chromedriver-win64\chromedriver.exe"
service = Service(chrome_drive_path)
url = "https://secure-retreat-92358.herokuapp.com"
try:
    driver = webdriver.Chrome(service=service)
    driver.get(url)

    # Wait for the price element to be present

    wait = WebDriverWait(driver, 10)
    #article_count_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#articlecount a")))
    #article_count_element.click()
    #all_portals = driver.find_element(By.LINK_TEXT, "Wikinews")
    #all_portals.click()

    search_1 = driver.find_element(By.NAME, "fName")
    search_1.send_keys("Tom")
    #search_1.send_keys(Keys.ENTER)

    search_2 = driver.find_element(By.NAME, "lName")
    search_2.send_keys("Tom")
    #search_2.send_keys(Keys.ENTER)

    search_3 = driver.find_element(By.NAME, "email")
    search_3.send_keys("Tom@Tom.cz")
    #search_3.send_keys(Keys.ENTER)

    button = driver.find_element(By.XPATH, '//button[text()="Sign Up"]')
    button.click()
    # Print the text of the element
    # print(article_count_element.text)

finally:
    # Keep the browser open for 10 seconds to observe the result
    time.sleep(10)
    # Close the browser
    driver.quit()