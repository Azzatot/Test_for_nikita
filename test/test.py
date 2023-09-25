from base_driver import options
from helpers.steps import uninstall, install, policy_manager_is_visible, open_app, close_app


def test_app_reinstall():
    uninstall(options)
    install()
    open_app(options)
    policy_manager_is_visible()


def test_app_closed():
    close_app(options)
    open_app(options)
    policy_manager_is_visible()
