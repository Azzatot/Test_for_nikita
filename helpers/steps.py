from base_dr import driver, options
from page.onb import policy_manager_header


def uninstall():
    driver.remove_app(app_id=app_package)


def install():
    driver.install_app(app_path="D:\\Python\\test_app.apk")


def open_app():
    driver.activate_app(
                        app_id=app_package
                        )


def policy_manager_is_visible():
    policy_manager_header.should_be_visible()


def close_app():
    driver.terminate_app(
                        app_package
                        )


options_obj = options()
app_package = options_obj.app_package
