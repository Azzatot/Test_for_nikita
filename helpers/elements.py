from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from base_driver import driver


def should_be_visible(element, timeout=10):
    wait = WebDriverWait(driver, timeout)
    wait.until(ec.visibility_of(element))
