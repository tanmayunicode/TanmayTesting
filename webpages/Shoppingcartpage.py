import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from webpages.Loginpage import LoginPage


class ShoppingCartPage:

    def __init__(self,driver):
        self.driver = driver

    lnk_checkout = (By.XPATH,"//*[text()='Checkout']")

    def clickCheckout(self):
        self.driver.find_element(*self.lnk_checkout).click()
        loginpage = LoginPage(self.driver)
        return loginpage