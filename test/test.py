from helpers.steps import uninstall, install, policy_manager_is_visible, open_app, close_app


def test_app_reinstall():
    uninstall()
    install()
    open_app()
    policy_manager_is_visible()


def test_app_closed():
    close_app()
    open_app()
    policy_manager_is_visible()
