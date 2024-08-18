from selenium.webdriver.common.by import By
from selenium.webdriver.remote import webdriver


class HomePage:
    driver: webdriver

    def __init__(self, driver):
        self.driver = driver

    search_box_field_id = "q"

    def enter_product_into_search_box_filed(self, product_name):
        self.driver.find_element(By.ID, self.search_box_field_id).click()
        self.driver.find_element(By.ID, self.search_box_field_id).clear()
        self.driver.find_element(By.ID, self.search_box_field_id).send_keys(product_name)
