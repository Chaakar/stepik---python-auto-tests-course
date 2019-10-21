from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

# Solution for the https://stepik.org/lesson/181384/step/8 task


# function used in captcha calculation
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/explicit_wait2.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)

    # waiting for the price to be $100
    priceLabel = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    button = browser.find_element_by_id("book")
    button.click()

    # calculating captcha
    x = int(browser.find_element_by_id("input_value").text)
    y = calc(x)
    answerField = browser.find_element_by_id("answer")
    answerField.send_keys(y)
    answerField.submit()

finally:
    # waiting to manually assure, that test was performed correctly
    time.sleep(10)
    browser.quit()
