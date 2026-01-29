import os
import time
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# --- আপনার তথ্য ---
EMAIL = "hay.salman.ahmed@gmail.com"
PASSWORD = "Salman890@#"
LOGIN_URL = "https://wispbyte.com/client/auth/login" 
SERVER_URL = "https://wispbyte.com/client/servers/a40bf993/console"

def run_bot():
    # ক্রোম অপশন কনফিগারেশন
    options = uc.ChromeOptions()
    
    # Termux-এর জন্য গুরুত্বপূর্ণ সেটিংস
    options.add_argument('--headless')  # ব্যাকগ্রাউন্ডে চালানোর জন্য
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    
    # অটোমেশন ডিটেকশন এড়ানোর প্যারামিটার
    options.add_argument('--disable-popup-blocking')
    options.add_argument("user-agent=Mozilla/5.0 (Linux; Android 13; SM-S911B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36")

    try:
        print("🚀 Undetected Driver সেটআপ হচ্ছে...")
        # Termux এর নির্দিষ্ট chromedriver পাথ ব্যবহার করে ড্রাইভার শুরু করা
        driver = uc.Chrome(
            options=options, 
            driver_executable_path='/data/data/com.termux/files/usr/bin/chromedriver'
        )
        
        # ক্লাউডফ্লেয়ারকে ধোঁকা দেওয়ার জন্য জাভাস্ক্রিপ্ট মাস্কিং
        driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

        print(f"🔗 {LOGIN_URL} ওপেন হচ্ছে...")
        driver.get(LOGIN_URL)
        
        # ক্লাউডফ্লেয়ার চ্যালেঞ্জ লোড হওয়ার জন্য পর্যাপ্ত সময় দিন
        print("⏳ ক্লাউডফ্লেয়ার ভেরিফিকেশনের জন্য ৪০ সেকেন্ড অপেক্ষা করছি...")
        time.sleep(40) 

        # --- ক্লাউডফ্লেয়ার চ্যালেঞ্জ ক্লিক করার লজিক (নতুন যুক্ত করা হয়েছে) ---
        print("🛡️ ক্লাউডফ্লেয়ার চ্যালেঞ্জ চেক করছি...")
        try:
            # এটি ক্লাউডফ্লেয়ারের সাধারণ চেক বক্স খোঁজার চেষ্টা করবে
            driver.switch_to.frame(0) # অনেক সময় ফ্রেমের ভেতর থাকে
            driver.find_element(By.ID, "challenge-stage").click()
            print("✅ ক্লাউডফ্লেয়ার চ্যালেঞ্জে ক্লিক করা হয়েছে!")
            time.sleep(10) # ক্লিকের পর লোড হতে সময় দিন
            driver.switch_to.default_content()
        except:
            print("ℹ️ সরাসরি চ্যালেঞ্জ বাটন পাওয়া যায়নি, পরবর্তী ধাপে যাচ্ছি...")
            driver.switch_to.default_content()

        # -----------------------------------------------------------

        print("🔑 লগইন করার চেষ্টা করছি...")
        wait = WebDriverWait(driver, 30)
        
        try:
            # ইউজারনেম ফিল্ড খুঁজে পাওয়া
            user_input = wait.until(EC.presence_of_element_located((By.NAME, "username")))
            user_input.send_keys(EMAIL)
            
            # পাসওয়ার্ড ফিল্ড
            password_input = driver.find_element(By.NAME, "password")
            password_input.send_keys(PASSWORD)
            
            # লগইন বাটন ক্লিক
            login_btn = driver.find_element(By.XPATH, "//button[@type='submit']")
            driver.execute_script("arguments[0].click();", login_btn)
            print("📡 লগইন ডাটা সাবমিট করা হয়েছে...")
            
        except Exception as login_err:
            print(f"❌ লগইন পেজ লোড হয়নি বা ক্লাউডফ্লেয়ার আটকে দিয়েছে।")
            driver.save_screenshot("cloudflare_issue.png")
            return
        
        # লগইন হওয়ার পর ড্যাশবোর্ড আসার জন্য সময় দিন
        time.sleep(15) 
        
        # সরাসরি সার্ভার কনসোলে যাওয়া
        print(f"🔗 সার্ভার কনসোলে যাচ্ছি: {SERVER_URL}")
        driver.get(SERVER_URL)
        time.sleep(15)

        # প্লে (Start) বাটনে ক্লিক করার লজিক
        print("🖱️ স্টার্ট বাটনে ক্লিক করার চেষ্টা করছি...")
        try:
            # i.fa-play আইকনওয়ালা বাটন খুঁজে বের করা
            play_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "i.fa-play")))
            driver.execute_script("arguments[0].parentElement.click();", play_button)
            print("✅ SUCCESS: সার্ভার স্টার্ট কমান্ড পাঠানো হয়েছে!")
        except:
            print("❌ স্টার্ট বাটন পাওয়া যায়নি (হয়তো সার্ভার অলরেডি রানিং)।")
            driver.save_screenshot("server_status.png")

    except Exception as e:
        print(f"❌ রান-টাইম এরর: {e}")
        driver.save_screenshot("error_snapshot.png")
    
    finally:
        print("🔒 ব্রাউজার বন্ধ হচ্ছে...")
        if 'driver' in locals():
            driver.quit()

if __name__ == "__main__":
    run_bot()
    
