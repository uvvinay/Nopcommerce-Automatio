from selenium import webdriver
import pytest
import undetected_chromedriver as uc
from selenium.webdriver.common.service import Service


#@pytest.fixture
#def setup(browser):
 #   if browser == "chrome":
  #      driver = webdriver.ChromeOptions()
        #driver = webdriver.Chrome()
   #     return driver
    #elif browser == "firefox":
     #   driver = webdriver.FirefoxOptions()
      #  return driver
    #elif browser == "ie":
     #   driver = webdriver.IeOptions()
      #  return driver


@pytest.fixture
def setup():
   options= uc.ChromeOptions()
   #options.add_argument('--headless=new')
   options.add_argument('--no-sandbox')
   options.add_argument("--disable-blink-features=AutomationControlled")
   driver = uc.Chrome(options=options)
   return driver
#to avoid the duplicate code or repeated code we can created this config
#file and call the setup method where we cau re use this drivers
#Ex: self.driver = webdriver.Chrome()  this code is used in both
#login_home_title and login_page in testcases instead used of this we can use setup method

def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--headless")


@pytest.fixture
def browser(request):
    return request.config.getoption("--browser")


#*********  pytest html reports

# it is hooks adding environment info to html report
def pytest_configure(config):
    config.metadata['project name'] = 'Slenium Nop Commerse'
    config.metadata['module name'] = 'Customers'
    config.metadata['Tester'] = 'Vinay'


@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("plugins", None)
