import sys, os, time
import win32com.client
from selenium import webdriver
from bs4 import BeautifulSoup

if getattr(sys, 'frozen', False):
    Chrome_path = os.path.join(sys._MEIPASS, "ChromeDriver.exe")
    driver = webdriver.Chrome(Chrome_path)
else:
    driver=webdriver.Chrome()

a=2
b=2
c=2

id="genetickorea"
pw="gk#50900"
ad=input("검색할 키워드를 입력해주세요")
driver.get("https://searchad.naver.com/")
driver.find_element_by_id("uid").send_keys(id)
driver.find_element_by_id("upw").send_keys(pw)
driver.find_element_by_xpath('//*[@id="container"]/main/div/div[1]/home-login/div/fieldset/span/button').click()
driver.get("https://manage.searchad.naver.com/customers/1139809/tool/keyword-planner")
driver.implicitly_wait(5)
driver.find_element_by_xpath('//*[@id="wrap"]/div/div/div[1]/div[1]/div/div/div/div[2]/div[1]/div[1]/div[2]/form/div[1]/div/div/textarea').send_keys(ad)
driver.find_element_by_xpath('//*[@id="wrap"]/div/div/div[1]/div[1]/div/div/div/div[2]/div[1]/div[1]/div[2]/form/div[4]/div/div/ul/li/button').click()
time.sleep(3)
driver.find_element_by_xpath('//*[@id="wrap"]/div/div/div[1]/div[1]/div/div/div/div[2]/div[1]/div[2]/div[1]/div/button').click()
driver.get("https://shopping.naver.com/home/p/index.nhn")
driver.find_element_by_xpath('//*[@id="autocompleteWrapper"]/input[1]').send_keys(ad)
driver.find_element_by_xpath('//*[@id="autocompleteWrapper"]/a[2]').click()
time.sleep(2)

excel=win32com.client.Dispatch("Excel.Application")
excel.Visible=True
url=input("엑셀 파일 경로를 입력하세요:")
wb=excel.workbooks.Open(url)
ws=wb.ActiveSheet
ws.Cells(1,13).Value="판매자"
ws.Cells(1,14).Value="url"
ws.Cells(1,15).Value="카테고리"
html=driver.page_source
soup=BeautifulSoup(html,'html.parser')
for i in soup.select('div > ul > li > div > p > a.mall_img'):
    ws.Cells(a,13).Value=i.string
    a+=1
for k in soup.select('div > ul > li > div > a.tit'):
    ws.Cells(c,14).Value=k.get('href')
    c+=1
for j in soup.select('div > ul > li > div > span.depth > a'):
    ws.Cells(b,15).Value=j.string
    b+=1
