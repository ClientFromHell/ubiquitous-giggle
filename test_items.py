from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, InvalidSelectorException
import time

url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_if_add_to_cart_button_is_available(browser):
    browser.get(url)
    time.sleep(3)
    try:
        button = WebDriverWait(browser, 3).until(
            EC.visibility_of_all_elements_located((By.CLASS_NAME, "1btn-add-to-basket"))
        )
    except (TimeoutException, InvalidSelectorException):
        button = None
    assert button, 'The button is not available on this page'
    #
    #
    # time.sleep(1)
    # browser.implicitly_wait(5)
    # button = browser.find_elements(By.CSS_SELECTOR, '.a1dd-to-basket>button')
    # assert button, "NOT FOUND"
