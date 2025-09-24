import time
from testcases.Baseclass import BaseClass
from webpages.Homepage import HomePage


class TestPayment(BaseClass):

    def test_paymentScenario(self):

        logs = self.generateLogs()
        logs.info("We are in Homepage")
        homepage = HomePage(self.driver)
        self.driver.save_screenshot("/Users/tanmayshah/Documents/Batches/BA275PythonFramework/screenshots/HomePage.png")
        categorypage = homepage.clickHeadphones()
        time.sleep(2)
        self.driver.save_screenshot("/Users/tanmayshah/Documents/Batches/BA275PythonFramework/screenshots/CategoryPage.png")

        logs.info("We are in CategoryPage")
        shoppingcartpage = categorypage.clickBuyNow()
        time.sleep(2)
        self.driver.save_screenshot("/Users/tanmayshah/Documents/Batches/BA275PythonFramework/screenshots/ShoppingCart.png")

        logs.info("We are in Shopping Cart Page")

        loginpage = shoppingcartpage.clickCheckout()
        self.driver.save_screenshot("/Users/tanmayshah/Documents/Batches/BA275PythonFramework/screenshots/LoginPage.png")

        logs.info("We are in LoginPage")

        loginpage.setEmailAddress("tanmay.shah1810@unicode.com")
        loginpage.setPassword("unicode")
        time.sleep(2)
        shippingpage = loginpage.clicksignin()
        self.driver.save_screenshot("/Users/tanmayshah/Documents/Batches/BA275PythonFramework/screenshots/ShippingCartPage.png")

        logs.info("We are in ShippingCart Page")

        time.sleep(2)
        checkoutpage = shippingpage.clickContinue()
        checkoutpage.clickCashonDelivery()
        time.sleep(2)
        checkoutpage.setComments("I need my order ASAP")
        logs.info("We are in CheckoutPage")

        orderconfirmation = checkoutpage.clickContinue()
        time.sleep(2)
        logs.info("We are in OrderConfirmation Page")
        self.driver.save_screenshot("/Users/tanmayshah/Documents/Batches/BA275PythonFramework/screenshots/OrderConfirmation.png")

        successpage = orderconfirmation.clickConfirmOrder()
        time.sleep(2)
        logs.info("We are in Success Page")
        self.driver.save_screenshot("/Users/tanmayshah/Documents/Batches/BA275PythonFramework/screenshots/SuccessPage.png")

        welcomepage = successpage.clickContinue()
        time.sleep(2)
        logs.info("We are in Welcome Page")

        logoffpage = welcomepage.clicklogoff()
        time.sleep(2)
        logs.info("We are in Log Off Page")

        logoffpage.clickContinue()
        """
        time.sleep(1)
        allCategories = self.driver.find_elements(By.XPATH,"//div[@id='left_sidebar']/div[1]/div[2]/a")

        for category in allCategories:
            catName = category.text
            if catName=="Headphones":
                category.click()
                break
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//*[text()='Sony MDR XB650']/parent::td/following-sibling::td[2]/span/a").click()
        time.sleep(1)

        self.driver.find_element(By.XPATH,"//*[text()='Checkout']").click()
        time.sleep(1)

        self.driver.find_element(By.NAME, "email_address").send_keys("tanmay.shah1810@unicode.com")
        self.driver.find_element(By.NAME, "password").send_keys("unicode")
        time.sleep(1)
        self.driver.find_element(By.NAME, "password").send_keys(Keys.ENTER)
        time.sleep(1)

        self.driver.find_element(By.XPATH,"//*[text()='Continue']").click()
        time.sleep(1)

        self.driver.find_element(By.XPATH,"//*[text()='Cash on Delivery']/parent::td/following-sibling::td/input").click()
        time.sleep(1)

        self.driver.find_element(By.NAME,"comments").send_keys("I need my orders ASAP")
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//*[text()='Continue']").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//*[text()='Confirm Order']").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//*[text()='Continue']").click()
        time.sleep(1)
        self.driver.find_element(By.LINK_TEXT,"Log Off").click()
        time.sleep(1)
        self.driver.find_element(By.ID,"tdb1").click()
        """


