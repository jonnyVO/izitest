import pytest
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities

from pages.pages import HomePage


@pytest.fixture
def firefox_driver():
    #firefox_capabilities = DesiredCapabilities.FIREFOX
    #firefox_capabilities['marionette'] = True
    #firefox_capabilities['binary'] = '/usr/local/bin/geckodriver'
    driver = webdriver.Firefox(
        executable_path='/usr/local/bin/geckodriver',
        #capabilities=firefox_capabilities,
    )

    yield driver

    driver.close()


@pytest.fixture
def page_factory(firefox_driver):
    firefox_driver.maximize_window()
    firefox_driver.implicitly_wait(20)
    firefox_driver.set_page_load_timeout(60)

    def _factory(page_name):
        page = page_name(firefox_driver)
        page.open()

        return page

    return _factory


@pytest.fixture
def home_page(page_factory):
    return page_factory(HomePage)