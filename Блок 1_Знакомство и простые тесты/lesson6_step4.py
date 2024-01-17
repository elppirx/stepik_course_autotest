from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/simple_form_find_task.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.CSS_SELECTOR, '.form-group:nth-of-type(1) .form-control')
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, 'last_name')
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CLASS_NAME, 'form-control.city')
    input3.send_keys("San Francisco")
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("USA")
    button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    button.click()

finally:
    #успеваем скопировать полученный код за 30 секунд
    time.sleep(30)
    #закрываем браузер после всех манипуляций
    browser.quit()

#незабываем оставить пустую строку в конце файла, если ее не будет в скрипте,
#то последняя строчка, содержащая код, может не выполниться.
