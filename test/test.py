from helpers import steps
from base_driver import options


def test_app_reinstall():
    steps.uninstall(options)
    steps.install()
    steps.open_app(options)
    steps.policy_manager_is_visible()


def test_app_closed():
    steps.close_app(options)
    steps.open_app(options)
    steps.policy_manager_is_visible()
