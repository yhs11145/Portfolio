import sys,os,time
from selenium import webdriver
from bs4 import BeautifulSoup
import win32com.client

if getattr(sys, 'frozen', False):
    Chrome_path = os.path.join(sys._MEIPASS, "ChromeDriver.exe")
    driver = webdriver.Chrome(Chrome_path)
else:#
    driver=webdriver.Chrome()

excel=win32com.client.Dispatch("Excel.Application")
excel.Visible=True
workbook=excel.Workbooks.Add()
wb=workbook.Worksheets("Sheet1")

url=(["https://www.assacom.com/shop/product/view_tab_add1_u1.htm?part=2&dex=0&pno=5283&ono=1214&exe=Y&item=item3&item_var=&new_code=202106050221329310421&u1=one",
    'https://www.assacom.com/shop/product/view_tab_add1_u1.htm?part=2&dex=1&pno=5283&ono=1222&exe=Y&item=item12&item_var=&new_code=202106050226203459464&u1=one'])##아싸컴 주소

for i in url:##아싸컴 가격비교 검색(조립)
    driver.get(i)
    html=driver.page_source
    soup=BeautifulSoup(html,'html.parser')
    for name in soup.select('body > div > div > div.frame__content > table > tbody > tr > td.ex-pro_name'):
        print(name.text.strip())
    for price in soup.select('body > div > div > div.frame__content > table > tbody > tr > td.ex-price'):
        print(price.text.strip())
