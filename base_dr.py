from appium import webdriver


desired_caps = {
    "platformName": "android",
    "fullReset": True,
    "appWaitActivity": "com.dog_app.plink.*",
    "appPackage": "tech.plink.PlinkApp",
    "language": "en",
    "locale": "US",
    "deviceName": "ZE2232JWS9",
    "platformVersion": "10",
    "app": "D:\\Python\\app-release.apk"
}

url = "http://localhost:4723/wd/hub"

driver = webdriver.Remote(
                        url,
                        desired_caps
                        )
