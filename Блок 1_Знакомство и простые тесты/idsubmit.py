import time

from selenium import webdriver
from selenium.webdriver.common.by import By

#Для того, чтобы гарантировать закрытие,
#даже если произошла ошибка в предыдущих строках, проще всего использовать конструкцию try/finally
try:
    link = "http://suninjuly.github.io/simple_form_find_task.html"
    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(5)
    button = browser.find_element(By.ID, "submit_button")
    button.click()
finally:
    # Закрываем браузер
    browser.quit()