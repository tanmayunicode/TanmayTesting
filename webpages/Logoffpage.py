import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

class LogOffPage:

    def __init__(self,driver):
        self.driver = driver

    lnk_continue = (By.XPATH,"//*[text()='Continue']")

    def clickContinue(self):
        self.driver.find_element(*self.lnk_continue).click()

