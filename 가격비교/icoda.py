import sys,os,time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import win32com.client
from datetime import datetime

if getattr(sys, 'frozen', False):
    Chrome_path = os.path.join(sys._MEIPASS, "ChromeDriver.exe")
    driver = webdriver.Chrome(Chrome_path)
else:
    driver=webdriver.Chrome()

driver.get('https://usr.icoda.co.kr/')##아이코다

excel=win32com.client.Dispatch("Excel.Application")##엑셀가져오기
excel.Visible=True
wb=excel.workbooks.Open(os.getcwd()+'\icoda.xlsx')
for number in range(1,15):##셀번호 이동
    ws=wb.Worksheets(number)
    i=3
    while(1):
        code=ws.Cells(i,1).Value
        driver.find_element_by_xpath('//*[@id="search_inp"]').clear()
        if code is None:
            i+=1
            continue
        else:
            driver.find_element_by_xpath('//*[@id="search_inp"]').send_keys(code)##검색어 입력
        driver.find_element_by_xpath('//*[@id="search_btn"]').click()##검색

        productprice=driver.find_element_by_xpath('//*[@id="pno_section"]/ul/li/div[4]/div[2]/div[2]/div[1]/span').text #가격
        ws.Cells(i,4).Value=productprice

        i+=1
        if(ws.Cells(i,2).Value is None):
            break


wb.SaveAs(os.getcwd()+'\\'+str(datetime.today().strftime('%Y-%m-%d'))+'아이코다.xlsx')