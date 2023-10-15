import pytest
from selene import browser
from selenium import webdriver

from config import config
from ozon_demo_project.utils import attach


@pytest.fixture(scope='function', autouse=True)
def browser_setup():
    if config.browser_name == 'chrome':
        options = webdriver.ChromeOptions()
    else:
        options = webdriver.FirefoxOptions()

    browser.config.window_width = config.window_width
    browser.config.window_height = config.window_height
    browser.config.driver_options = options
    browser.config.base_url = config.base_url

    yield

    attach.add_html(browser)
    attach.add_screenshot(browser)

    if config.browser_name == 'chrome':
        attach.add_logs(browser)

    browser.quit()
