from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from conftest import driver_mobile


def should_be_visible(element, driver_mobile=driver_mobile, timeout=10):
    wait = WebDriverWait(driver_mobile.driver, timeout)
    wait.until(ec.visibility_of(element))
