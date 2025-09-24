import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from webpages.Orderonfirmationpage import OrderConfirmationPage


class CheckOutPage:

    def __init__(self,driver):
        self.driver = driver

    btn_cod = (By.XPATH,"//*[text()='Cash on Delivery']/parent::td/following-sibling::td/input")
    txt_comments = (By.NAME,"comments")
    btn_continue = (By.XPATH,"//*[text()='Continue']")


    def clickCashonDelivery(self):
        self.driver.find_element(*self.btn_cod).click()

    def setComments(self, comment):
        self.driver.find_element(*self.txt_comments).send_keys(comment)

    def clickContinue(self):
        self.driver.find_element(*self.btn_continue).click()
        orderconfirmationpage = OrderConfirmationPage(self.driver)
        return orderconfirmationpage