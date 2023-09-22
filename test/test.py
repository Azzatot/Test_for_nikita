from helpers.steps import open_app, tap_continue_btn
from page.onb import continue_btn


def test_app_opened():
    open_app("tech.plink.PlinkApp")


def test_pass_preview():
    continue_btn.should_be_visible()
    [tap_continue_btn() for _ in range(4)]

