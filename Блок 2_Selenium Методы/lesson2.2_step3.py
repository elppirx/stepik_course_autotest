#Работа с загрузкой файлов

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
import os

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.CSS_SELECTOR, "[name='firstname']")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.CSS_SELECTOR, "[name='lastname']")
    input2.send_keys("Ivanov")
    input3 = browser.find_element(By.CSS_SELECTOR, "[name='email']")
    input3.send_keys("mymalo@gmail.com")

    #Загружаем файл
    #Сначала получаем путь к текущему файлу, с помощью метода импортируемой библиотеки
    current_dir = os.path.abspath(os.path.dirname(__file__))
    #Далее мы добавляем к пути имя файла, который находится в этой же директории
    file_path = os.path.join(current_dir, 'file.txt')
    #Находим элемент, где нужно загрузить файл
    file_input = browser.find_element(By.CSS_SELECTOR, "#file")
    #Загружаем с помощью метода send_keys, только в качестве аргумента передаем путь к файлу, который мы сохранили ранее
    file_input.send_keys(file_path)


    #Нажимаем на кнопку submit
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    time.sleep(10)

finally:
    browser.quit()


#empty str