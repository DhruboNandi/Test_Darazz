import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from pages.homepage import HomePage


@pytest.mark.usefixtures("setup_and_teardown")
class TestSearch:
    driver: WebDriver

    def test_search_for_valid_product(self):
        home_page = HomePage(self.driver)
        home_page.enter_product_into_search_box_filed("Honestime Presents Tenda F3 300mbps 3 Antennas Router")
        # self.driver.find_element(By.ID, "q").send_keys("Honestime Presents Tenda F3 300mbps 3 Antennas Router")
        # time.sleep(2)
        self.driver.find_element(By.CLASS_NAME, "search-box__button--1oH7").click()
        time.sleep(2)
        assert self.driver.find_element(By.PARTIAL_LINK_TEXT, "Honestime Presents ").is_displayed()
        time.sleep(5)

    def test_search_for_invalid_product(self):
        self.driver.find_element(By.ID, "q").send_keys("qgdhgd")
        time.sleep(2)
        self.driver.find_element(By.CLASS_NAME, "search-box__button--1oH7").click()
        time.sleep(2)
        expected_text = "Search No Result"
        assert self.driver.find_element(By.CLASS_NAME, "jG0xV ").text.__eq__(expected_text)
        time.sleep(5)

    def test_search_for_no_product(self):
        self.driver.find_element(By.CLASS_NAME, "search-box__button--1oH7").click()
        time.sleep(2)
        assert self.driver.find_element(By.CLASS_NAME, "p-mod-card-content ").is_displayed()
        time.sleep(5)
