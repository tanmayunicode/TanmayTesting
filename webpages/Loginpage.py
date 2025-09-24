import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from webpages.Shippingpage import ShippingPage


class LoginPage:

    def __init__(self,driver):
        self.driver = driver

    txt_email = (By.NAME,"email_address")
    txt_password = (By.NAME,"password")
    btn_signin = (By.ID,"tdb1")

    def setEmailAddress(self, emailAdd):
        self.driver.find_element(*self.txt_email).send_keys(emailAdd)

    def setPassword(self, pwd):
        self.driver.find_element(*self.txt_password).send_keys(pwd)

    def clicksignin(self):
        self.driver.find_element(*self.btn_signin).click()
        shippingpage = ShippingPage(self.driver)
        return shippingpage