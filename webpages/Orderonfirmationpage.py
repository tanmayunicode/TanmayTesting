import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from webpages.successage import SuccessPage


class OrderConfirmationPage:

    def __init__(self,driver):
        self.driver = driver

    btn_confirmorder = (By.XPATH,"//*[text()='Confirm Order']")

    def clickConfirmOrder(self):
        self.driver.find_element(*self.btn_confirmorder).click()
        successpage = SuccessPage(self.driver)
        return successpage