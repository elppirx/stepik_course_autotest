#Работа с элементами, которые закрыты другими элементами - скролл вниз по странице

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)
    valuex = browser.find_element(By.CSS_SELECTOR, "#input_value").text
    y = int(valuex)
    z = calc(y)
    x = str(z)
    #Здесь мы скролим страницу вниз по заданным параметрам,
    #так как нужные нам последующие эелементы находятся ниже области экрана
    browser.execute_script("window.scrollBy(0,100);")
    input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
    input1.send_keys(x)
    chexbox = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    chexbox.click()
    radiobut = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    radiobut.click()
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    time.sleep(10)

finally:
    browser.quit()


#Пустая строка





#browser = webdriver.Chrome()

#можно использовать функцию данную, передав в нее код из js
#browser.execute_script('alert("Robots at work");')

#Можно указывать несколько скриптов на js - просто перечисляя их через точку с запятой
#browser.execute_script('document.title="Script executing";alert("Robots at work");')

#browser.quit()

#link = "https://SunInJuly.github.io/execute_script.html"
#browser.get(link)
#button = browser.find_element(By.TAG_NAME, "button")
#button.click()

#пустая строчка кода