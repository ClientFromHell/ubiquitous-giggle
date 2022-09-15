from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_if_add_to_cart_button_is_available(browser):
    browser.get(url)
    time.sleep(30)
    try:
        button = WebDriverWait(browser, 3).until(
            EC.visibility_of_all_elements_located((By.CLASS_NAME, "btn-add-to-basket"))
        )
    except TimeoutException:
        button = None
    assert button, 'The button is not available on this page'


