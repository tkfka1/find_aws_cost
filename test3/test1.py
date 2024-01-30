from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

# WebDriver 설정
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# 대상 URL
url = 'https://calculator.aws/#/createCalculator/ec2-enhancement'

# 웹 페이지 접근
driver.get(url)

# 페이지가 완전히 로드될 때까지 기다림 (필요에 따라 시간 조정)
time.sleep(5)

# 페이지의 HTML 내용을 가져옴
page_content = driver.page_source

# HTML 내용 출력
print(page_content)

# # 브라우저 종료
# driver.quit()
