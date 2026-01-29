import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# আপনার তথ্য
EMAIL = "hay.salman.ahmed@gmail.com"
PASSWORD = "Salman890@#"
LOGIN_URL = "https://wispbyte.com/client/auth/login"
SERVER_URL = "https://wispbyte.com/client/servers/a40bf993/console"

def run_bot():
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--window-size=1920,1080') # ফুল স্ক্রিন মোড

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    wait = WebDriverWait(driver, 30)

    try:
        # লগইন প্রক্রিয়া
        print("Logging in to WispByte...")
        driver.get(LOGIN_URL)
        wait.until(EC.presence_of_element_located((By.NAME, "username"))).send_keys(EMAIL)
        driver.find_element(By.NAME, "password").send_keys(PASSWORD)
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        
        time.sleep(7) # ড্যাশবোর্ড লোড হওয়ার জন্য সময় দিন
        
        # সার্ভার পেজে যাওয়া
        print(f"Navigating to: {SERVER_URL}")
        driver.get(SERVER_URL)
        time.sleep(5)

        # স্টার্ট বাটন খোঁজা (আইকন বা ক্লাস দিয়ে)
        print("Searching for the Start Button icon...")
        
        # এখানে কয়েক ধরণের XPath ট্রাই করবে
        xpath_list = [
            "//button[contains(@class, 'btn-success')]", # সবুজ বাটন
            "//button[contains(@class, 'play')]",        # প্লে আইকন
            "//i[contains(@class, 'play')]/..",          # আইকন এর প্যারেন্ট বাটন
            "//button[contains(@title, 'Start')]",       # যদি মাউস রাখলে স্টার্ট দেখায়
            "//button[text()='Start']"                   # সাধারণ টেক্সট
        ]
        
        start_btn = None
        for xpath in xpath_list:
            try:
                start_btn = driver.find_element(By.XPATH, xpath)
                if start_btn.is_displayed():
                    print(f"Button found using: {xpath}")
                    break
            except:
                continue
        
        if start_btn:
            driver.execute_script("arguments[0].click();", start_btn) # সরাসরি জাভাস্ক্রিপ্ট ক্লিক
            print("Successfully clicked the Start Button!")
        else:
            print("Error: Could not find the Start button. Check your console layout.")
            driver.save_screenshot("error_layout.png") # বাটন না পেলে ছবি তুলবে

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        driver.quit()
        print("Session closed.")

if __name__ == "__main__":
    run_bot()
    
