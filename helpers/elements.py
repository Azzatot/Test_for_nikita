from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


def should_be_visible(element, driver, timeout=10):
    wait = WebDriverWait(driver, timeout)
    wait.until(ec.visibility_of(element))
