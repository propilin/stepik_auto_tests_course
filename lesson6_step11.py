from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)
   
    input1 = browser.find_element(By.CSS_SELECTOR, "div.first_block>div.form-group.first_class>.form-control")
    input1.send_keys("Maxim")
    input2 = browser.find_element(By.CSS_SELECTOR, "div.first_block>div.form-group.second_class>.form-control")
    input2.send_keys("mcpropilin@gmail.com")
    button = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    button.click()
# Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла