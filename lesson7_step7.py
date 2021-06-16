from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
  
try: 
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Поиск элемента
    x_element = browser.find_element_by_id('treasure')
    # Взять значение определённого атрибута
    x = x_element.get_attribute('valuex')
    # Посчитать по формуле указанной сверху
    y = calc(x)
    input1 = browser.find_element_by_id('answer').send_keys(y)
    input2 = browser.find_element_by_id('robotCheckbox').click()
    input3 = browser.find_element_by_id('robotsRule').click()
    
    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn").click()
    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()