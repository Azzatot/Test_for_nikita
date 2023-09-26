import pytest

from helpers import steps


@pytest.mark.usefixtures('driver_mobile')
def test_app_reinstall(driver):
    steps.uninstall(driver)
    steps.install(driver)
    steps.open_app(driver)
    steps.policy_manager_is_visible(driver)


def test_app_closed(driver_mobile):
    steps.close_app(driver_mobile)
    steps.open_app(driver_mobile)
    steps.policy_manager_is_visible(driver_mobile)
