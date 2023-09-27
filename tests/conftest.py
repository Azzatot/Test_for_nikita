import pytest
from appium import webdriver


options = {
        "platformName": "android",
        "fullReset": True,
        "appActivity": "com.afwsamples.testdpc.PolicyManagementActivity",
        "bundle_id": "com.afwsamples.testdpc",
        "deviceName": "ZE2232JWS9",
        "app": "D:\\Python\\test_app.apk"
    }


url = "http://localhost:4723/wd/hub"


@pytest.fixture
def driver_mobile():
    driver = webdriver.Remote(
                            url,
                            options
                            )
    yield driver
    driver.quit()
