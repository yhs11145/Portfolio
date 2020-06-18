import urllib.request
import sys
import time
from selenium import webdriver
import urllib.parse
from bs4 import BeautifulSoup
import win32com.client

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

a=1
b=2
c=3
d=4
ws.Cells(1,2).Value="순위"
ws.Cells(1,3).Value="페이지"
ws.Cells(1,4).Value="상품명"
store=input("스토어이름을 입력하세요")
for j in range(2,5001):
     name=ws.Cells(j,1).Value
     url="https://search.shopping.naver.com/search/all.nhn?pagingIndex={}"
     for page in range(50):
          values={
               'query': name
               }
          params=urllib.parse.urlencode(values)
          urls=url.format(page+1)
          urlss=urls+"&"+params
          print("URL=",urlss)
          res=urllib.request.urlopen(urlss)
          soup=BeautifulSoup(res,"html.parser")
          for i in soup.select('div > ul > li > div > p > a.mall_img'):
               if i.string is None:
                    i.string="no"
               if store in i.string:
                    ws.Cells(j,b).Value=a
                    ws.Cells(j,c).Value=page+1
                    driver.get(urlss)
                    driver.find_element_by_xpath('//*[@id="_search_list"]/div[1]/ul/li['+str(a)+']/div[2]/div').click()
                    driver.switch_to.window(driver.window_handles[-1])
                    html=driver.page_source
                    soup=BeautifulSoup(html,'html.parser')
                    time.sleep(3)
                    print(driver.window_handles)
                    for k in soup.select('div > div > div > form > fieldset > div > p > span.thm'):
                         print(k.string)
                         ws.Cells(j,d).Value=k.string
                    b+=3
                    c+=3
                    d+=3
               a+=1
          a=1
