import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_contains_add_to_basket_button(browser):
    browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    browser.implicitly_wait(2)
    assert EC.visibility_of((By.CSS_SELECTOR, ".btn-add-to-basket"))
    time.sleep(30)
