#Работа с ожиданиями на странице

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    #Здесь мы передаем в переменную значение, которое ожидает, пока элемент появиться на странице,
    #и как только появиться, то запускает слудующий код, за ожиданием
    pricewin = WebDriverWait(browser, 20).until(
        EC.text_to_be_present_in_element((By.ID, 'price'), '$100'))

    butbook = browser.find_element(By.CSS_SELECTOR, '#book')
    butbook.click()
    valuex = browser.find_element(By.CSS_SELECTOR, '#input_value').text
    z = int(valuex)
    y = calc(z)
    x = str(y)
    input1 = browser.find_element(By.CSS_SELECTOR, '#answer')
    input1.send_keys(x)

    #скролим страницу вниз
    browser.execute_script('window.scrollBy(0, 100);')
    butsub = browser.find_element(By.ID, 'solve')
    butsub.click()

    time.sleep(10)

finally:
    browser.quit()

#empty str






