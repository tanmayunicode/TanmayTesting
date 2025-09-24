import pytest
from selenium.webdriver.common.by import By

from testcases.Baseclass import BaseClass
from webpages.Homepage import HomePage


class TestValidateUser(BaseClass):
    """
    @pytest.mark.parametrize('email,pwd',[("demo@unicodetechnologies.in","unicode"),
                                          ("tanmay.shah1810@unicode.com","unicode"),
                                          ("demo2@unicodetechnologies.in", "unicode2"),
                                          ]
                             )
    """
    @pytest.mark.parametrize('email,pwd',BaseClass.getTestData("TestValidateUser"))
    def test_validateUser(self,email,pwd):

        print(email," and ", pwd)
        homepage = HomePage(self.driver)
        loginpage = homepage.clickLogyourselfin()
        loginpage.setEmailAddress(email)
        loginpage.setPassword(pwd)
        loginpage.clicksignin()

        """
        self.driver.find_element(By.LINK_TEXT,"log yourself in").click()
        self.driver.find_element(By.NAME,"email_address").send_keys("tanmay.shah1810@unicode.com")
        self.driver.find_element(By.NAME,"password").send_keys("unicode")
        self.driver.find_element(By.NAME,"password").send_keys(Keys.ENTER)
        """
        try:
            checkLogin = self.driver.find_element(By.LINK_TEXT,"Log Off").is_displayed()
            print("User has been logged in successfully")
            self.driver.find_element(By.LINK_TEXT,"Log Off").click()
            self.driver.find_element(By.ID,"tdb1").click()

        except:
            print("Invalid Email Address or Password")
            self.driver.get("http://122.170.14.195:8080/uth/gadgetsgallery/catalog")
