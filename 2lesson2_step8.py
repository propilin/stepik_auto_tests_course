from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
   
    input1 = browser.find_element(By.NAME, "firstname")
    input1.send_keys("Maxim")
    input2 = browser.find_element(By.NAME, "lastname")
    input2.send_keys("Shcherbakov")
    input3 = browser.find_element(By.NAME, "email")
    input3.send_keys("mcpropilin@gmail.com")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    input4 = browser.find_element(By.CSS_SELECTOR, "[type='file']")
    input4.send_keys(file_path)
    button = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    button.click()

finally:
    # успеваем скопировать код за 10 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла