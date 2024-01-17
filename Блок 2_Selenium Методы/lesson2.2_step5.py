#Работа с новой вкладкой браузера

from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    buttonsw = browser.find_element(By.CSS_SELECTOR, "button.btn")
    #Здесь мы нажимаем на кнопку и открывается новая вкладка браузера, а Селениум остается на 1 вкладке
    buttonsw.click()
    #Сохраняем первую вкладку по индексу 0 в переменную
    frist_window = browser.window_handles[0]
    #сохраняем вторую вкладку в переменную по индексу 1
    new_window = browser.window_handles[1]
    #данной командой меняем вкладку на новую, указывая переменую, в которой сохранили новую вкладку
    browser.switch_to.window(new_window)
    valuex = browser.find_element(By.CSS_SELECTOR, "#input_value").text
    z = int(valuex)
    y = calc(z)
    x = str(y)
    input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
    input1.send_keys(x)
    butsub = browser.find_element(By.CSS_SELECTOR, "button.btn")
    butsub.click()

    time.sleep(10)

finally:
    browser.quit()


#empty str
