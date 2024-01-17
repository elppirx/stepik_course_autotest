#Работа с окнами, Alerts и как с ними жить

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = 'http://suninjuly.github.io/alert_accept.html'
    browser = webdriver.Chrome()
    browser.get(link)

    button1 = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    button1.click()
    #переходим на окно alert
    confirm = browser.switch_to.alert
    #подтвеждаем в окне alert
    confirm.accept()
    valuex = browser.find_element(By.CSS_SELECTOR, '#input_value').text
    valuy = int(valuex)
    y = calc(valuy)
    x = str(y)
    input_val = browser.find_element(By.CSS_SELECTOR, '#answer')
    input_val.send_keys(x)
    button2 = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    button2.click()

    time.sleep(10)

finally:
    browser.quit()


#empty str

