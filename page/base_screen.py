from conftest import driver_mobile


def policy_manager_header_element(driver_mobile=driver_mobile):
    policy_manager_header = (driver_mobile.driver
                             .find_element_by_xpath("//android.widget.TextView[@text='Policy management']"))
    return policy_manager_header
