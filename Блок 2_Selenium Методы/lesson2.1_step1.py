from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    y=x_element.text
    x = calc(y)
    input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
    input1.send_keys(x)
    checkbox1 = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    checkbox1.click()
    radiobutton1 = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    radiobutton1.click()
    button1 = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button1.click()

    time.sleep(10)

finally:
    browser.quit()

#пустая строка