import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options


def options():
    cup = UiAutomator2Options()
    cup.platform_name = "android"
    cup.full_reset = True
    cup.app_activity = "com.afwsamples.testdpc.PolicyManagementActivity"
    cup.bundle_id = "com.afwsamples.testdpc"
    cup.device_name = "ZE2232JWS9"
    cup.app = "D:\\Python\\test_app.apk"
    return cup.capabilities


url = "http://localhost:4723/wd/hub"


@pytest.fixture(autouse=True)
def driver_mobile():
    driver = webdriver.Remote(
                            url,
                            options()
                            )
    yield driver
    driver.quit()
