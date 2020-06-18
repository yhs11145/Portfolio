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
url=input("엑셀 파일 경로를 입력하세요. :")
wb=excel.workbooks.Open(url)
ws=wb.ActiveSheet

id='dorothy600'
pw='claeo1@3'
m=8

for i in range(2,7):
     name=ws.Cells(i,1).Value
     driver.get('https://sellper.kr/keywordsearch.html')
     time.sleep(2)
     driver.find_element_by_xpath('//*[@id="keyword"]').send_keys(name)
     driver.find_element_by_xpath('//*[@id="submit-btn"]').click()
     time.sleep(2)
     html=driver.page_source
     soup=BeautifulSoup(html,'html.parser')
     for pc in soup.select('tbody.list > tr > td.mpcqry'):
          ws.Cells(i,2).Value=pc.string
     for mobile in soup.select('tbody.list > tr > td.mmoqry'):
          ws.Cells(i,3).Value=mobile.string
     for sumsearch in soup.select('tbody.list > tr > td.mtoqry'):
          ws.Cells(i,4).Value=sumsearch.string
     for product in soup.select('tbody.list > tr > td.item_num'):
          ws.Cells(i,5).Value=product.string
     for factor in soup.select('tbody.list > tr > td.skfactor'):
          ws.Cells(i,6).Value=factor.string

driver.get('https://manage.searchad.naver.com/customers/1598814/tool/keyword-planner')
time.sleep(2)
driver.find_element_by_id('uid').send_keys(id)
driver.find_element_by_id('upw').send_keys(pw)
driver.find_element_by_xpath('//*[@id="container"]/div/div/fieldset/div/span/button').click()

for j in range(2,7):
     driver.get('https://manage.searchad.naver.com/customers/1598814/tool/keyword-planner')
     time.sleep(2)
     name=ws.Cells(j,1).Value
     driver.find_element_by_xpath('//*[@id="wrap"]/div/div/div[1]/div[1]/div/div/div/div[2]/div[1]/div[1]/div[2]/form/div[1]/div/div/textarea').send_keys(name)
     driver.find_element_by_xpath('//*[@id="wrap"]/div/div/div[1]/div[1]/div/div/div/div[2]/div[1]/div[1]/div[2]/form/div[4]/div/div/ul/li/button/span').click()
     time.sleep(2)
     html=driver.page_source
     soup=BeautifulSoup(html,'html.parser')
     for k in range(3,9):
          for naver in soup.select("#wgt-"+str(name)+" > td:nth-child("+str(k)+")"):
               ws.Cells(j,m).Value=naver.string
               m+=1
     m=8
               
          
     
