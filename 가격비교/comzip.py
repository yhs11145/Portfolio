import sys,os,time
from selenium import webdriver
from bs4 import BeautifulSoup
import win32com.client

if getattr(sys, 'frozen', False):
    Chrome_path = os.path.join(sys._MEIPASS, "ChromeDriver.exe")
    driver = webdriver.Chrome(Chrome_path)
else:
    driver=webdriver.Chrome()

excel=win32com.client.Dispatch("Excel.Application")
excel.Visible=True
wb=excel.workbooks.Open(os.getcwd()+'\price.xlsx')
ws=wb.Worksheets('컴집')

ws.Cells(1,1).Value="이름"
ws.Cells(1,2).Value="윈도우"
ws.Cells(1,3).Value="cpu"
ws.Cells(1,4).Value="cooler"
ws.Cells(1,5).Value="mainboard"
ws.Cells(1,6).Value="ram"
ws.Cells(1,7).Value="RGB ram"
ws.Cells(1,8).Value="vga"
ws.Cells(1,9).Value="ssd"
ws.Cells(1,10).Value="hdd"
ws.Cells(1,11).Value="cd/dvd"
ws.Cells(1,12).Value="sound"
ws.Cells(1,13).Value="lan"
i=2
cnt=0
j=2

url=(['https://www.comzip.co.kr/shopuser/goods/productList.html?largeno=152&middleno=1&kind=normal',
'https://www.comzip.co.kr/shopuser/goods/productList.html?largeno=152&middleno=2&kind=normal',
'https://www.comzip.co.kr/shopuser/goods/productList.html?largeno=152&middleno=3&kind=normal',
'https://www.comzip.co.kr/shopuser/goods/productList.html?largeno=152&middleno=4&kind=normal',
'https://www.comzip.co.kr/shopuser/goods/productList.html?largeno=152&middleno=5&kind=normal',
'https://www.comzip.co.kr/shopuser/goods/productList.html?largeno=152&middleno=6&kind=normal'])

for link in url:
    driver.get(link)
    time.sleep(2)
    html=driver.page_source
    soup=BeautifulSoup(html,'html.parser')
    for name in soup.select('td:nth-child(2) > table > tbody > tr:nth-child(3) > td > table > tbody > tr > td > b > a'):
        ws.Cells(i,1).Value=name.text.strip()
        i+=1
        cnt+=1
    i-=cnt
    for price in soup.select('td:nth-child(2) > table > tbody > tr:nth-child(7) > td > table > tbody > tr > td'):
        ws.Cells(i,2).Value=price.text.strip()
        i+=1
    i-=cnt
    for info in soup.select('td:nth-child(2) > table > tbody > tr:nth-child(10) > td > table > tbody > tr > td:nth-child(2)'):
        ws.Cells(i,j).Value=info.text.strip()
        j+=1
        if '3년무상' in info.text.strip():
            i+=1
            j=3
    cnt=0

    
