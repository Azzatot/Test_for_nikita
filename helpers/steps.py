from base_driver import driver
from helpers.elements import should_be_visible
from page.base_screen import policy_manager_header


def uninstall(app_options):
    bundle_id = app_options.app_package
    driver.remove_app(app_id=bundle_id)


def install():
    driver.install_app(app_path="D:\\Python\\test_app.apk")


def open_app(app_options):
    bundle_id = app_options.app_package
    driver.activate_app(
                        app_id=bundle_id
                        )


def policy_manager_is_visible():
    should_be_visible(policy_manager_header)


def close_app(app_options):
    bundle_id = app_options.app_package
    driver.terminate_app(
                        bundle_id
                        )
