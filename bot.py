import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# তথ্যগুলো এখানে দিন
EMAIL = "hay.salman.ahmed@gmail.com"
PASSWORD = "Salman890@#"
LOGIN_URL = "https://wispbyte.com/client/auth/login"
SERVER_URL = "https://wispbyte.com/client/servers/a40bf993/console"

def run_bot():
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    
    # GitHub Actions-এর জন্য ব্রাউজার সেটআপ
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    wait = WebDriverWait(driver, 30)

    try:
        print("Logging in...")
        driver.get(LOGIN_URL)
        wait.until(EC.presence_of_element_located((By.NAME, "username"))).send_keys(EMAIL)
        driver.find_element(By.NAME, "password").send_keys(PASSWORD)
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        
        time.sleep(5)
        print("Navigating to server...")
        driver.get(SERVER_URL)
        
        # Start বাটনে ক্লিক করা
        start_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Start')]")))
        start_btn.click()
        print("Success: Start command sent!")

    except Exception as e:
        print(f"Error: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    run_bot()
          
