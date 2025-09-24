import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from webpages.Afterloginpage import WelcomePage


class SuccessPage:

    def __init__(self,driver):
        self.driver = driver

    btn_continue = (By.XPATH,"//*[text()='Continue']")

    def clickContinue(self):
        self.driver.find_element(*self.btn_continue).click()
        welcomepage = WelcomePage(self.driver)
        return welcomepage
