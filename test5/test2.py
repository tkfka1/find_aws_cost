from selenium import webdriver
import chromedriver_autoinstaller
chromedriver_autoinstaller.install()
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

URL = 'https://calculator.aws/#/createCalculator/ec2-enhancement'
options = Options()
options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
driver = webdriver.Chrome(options=options)
# driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)



def open_page(url):
    driver.get(url)
    
def close_browser():
    driver.quit()
    
def get_data():
    # 특정 요소가 로드될 때까지 명시적으로 대기
    # 예: ID가 'element_id'인 요소의 가시성을 기다림
    # 참고: 실제 사용할 때는 'element_id'를 페이지에 존재하는 실제 요소의 ID로 변경해야 함
    element = wait.until(EC.visibility_of_element_located((By.ID, 'element_id')))    
    # 데이터 추출 로직
    data = element.text  # 대기가 끝난 후 해당 요소의 텍스트를 가져옴
    return data
    
def wait_browser(t):
    driver.implicitly_wait(t)


def find_element_by_id(id):
    return driver.find_element(by=By.ID, value=id).text


def find_element_by_xpath(xpath):
    return driver.find_element(by=By.XPATH,value=xpath).text

try:
    open_page(URL)
    # 페이지 로딩이나 데이터 로딩을 기다릴 필요가 있는 경우에는 time.sleep() 대신 적절한 WebDriverWait을 사용합니다.
    time.sleep(5)  # 실제 사용 시에는 WebDriverWait 사용을 권장합니다.
    # data = scraper.get_data()
    data = find_element_by_xpath('//*[@id="ec2enhancement"]/div')
    print(data)

finally:
    print("@@@@")
    close_browser()