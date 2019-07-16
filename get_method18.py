from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

options = webdriver.ChromeOptions()

options.add_experimental_option('w3c', False)

browser = webdriver.Chrome(options=options)

browser.get("http://suninjuly.github.io/wait2.html")

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
button = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.ID, "check"))
    )
button.click()
message = browser.find_element_by_id("check_message")

assert "успешно" in message.text