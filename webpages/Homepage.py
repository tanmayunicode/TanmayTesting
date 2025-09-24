import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from webpages.Categorypage import CategoryPage
from webpages.Loginpage import LoginPage


class HomePage:

    lnk_logyourselfin = (By.LINK_TEXT,"log yourself in")
    lnk_createAnAccount = (By.LINK_TEXT,"create an account")
    lnk_headphones = (By.XPATH,"//a[text()='Headphones']")

    def __init__(self,driver):
        self.driver = driver

    def clickLogyourselfin(self):
        self.driver.find_element(*self.lnk_logyourselfin).click()
        loginpage = LoginPage(self.driver)
        return loginpage

    def clickCreateAnAccount(self):
        self.driver.find_element(*self.lnk_createAnAccount).click()

    def clickHeadphones(self):
        self.driver.find_element(*self.lnk_headphones).click()
        categorypage = CategoryPage(self.driver)
        return categorypage