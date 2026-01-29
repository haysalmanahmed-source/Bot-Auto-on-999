import os
import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# আপনার সঠিক তথ্য
EMAIL = "hay.salman.ahmed@gmail.com"
PASSWORD = "Salman890@#"
LOGIN_URL = "https://wispbyte.com/client/auth/login"
SERVER_URL = "https://wispbyte.com/client/servers/a40bf993/console"

def run_bot():
    chrome_options = Options()
    chrome_options.add_argument('--headless') # গিটহাবের জন্য এটি জরুরি
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--window-size=1920,1080')
    
    # Cloudflare শনাক্তকরণ এড়াতে এই বিশেষ User-Agent টি জরুরি
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    # বট লুকানোর অ্যাডভান্সড স্ক্রিপ্ট
    driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        "source": "const newProto = navigator.__proto__; delete newProto.webdriver; navigator.__proto__ = newProto;"
    })

    wait = WebDriverWait(driver, 60)

    try:
        print("লগইন পেজে যাওয়া হচ্ছে...")
        driver.get(LOGIN_URL)
        time.sleep(10) # Cloudflare লোড হওয়ার জন্য সময়

        # ইউজারনেম ও পাসওয়ার্ড ইনপুট
        print("তথ্য দেওয়া হচ্ছে...")
        wait.until(EC.presence_of_element_located((By.NAME, "username"))).send_keys(EMAIL)
        driver.find_element(By.NAME, "password").send_keys(PASSWORD)
        
        # লগইন বাটনে ক্লিক (ভিডিও অনুযায়ী সরাসরি ক্লিক)
        login_btn = driver.find_element(By.XPATH, "//button[@type='submit']")
        driver.execute_script("arguments[0].click();", login_btn)
        
        print("ড্যাশবোর্ড লোড হওয়ার জন্য অপেক্ষা...")
        time.sleep(20) 
        
        # সরাসরি কনসোলে চলে যাওয়া
        print(f"সার্ভার কনসোলে যাওয়া হচ্ছে: {SERVER_URL}")
        driver.get(SERVER_URL)
        time.sleep(15) 

        # আপনার ভিডিওতে দেখা 'Play' বাটনটি ক্লিক করা
        print("প্লে (Start) বাটনে ক্লিক করার চেষ্টা করা হচ্ছে...")
        
        # ভিডিও অনুযায়ী প্লে আইকনওয়ালা বাটন খুঁজে ক্লিক করার জন্য নিখুঁত জাভাস্ক্রিপ্ট
        try:
            # এটি আপনার কনসোলের প্রথম প্লে আইকনওয়ালা বাটনটি খুঁজে ক্লিক করবে
            driver.execute_script("document.querySelector('button .fa-play').parentElement.click();")
            print("✅ সফল: প্লে বাটনে ক্লিক করা হয়েছে!")
        except Exception as e:
            print("বিকল্প পদ্ধতিতে খোঁজা হচ্ছে...")
            # যদি আইকন দিয়ে কাজ না হয়, তবে ক্লাসের নাম দিয়ে ক্লিক করবে
            start_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'btn-primary') or contains(@class, 'btn-success')]")))
            driver.execute_script("arguments[0].click();", start_btn)
            print("✅ সফল: বিকল্প পদ্ধতিতে ক্লিক করা হয়েছে!")

    except Exception as e:
        print(f"❌ ভুল হয়েছে: {e}")
        driver.save_screenshot("debug_screen.png") # সমস্যা হলে ছবি তুলে রাখবে
    finally:
        driver.quit()

if __name__ == "__main__":
    run_bot()
    
