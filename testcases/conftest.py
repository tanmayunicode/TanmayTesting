import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def pytest_addoption(parser):
    parser.addoption("--browserVal", action="store", default="chrome")
    parser.addoption("--urlVal", action="store", default="production")


@pytest.fixture(scope="class")
def startUP(request):

    browser = request.config.getoption("--browserVal")
    print(browser)
    if browser == "chrome":
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
    elif browser == "edge":
        service = Service("D:\\Software\\Selenium\\msedgedriver.exe")  # Path to downloaded driver
        driver = webdriver.Edge(service=service)
    elif browser == "safari":
        driver = webdriver.Safari()

    driver.maximize_window()
    driver.implicitly_wait(5)

    url = request.config.getoption("--urlVal")
    print(url)
    if url == "localhost":
        driver.get("http://localhost/uth/gadgetsgallery/catalog")
    elif url == "production":
        driver.get("http://122.170.14.195:8080/uth/gadgetsgallery/catalog/")

    request.cls.driver=driver
