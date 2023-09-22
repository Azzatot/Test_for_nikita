import time
from typing import List

from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver import WebElement
from appium.webdriver.common.touch_action import TouchAction
from selenium.common import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait

from base_dr import driver
from helpers.locator import by


class NoSuchElementAssertion(AssertionError):
    pass


class Element:

    def __init__(
            self,
            locator: tuple,
            driver=lambda: driver
    ):
        self._locator = locator
        self._driver_source = driver if callable(driver) else lambda: driver

    @property
    def mobile_driver(self) -> WebDriver:
        return self._driver_source()

    def wait(self, timeout=10) -> 'Element':
        try:
            WebDriverWait(self.mobile_driver, timeout).until(
                EC.visibility_of_element_located(self._locator)
            )
        except ():
            pass
        return self

    def locate(self, index=None) -> WebElement:
        try:
            if index is None:
                return self.mobile_driver.find_element(*self._locator)
            else:
                return self.mobile_driver.find_elements(*self._locator)[index]
        except NoSuchElementException as e:
            raise NoSuchElementAssertion(e.__str__() + f'locator of element {self._locator}')

    def locate_all(self) -> List[WebElement]:
        return self.wait().mobile_driver.find_elements(*self._locator)

    def text(self, index=None, timeout=10) -> str:
        return self.wait(timeout).locate(index).text

    def type(self, text: str, index=None, clear=True, timeout=10):
        field = self.wait(timeout=timeout).locate(index)
        field.clear() if clear else ...
        field.send_keys(text)

    def tap(self, index=None, timeout=10):
        action = TouchAction(self.mobile_driver)
        action.tap(self.wait(timeout=timeout).locate(index)).perform()
        return self

    def should_be_visible(self, index=None, timeout=10):
        self.is_displayed(index=index, timeout=timeout)
        return self

    def is_displayed(self, index=None, timeout=10):  # -> bool | dict:
        try:
            return self.wait(timeout=timeout).locate(index=index).is_displayed()
        except ():
            return False

    def should_have_text(
            self,
            expected_text: str,
            index=None,
            timeout=10,
    ) -> 'Element':
        while timeout * 2 > 0:
            actual_text = self.text(index, timeout)
            if actual_text == expected_text:
                break
            time.sleep(0.43)
            timeout -= 1
        return self

    def should_be_enabled(self, index=None, timeout=10):
        self.wait(timeout=timeout).locate(index).is_enabled()

    def should_not_be_enabled(self, index=None, timeout=10):
        self.wait(timeout=timeout).locate(index).is_enabled()

    def should_be_checked(self, index=None, timeout=10):
        self.wait(timeout=timeout).locate(index).get_attribute('checked'),


def element(android=None) -> Element:
    return Element(by(android))
