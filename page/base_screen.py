from appium import webdriver
from selenium.webdriver.common.by import By


def policy_manager_header_element(driver: webdriver):
    return driver.find_element(By.XPATH, "//android.widget.TextView[@text='Policy management']")
