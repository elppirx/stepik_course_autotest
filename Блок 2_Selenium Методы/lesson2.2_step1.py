#Работа со списками и выбор из выпадающего и из невыпадающего списка

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver .support.ui import Select

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)


    num1 = browser.find_element(By.CSS_SELECTOR, "#num1").text
    numfirst = int(num1)
    num2 = browser.find_element(By.CSS_SELECTOR, "#num2").text
    numsecond = int(num2)
    result = numfirst + numsecond
    resnew = str(result)
    print(resnew)
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(resnew)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    time.sleep(10)

finally:
    browser.quit()


#осталяем пустую строку
