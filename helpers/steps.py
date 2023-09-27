import os

from helpers.elements import should_be_visible
from page.base_screen import policy_manager_header_element
from tests.conftest import options


def uninstall(driver):
    driver.remove_app(options["bundle_id"])


def install(driver):
    app_path = os.path.join(os.getcwd(), "../test_app.apk")
    driver.install_app(app_path=app_path)


def open_app(driver):
    driver.activate_app(options["bundle_id"])


def policy_manager_is_visible(driver):
    element = policy_manager_header_element(driver)
    should_be_visible(element, driver)


def close_app(driver):
    driver.terminate_app(options["bundle_id"])
