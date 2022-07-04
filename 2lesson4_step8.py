from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    WebDriverWait(browser, 20).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    button1 = browser.find_element(By.ID, "book")
    button1.click()
    browser.execute_script("window.scrollBy(0, 400);")

    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)
    input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
    input1.send_keys(y)
    button2 = browser.find_element(By.ID, "solve")
    button2.click()

finally:
    
    time.sleep(10) 
    
    browser.quit()