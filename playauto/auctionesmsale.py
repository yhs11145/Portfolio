from selenium import webdriver
import sys,os,time
from bs4 import BeautifulSoup

if getattr(sys, 'frozen', False):
    chrome_path = os.path.join(sys._MEIPASS, "chromedriver.exe")
    driver = webdriver.Chrome(chrome_path)
else:
    driver=webdriver.Chrome()


id=input('아이디를 입력하세요: ')
pw=input('비밀번호를 입력하세요: ')

driver.get('http://www.esmplus.com/Home/Home#TDM396')
driver.find_element_by_id("Id").send_keys(id)
driver.find_element_by_id("Password").send_keys(pw)
driver.find_element_by_xpath('//*[@id="btnLogOn"]/img').click()
time.sleep(2)
driver.get("http://www.esmplus.com/Sell/SingleGoodsMng?menuCode=TDM396")
time.sleep(2)
driver.find_element_by_xpath('//*[@id="divAcumlSum"]/table/tbody/tr[1]/td[3]/a').click()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="selPageSize"]/option[7]').click()
time.sleep(2)
while(1):
    driver.find_element_by_xpath('//*[@id="gridcolumn-1014-textEl"]').click()
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="goodsContents"]/div[1]/div[1]/div[1]/span[2]/a').click()
    time.sleep(2)
    driver.switch_to.window(driver.window_handles[1])
    driver.find_element_by_xpath('//*[@id="siteTypeIAC"]/input').click()
    driver.maximize_window()
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="SellStateChangeStop"]').click()
    time.sleep(300)
    driver.switch_to.window(driver.window_handles[1])
    driver.find_element_by_xpath('//*[@id="popFooter"]/a/img').click()
    time.sleep(5)
    driver.switch_to.window(driver.window_handles[0])
    

