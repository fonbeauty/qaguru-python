import pytest
from selene.support.shared import browser
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope='session', autouse=True)
def config():
    ChromeDriverManager(path="/Users/a18980620/PythonProject/qaguru-python/Drivers").install()
    browser.config.window_width = 1000
    browser.config.window_height = 600


@pytest.fixture
def open_browser():
    browser.open('https://google.com')
