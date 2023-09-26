def policy_manager_header_element(driver):
    policy_manager_header = (driver
                             .find_element_by_xpath("//android.widget.TextView[@text='Policy management']"))
    return policy_manager_header
