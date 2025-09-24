import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from webpages.Shoppingcartpage import ShoppingCartPage


class CategoryPage:

    def __init__(self,driver):
        self.driver = driver

    lnk_productBuyNow = (By.XPATH,"//*[text()='Sony MDR XB650']/parent::td/following-sibling::td[2]/span/a")

    def clickBuyNow(self):
        self.driver.find_element(*self.lnk_productBuyNow).click()
        shoppingcartpage = ShoppingCartPage(self.driver)
        return shoppingcartpage
