import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


@pytest.mark.usefixtures("setup_and_teardown")
class TestSignup:
    driver: WebDriver

    def test_valid_signup(self):
        self.driver.find_element(By.ID, "topActionSell").click()
        time.sleep(3)
        self.driver.find_element(By.LINK_TEXT, "Create a new account").click()
        time.sleep(5)
        # self.driver.find_element(By.ID, "phone").send_keys("0187124178")
        # time.sleep(3)
        # # self.driver.find_element(By.CLASS_NAME, "primary-button-daraz").click()
        # # time.sleep(3)
        # self.driver.find_element(By.LINK_TEXT,"Login in").click()
        # time.sleep(3)
