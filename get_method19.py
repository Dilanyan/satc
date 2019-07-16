from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

options = webdriver.ChromeOptions()

options.add_experimental_option('w3c', False)

browser = webdriver.Chrome(options=options)

browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
message_value = WebDriverWait(browser, 5).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '10000')
    )
	
button = browser.find_element_by_id("book")
button.click()

x_element = browser.find_element_by_id("input_value")
x = x_element.text
y = calc(x)

input1 = browser.find_element_by_id('answer')
input1.send_keys(y)

button1 = browser.find_element_by_id("solve")
button1.click()