import sys, os, time
import win32com.client
from selenium import webdriver
from bs4 import BeautifulSoup

if getattr(sys, 'frozen', False):
    Chrome_path = os.path.join(sys._MEIPASS, "ChromeDriver.exe")
    driver = webdriver.Chrome(Chrome_path)
else:
    driver=webdriver.Chrome()


excel=win32com.client.Dispatch("Excel.Application")
excel.Visible=True
url=input("엑셀 파일 경로를 입력하세요:")
wb=excel.workbooks.Open(url)
ws=wb.ActiveSheet

a=1
b=30
for i in range(1,int(ws.Cells(1,1).Value)+1):
     word=ws.Cells(1+i,1).Value
     driver.get("https://shopping.naver.com/")
     driver.find_element_by_name("query").send_keys(word)
     driver.find_element_by_xpath('//*[@id="autocompleteWrapper"]/a[2]').click()
     driver.find_element_by_xpath('//*[@id="_pagingSizeLayerWrapper"]/div[1]/button').click()
     driver.find_element_by_xpath('//*[@id="_pagingSizeLayerWrapper"]/div[2]/ul/li[1]/a').click()
     time.sleep(2)
     html=driver.page_source
     soup=BeautifulSoup(html,'html.parser')
     for j in soup.select('div.info > a.tit'):
          ws.Cells(1+i,1+a).Value=j.string
          a+=1
     for k in soup.select('span.depth > a'):
          ws.Cells(1+i,b).Value=k.string
          b+=1
     a=1
     b=30
