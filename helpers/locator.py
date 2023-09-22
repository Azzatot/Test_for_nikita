from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.mobileby import MobileBy


def by(selector: str):
    if selector.startswith("text="):
        return MobileBy.XPATH, f"//*[@text='{selector[5:]}']"

    if selector.startswith('contain_text='):
        return MobileBy.XPATH, f'//*[contains(@text, "{selector[13:]}")]'

    if selector.startswith('class='):
        return MobileBy.CLASS_NAME, selector[6:]

    if selector.lower().startswith("textview="):
        return (
            MobileBy.XPATH, f"//android.widget.TextView[@text='{selector[9:]}']"
            )
    if selector.startswith("id="):
        return AppiumBy.ID, selector[3:]

    if selector.startswith("accId="):
        return MobileBy.ACCESSIBILITY_ID, selector[6:]

    if selector.startswith("id="):
        return MobileBy.ACCESSIBILITY_ID, selector[3:]

    if (
            selector.startswith('/')
            or selector.startswith('./')
            or selector.startswith('..')
            or selector.startswith('(')
    ):
        return MobileBy.XPATH, selector

    if selector.startswith('**/'):
        return MobileBy.IOS_CLASS_CHAIN, selector

    return MobileBy.ACCESSIBILITY_ID, selector