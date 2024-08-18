import time

import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.edge.webdriver import WebDriver


@pytest.mark.usefixtures("setup_and_teardown")
class TestSeller:
    driver: WebDriver

    def test_invalid_id(self):
        self.driver.find_element(By.ID, "topActionSell").click()
        time.sleep(3)
        self.driver.find_element(By.ID, "account").send_keys("01871241878")
        time.sleep(2)
        self.driver.find_element(By.ID, "password").send_keys("abc")
        self.driver.find_element(By.CLASS_NAME, "login-button-daraz").click()
        time.sleep(2)
        expected_text = "Invalid account or password."
        assert self.driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/form[1]/div[1]/div[1]/div[1]").text.__eq__(expected_text)
        time.sleep(5)

    def test_valid_id(self):
        self.driver.find_element(By.ID, "topActionSell").click()
        time.sleep(3)
        self.driver.find_element(By.ID, "account").send_keys("01871241878")
        time.sleep(2)
        self.driver.find_element(By.ID, "password").send_keys("abc")
        self.driver.find_element(By.CLASS_NAME, "login-button-daraz").click()
        time.sleep(2)
        expected_text = "Invalid account or password."
        assert self.driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/form[1]/div[1]/div[1]/div[1]").text.__eq__(expected_text)
        time.sleep(5)