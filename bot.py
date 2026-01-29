import os
import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# আপনার তথ্য
EMAIL = "hay.salman.ahmed@gmail.com"
PASSWORD = "Salman890@#"
SERVER_URL = "https://wispbyte.com/client/servers/a40bf993/console"

def run_bot():
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    
    # এটি ক্লাউডফ্লেয়ার চ্যালেঞ্জ এড়াতে সাহায্য করে
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
    chrome_options.add_argument('--disable-blink-features=AutomationControlled')

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        print("WispByte ওপেন হচ্ছে...")
        driver.get("https://wispbyte.com/client/auth/login")
        time.sleep(15) # Cloudflare সল্ভ হওয়ার সময়

        # তথ্য দেওয়া হচ্ছে
        driver.find_element(By.NAME, "username").send_keys(EMAIL)
        driver.find_element(By.NAME, "password").send_keys(PASSWORD)
        
        # লগইন বাটনে ক্লিক
        login_btn = driver.find_element(By.XPATH, "//button[@type='submit']")
        driver.execute_script("arguments[0].click();", login_btn)
        print("লগইন চেষ্টা করা হয়েছে...")
        
        time.sleep(20) # ড্যাশবোর্ড লোড হওয়ার জন্য বেশি সময়
        
        # সরাসরি কনসোলে চলে যাওয়া
        driver.get(SERVER_URL)
        time.sleep(15)

        # প্লে আইকন ক্লিক (ভিডিও অনুযায়ী)
        print("প্লে (Start) বাটনে ক্লিক করা হচ্ছে...")
        # ভিডিওতে দেখা সেই স্পেসিফিক বাটনে ক্লিক
        driver.execute_script("document.querySelector('button i.fa-play').parentElement.click();")
        print("✅ SUCCESS: Start command sent!")

    except Exception as e:
        print(f"❌ Error: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    run_bot()
    
