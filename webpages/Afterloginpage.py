import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from webpages.Logoffpage import LogOffPage


class WelcomePage:

    def __init__(self,driver):
        self.driver = driver

    lnk_logoff = (By.XPATH,"//*[text()='Log Off']")

    def clicklogoff(self):
        self.driver.find_element(*self.lnk_logoff).click()
        logoffpage = LogOffPage(self.driver)
        return logoffpage