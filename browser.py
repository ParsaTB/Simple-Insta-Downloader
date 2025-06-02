from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def download_instagram(instagram_url):
    options = webdriver.ChromeOptions()
    options.headless = True
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    driver = webdriver.Chrome(options=options)
    
    try:
        driver.get("https://fastdl.app/en")
                
        input_box = driver.find_element(By.ID, "search-form-input")
        input_box.send_keys(instagram_url)
        
        search_btn = driver.find_element(By.CLASS_NAME, "search-form__button")
        search_btn.click()
        
        wait = WebDriverWait(driver, 10)
        
        caption_elem = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#app > section.search-result > div > div > div.output-list__caption > p")))
        like_count_elem = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "output-list__info-like")))
        time_posted_elem = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "output-list__info-time")))
        comment_count_elem = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "output-list__info-comment")))
        
        download_btn = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a.button__download")))
        href = download_btn.get_attribute("href")
        
        caption = caption_elem.text
        like_count = like_count_elem.text
        time_posted = time_posted_elem.text
        comment_count = comment_count_elem.text
        
        return href, caption, like_count, time_posted, comment_count
    
    except Exception as e:
        print(f"Error : {e}")
        return None, None, None, None, None
    finally:
        driver.close()