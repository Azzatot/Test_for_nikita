import os

from conftest import driver_mobile
from helpers.elements import should_be_visible
from page.base_screen import policy_manager_header_element


def uninstall(driver):
    driver.remove_app(driver.bundle_id)


def install(driver):
    app_path = os.path.join(os.getcwd(), "test_app.apk")
    driver.install_app(app_path=app_path)


def open_app(driver):
    driver.activate_app(driver.bundle_id)


def policy_manager_is_visible(driver):
    should_be_visible(policy_manager_header_element(driver))


def close_app(driver_mobile=driver_mobile):
    driver_mobile.driver.terminate_app(bundle_id)
