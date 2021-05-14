import sys,os,time
from selenium import webdriver
from bs4 import BeautifulSoup
import win32com.client

if getattr(sys, 'frozen', False):
    Chrome_path = os.path.join(sys._MEIPASS, "ChromeDriver.exe")
    driver = webdriver.Chrome(Chrome_path)
else:
    driver=webdriver.Chrome()

driver.get('http://www.compuzone.co.kr/product/iworks_list.htm')
time.sleep(2)
for i in range(1,8):
    driver.find_element_by_xpath('//*[@id="iw_2020_wrap"]/div[3]/div[1]/table/tbody/tr[2]/td[i]/span').click()
    driver.find_element_by_xpath('//*[@id="iw_2020_wrap"]/div[3]/div[3]/table/tbody/tr/td/a[2]').click()
    
    html=driver.page_source
    soup=BeautifulSoup(html,'html.parser')

    driver.find_element_by_xpath('//*[@id="iw_2020_wrap"]/div[3]/div[1]/table/tbody/tr[2]/td[i]/span').click()

