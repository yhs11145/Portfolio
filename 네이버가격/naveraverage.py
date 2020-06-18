import urllib.request
import sys
import time
import urllib.parse
from bs4 import BeautifulSoup
import win32com.client

excel = win32com.client.Dispatch("Excel.Application")
excel.Visible = True
wb = excel.Workbooks.Add()
ws = wb.Worksheets("Sheet1")

name=input("검색할 키워드 입력 :")
a=2
url="https://search.shopping.naver.com/search/all.nhn?pagingIndex={}"
for page in range(3):
     values={
          'query': name
          }
     params=urllib.parse.urlencode(values)
     urls=url.format(page+1)
     urlss=urls+"&"+params
     print("URL=",urlss)
     res=urllib.request.urlopen(urlss)
     soup=BeautifulSoup(res,"html.parser")
     ws.Cells(1,3).Value=time.localtime()
     ws.Cells(1,1).Value="검색한 단어 : " +str(name)
     ws.Cells(a,1).Value=str(page+1)+"페이지"
     for i in soup.select('div > ul > li > div > span > em > span.num._price_reload'):
          ws.Cells(a,2).Value=i.string
          a+=1      
