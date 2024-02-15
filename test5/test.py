from selenium import webdriver
import chromedriver_autoinstaller
chromedriver_autoinstaller.install()
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
import time

class AWSCalculatorScraper:
    def __init__(self):
        self.options = Options()
        self.options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
        # self.options.add_experimental_option()
        self.driver = webdriver.Chrome(options=self.options)
        self.wait = WebDriverWait(self.driver, 10)
    
    def open_page(self, url):
        self.driver.get(url)
    
    def close_browser(self):
        self.driver.quit()
    
    def get_data(self):
        # 특정 요소가 로드될 때까지 명시적으로 대기
        # 예: ID가 'element_id'인 요소의 가시성을 기다림
        # 참고: 실제 사용할 때는 'element_id'를 페이지에 존재하는 실제 요소의 ID로 변경해야 함
        element = self.wait.until(EC.visibility_of_element_located((By.ID, 'element_id')))
        
        # 데이터 추출 로직
        data = element.text  # 대기가 끝난 후 해당 요소의 텍스트를 가져옴
        
        return data
    
    def wait_browser(self,t):
        self.driver.implicitly_wait(t)
    

    def find_element_by_id(self, id):
        return self.driver.find_element(by=By.ID, value=id).text

    
    def find_element_by_xpath(self, xpath):
        return self.driver.find_element(by=By.XPATH,value=xpath).text
    
    def click_selector(self, pat):
        self.driver.find_element(by=By.CSS_SELECTOR, value=pat).click()

    def find_scroll(self, pat):
        option = self.driver.find_element(by=By.XPATH, value=pat)
        self.driver.execute_script("arguments[0].scrollIntoView();", option)
        option.click()


if __name__ == "__main__":

    URL = 'https://calculator.aws/#/createCalculator/ec2-enhancement'
    scraper = AWSCalculatorScraper()

    # try:
    #     scraper.open_page(URL)
    #     # 페이지 로딩이나 데이터 로딩을 기다릴 필요가 있는 경우에는 time.sleep() 대신 적절한 WebDriverWait을 사용합니다.
    #     time.sleep(5)  # 실제 사용 시에는 WebDriverWait 사용을 권장합니다.
    #     # data = scraper.get_data()
    #     data = scraper.find_element_by_xpath('//*[@id="ec2enhancement"]/div')
    #     print(data)

    # finally:
    #     print("@@@@")
    #     #scraper.close_browser()
# <div id="1684-1707967022366-7293" class=""><button id="formField1678-1707967022366-9167" type="button" class="awsui_button-trigger_18eso_kcg3o_97 awsui_pressed_18eso_kcg3o_180 awsui_has-caret_18eso_kcg3o_164" aria-expanded="true" aria-labelledby="formField1678-1707967022366-9167-label select-arialabel-1682-1707967022366-1909 trigger-content-1686-1707967022366-96" aria-haspopup="dialog" aria-controls="dialog1681-1707967022366-7295"><span id="trigger-content-1686-1707967022366-96" class="awsui_trigger_dwuol_duyiz_116">아시아 태평양(서울)</span><span class="awsui_arrow_18eso_kcg3o_97"><span class="awsui_icon_h11ix_19jzl_98 awsui_size-normal-mapped-height_h11ix_19jzl_152 awsui_size-normal_h11ix_19jzl_148 awsui_variant-normal_h11ix_19jzl_224"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" focusable="false" aria-hidden="true"><path class="filled stroke-linejoin-round" d="M4 5h8l-4 6-4-6z"></path></svg></span></span></button></div>
    try:
        data = scraper.find_element_by_xpath('//*[@id="ec2enhancement"]/div')
        print(data)
        x = scraper.click_selector('#ec2enhancement > div > div.awsui_grid-column_14yj0_o8rqb_137.awsui_colspan-10_14yj0_o8rqb_238 > div > div > div.awsui_root_1i0s3_1krki_93 > div > div.awsui_content_5gtk3_epevd_129 > div > div.awsui_root_18582_frdpw_93.awsui_vertical_18582_frdpw_140.awsui_vertical-m_18582_frdpw_155 > div > div > div > div > div > div > div > div > div:nth-child(2) > div > div > div > div.awsui_controls_14mhv_dicza_240 > div > div > div > div > div > div')
        # x.select_by_index(2)
        scraper.find_scroll("//*[text()='ap-northeast-2']")
        
    finally:
        print("@@@@")