import time
import math
from selenium import webdriver
from selenium.webdriver.support.ui import Select

def calc(i, b):
    return str(int(i) + int(b))


try:
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Поиск элемента
    i_element = browser.find_element_by_id('num1')
    # Взять значение определённого атрибута
    i = i_element.text
    # Поиск элемента
    b_element = browser.find_element_by_id('num2')
    # Взять значение определённого атрибута
    b = b_element.text
    # Посчитать по формуле указанной сверху
    y = calc(i, b)
    print(calc(i, b))

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(y)

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
