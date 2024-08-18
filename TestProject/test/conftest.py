import pytest
from selenium import webdriver

from utilities import ReadConfiguration


@pytest.fixture()
def setup_and_teardown(request):
    browser = ReadConfiguration.read_configuration("basic info", "browser")
    driver = None
    if browser.__eq__("edge"):
        driver = webdriver.Edge()
    elif browser.__eq__("firefox"):
        driver = webdriver.firefox
    else:
        print("driver")
    driver.maximize_window()
    app_url = ReadConfiguration.read_configuration("basic info", "url")
    driver.get(app_url)
    request.cls.driver = driver
    yield
    driver.quit()
