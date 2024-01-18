from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest

class TestAbs(unittest.TestCase):
    def test_abs1(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        input1 = browser.find_element(By.CSS_SELECTOR, '.first_block:nth-of-type(1) .first')
        input1.send_keys('John')
        input2 = browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your last name"]')
        input2.send_keys('Smith')
        input3 = browser.find_element(By.CSS_SELECTOR, 'input.third')
        input3.send_keys('mymail@gmail.com')
        button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
        button.click()

        time.sleep(3)

        welcome_text = browser.find_element(By.TAG_NAME, "h1").text

        assert welcome_text == 'Congratulations! You have successfully registered!'

        time.sleep(10)

        browser.quit()

    def test_abs2(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        input1 = browser.find_element(By.CSS_SELECTOR, '.first_block:nth-of-type(1) .first')
        input1.send_keys('John')
        input2 = browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your last name"]')
        input2.send_keys('Smith')
        input3 = browser.find_element(By.CSS_SELECTOR, 'input.third')
        input3.send_keys('mymail@gmail.com')
        button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
        button.click()

        time.sleep(3)

        welcome_text = browser.find_element(By.TAG_NAME, "h1").text

        assert welcome_text == 'Congratulations! You have successfully registered!'

        time.sleep(10)

        browser.quit()



if __name__ == '__main__':
    pytest.main()