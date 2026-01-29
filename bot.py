import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# তথ্য
EMAIL = "hay.salman.ahmed@gmail.com"
PASSWORD = "Salman890@#"
LOGIN_URL = "https://wispbyte.com/client/auth/login"
SERVER_URL = "https://wispbyte.com/client/servers/a40bf993/console"

def run_bot():
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--window-size=1920,1080')

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    wait = WebDriverWait(driver, 30)

    try:
        print("Logging in...")
        driver.get(LOGIN_URL)
        wait.until(EC.presence_of_element_located((By.NAME, "username"))).send_keys(EMAIL)
        driver.find_element(By.NAME, "password").send_keys(PASSWORD)
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        
        time.sleep(10) # ড্যাশবোর্ড লোড হতে সময় দিন
        
        print("Navigating to console...")
        driver.get(SERVER_URL)
        time.sleep(10)

        # আপনার স্ক্রিনশট অনুযায়ী প্লে আইকন বাটনটি খোঁজা
        print("Finding the Play/Start icon...")
        
        # আপনার কনসোলের প্লে বাটনের নিখুঁত পথ (XPath)
        # এটি সেই বাটনটিকে খুঁজবে যেটির ভেতরে প্লে আইকন আছে
        start_button_xpath = "//button[.//i[contains(@class, 'fa-play') or contains(@class, 'play')]] | //button[contains(@class, 'btn-success')]"
        
        start_btn = wait.until(EC.element_to_be_clickable((By.XPATH, start_button_xpath)))
        
        # বাটনে ক্লিক করা
        driver.execute_script("arguments[0].click();", start_btn)
        print("✅ SUCCESS: Play/Start button clicked!")

    except Exception as e:
        print(f"❌ Error: {e}")
        driver.save_screenshot("error_check.png")
    finally:
        driver.quit()

if __name__ == "__main__":
    run_bot()
    
