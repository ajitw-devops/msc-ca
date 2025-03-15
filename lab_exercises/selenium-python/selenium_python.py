from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# Set up the Chrome WebDriver
driver = webdriver.Chrome()

try:
    # Open Google
    driver.get("https://www.google.com")

    # Allow the page to load
    #time.sleep(2)
    #time.sleep(2)
    driver.implicitly_wait(10)
    
    try:
    # wait 10 seconds before looking for element
        element = WebDriverWait(driver, 10).until(
    )
    finally:
    # else quit
        driver.quit()
    
    # Locate the Google search bar
    search_box = driver.find_element(By.NAME, "l")

    # Type "How are you" into the search box
    search_box.send_keys("How are you")

    # Press Enter to search
    search_box.send_keys(Keys.RETURN)

    # Wait for results to load
    time.sleep(3)

finally:
    # Close the browser after some time
    time.sleep(5)
    driver.quit()