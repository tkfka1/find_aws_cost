from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from excel import *
import clipboard


url = 'https://calculator.aws/#/addService'



def _init_browser():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.add_experimental_option("excludeSwitches", ['enable-logging'])
    options.add_argument("headless")
    driver = webdriver.Chrome(options=options)

    return driver

def _service_choice(driver):
    WebDriverWait(driver , 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="awsui-select-2-textbox"]'))).click()  # Choose a resion
    WebDriverWait(driver , 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="awsui-select-2-dropdown-option-8"]/div[1]'))).click() # ap-northeast-2 click
    WebDriverWait(driver , 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="awsui-input-0"]'))).send_keys('ec2') # ec2 입력
    time.sleep(1)
    # WebDriverWait(driver , 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[2]/div/div/div/main/div/div[2]/div/div[1]/div/div[2]/awsui-cards/div/ol/li[15]/div/div[3]/div/span/div/div[2]/button'))).click() # ec2 구성 click
    try:
        title = driver.find_element(By.XPATH, '//*[@id="awsui-cards-0-0-header"]/span/span').text
        print(title)
        if(title == 'Amazon EC2'):
            WebDriverWait(driver , 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[2]/div/div/div/main/div/div[2]/div/div[1]/div/div[2]/awsui-cards/div/ol/li[1]/div/div[3]/div/span/div/div[2]/button'))).click() # 구성 click
    except:
        print("error",title)


    
def _configure_EC2(driver, i):
    time.sleep(1)
    WebDriverWait(driver , 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div[2]/div/div/div/main/div/div[2]/div/awsui-modal/div[2]/div/div/div[2]/div/span/div/div[1]/div/div/div/awsui-form/div/div[2]/span/span/div[2]/div/div/div/div[2]/div/div/span[1]/awsui-form-section/div/div[2]/span/div/div/div/div/div/div[6]/awsui-table/div/div[2]/div/div[2]/span/div/div[1]/div/div/div[2]/div/div/div/div/awsui-input/div/input'))).send_keys(NP[i][2]) # 타입 입력
    WebDriverWait(driver , 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div[2]/div/div/div/main/div/div[2]/div/awsui-modal/div[2]/div/div/div[2]/div/span/div/div[1]/div/div/div/awsui-form/div/div[2]/span/span/div[2]/div/div/div/div[2]/div/div/span[1]/awsui-form-section/div/div[2]/span/div/div/div/div/div/div[6]/awsui-table/div/div[3]/table/tbody/tr/td[1]/awsui-radio-button/div/label/input'))).send_keys(Keys.SPACE) # 라디오버튼 타입 설정
    WebDriverWait(driver , 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="on-demand"]'))).send_keys(Keys.SPACE) # On-demand 설정
    WebDriverWait(driver , 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="calculator-app-modal-container"]/div[2]/div/div/div[3]/span/div/div[3]/div/div/div[2]/div/button'))).click() # Finish
    
def _estimate_(driver):
    WebDriverWait(driver , 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="estimate-button"]'))).click() # estimate
    txt3 = WebDriverWait(driver , 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="current-group-label"]/span'))).text # agree-continue
    WebDriverWait(driver , 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[2]/div/div/div/main/div/div[2]/div/div[1]/div/div[1]/div[2]/div/div/div[2]/button'))).click() # save-and-share
    print(WebDriverWait(driver , 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[2]/div/div/div/main/div/div[2]/div/div[1]/div/div[1]/div[2]/div/div/div[2]/button'))).text)
    WebDriverWait(driver , 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div/div[2]/div/div/div[3]/span/span/button[2]'))).click() # agree-continue    
    time.sleep(3)
    # WebDriverWait(driver , 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div/div[2]/div/div/div[2]/section/div/div/div[2]/div/span/button'))).click() # agree-continue
    link = WebDriverWait(driver , 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div/div[2]/div/div/div[2]/section/div/div/div[2]/div/div[1]/input'))).get_attribute('value') # agree-continue
    print(link)
    return link
    


if __name__ == "__main__":
    print("init browser")
    driver = _init_browser()
    driver.get(url)
    for i in range(len(NP)):
        _service_choice(driver)
        _configure_EC2(driver, i)
    link = _estimate_(driver)
    driver.quit()
    print(link)

    # link = clipboard.paste()
    f = open('estimate link.txt', 'a')
    f.write(link)
    f.write('\n')
    f.close()