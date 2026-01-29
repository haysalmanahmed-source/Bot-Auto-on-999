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

# আপনার তথ্য
EMAIL = "hay.salman.ahmed@gmail.com"
PASSWORD = "Salman890@#"
# সরাসরি হোম পেজ থেকে লগইন করার চেষ্টা
LOGIN_URL = "https://wispbyte.com/client" 
SERVER_URL = "https://wispbyte.com/client/servers/a40bf993/console"

def run_bot():
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--window-size=1920,1080')
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    wait = WebDriverWait(driver, 45)

    try:
        print("লগইন পেজ ওপেন করা হচ্ছে...")
        driver.get(LOGIN_URL)
        time.sleep(7)

        # যদি সরাসরি ইউজারনেম বক্স না পায়, তবে পুনরায় পেজ লোড করবে
        try:
            username_field = wait.until(EC.presence_of_element_located((By.NAME, "username")))
            print("লগইন বক্স পাওয়া গেছে। তথ্য দেওয়া হচ্ছে...")
            username_field.send_keys(EMAIL)
            driver.find_element(By.NAME, "password").send_keys(PASSWORD)
            
            login_btn = driver.find_element(By.XPATH, "//button[@type='submit']")
            driver.execute_script("arguments[0].click();", login_btn)
            print("লগইন বাটনে ক্লিক করা হয়েছে।")
        except:
            print("লগইন বক্স পাওয়া যায়নি। হয়তো আপনি অলরেডি লগইন অবস্থায় আছেন।")

        time.sleep(15) # ড্যাশবোর্ড লোড হওয়ার পর্যাপ্ত সময়
        
        print("সার্ভার কনসোলে যাওয়া হচ্ছে...")
        driver.get(SERVER_URL)
        time.sleep(15) 

        # প্লে বাটন খোঁজার চেষ্টা
        print("প্লে (Start) বাটন ক্লিক করার চেষ্টা করা হচ্ছে...")
        try:
            # স্ক্রিনশট অনুযায়ী প্লে আইকন ক্লিক
            driver.execute_script("document.querySelector('button i.fa-play, button i.play').parentElement.click();")
            print("✅ SUCCESS: Play button clicked!")
        except Exception as e:
            # বিকল্প পদ্ধতি
            start_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[.//i[contains(@class, 'play')]]")))
            driver.execute_script("arguments[0].click();", start_btn)
            print("✅ SUCCESS: Play button clicked via XPath!")

    except Exception as e:
        print(f"❌ এরর হয়েছে: {e}")
        driver.save_screenshot("login_issue.png")
    finally:
        driver.quit()

if __name__ == "__main__":
    run_bot()
    
