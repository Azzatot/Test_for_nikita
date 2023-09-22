from base_dr import driver
from page.onb import continue_btn


def uninstall():
    driver.remove_app("tech.plink.PlinkApp")


def open_app(app_id: str):
    driver.activate_app(app_id)


def tap_continue_btn():
    continue_btn.tap()
