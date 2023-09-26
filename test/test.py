from helpers import steps


def test_app_reinstall(driver_mobile):
    steps.uninstall(driver_mobile)
    steps.install(driver_mobile)
    steps.open_app(driver_mobile)
    steps.policy_manager_is_visible(driver_mobile)


def test_app_closed(driver_mobile):
    steps.close_app(driver_mobile)
    steps.open_app(driver_mobile)
    steps.policy_manager_is_visible(driver_mobile)
