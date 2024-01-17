from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    findex = browser.find_element(By.CSS_SELECTOR, "#treasure")
    y = findex.get_attribute("valuex")
    x = calc(y)
    input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
    input1.send_keys(x)
    checeb = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    checeb.click()
    radiobut = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    radiobut.click()
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    time.sleep(10)

finally:
    browser.quit()

#пустая строка