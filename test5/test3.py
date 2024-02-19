import chromedriver_autoinstaller
chromedriver_autoinstaller.install()
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

co = Options()
co.add_experimental_option('debuggerAddress', '127.0.0.1:9222')
driver = webdriver.Chrome(options=co)
driver.get('https://calculator.aws/#/createCalculator/ec2-enhancement')