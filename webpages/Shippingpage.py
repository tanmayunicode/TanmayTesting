import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from webpages.Checkoutpage import CheckOutPage


class ShippingPage:

    def __init__(self,driver):
        self.driver = driver

    btn_continue = (By.XPATH,"//*[text()='Continue']")

    def clickContinue(self):
        self.driver.find_element(*self.btn_continue).click()
        checkoutpage = CheckOutPage(self.driver)
        return checkoutpage