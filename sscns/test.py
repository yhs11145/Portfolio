import sys,os,time
from selenium import webdriver
from bs4 import BeautifulSoup
from datetime import datetime
import win32com.client

if getattr(sys, 'frozen', False):
    Chrome_path = os.path.join(sys._MEIPASS, "ChromeDriver.exe")
    driver = webdriver.Chrome(Chrome_path)
else:#
    driver=webdriver.Chrome()

excel=win32com.client.Dispatch("Excel.Application") ##크롤링 엑셀
excel.Visible=True
wb = excel.Workbooks.Add()
ws = wb.Worksheets("Sheet1")

url=input("제목을 입력하세요") ## 키워드 엑셀
wb1=excel.workbooks.Open(os.getcwd()+'\\'+url)
ws1=wb1.Worksheets("제품명키워드")

#wb1=excel.workbooks.Open('C:\Users\SSCNS\Downloads\삼성 키워드 리스트_210716')
#ws1=wb1.Worksheets('제품명 키워드')
number=1
##(주) 삼성비지니스솔루션
ws.Cells(number,1).Value="삼성비지니스솔루션"
number+=1
driver.get('http://samsungbsmall.com/goods/goods_list.php?cateCd=005001001') ##PC

html=driver.page_source
soup=BeautifulSoup(html,'html.parser')


for i in soup.select('#contents > div > div.content > div.goods_list_item > div.goods_list > div > div > ul > li > div > div.item_info_cont > div.item_tit_box > a > strong'):
    ws.Cells(number,1).Value="삼성 데스크탑"
    ws.Cells(number,2).Value=i.text
    number+=1
    
driver.get('http://samsungbsmall.com/goods/goods_list.php?cateCd=005001002') ##노트북

html=driver.page_source
soup=BeautifulSoup(html,'html.parser')

for j in soup.select('#contents > div > div.content > div.goods_list_item > div.goods_list > div > div > ul > li > div > div.item_info_cont > div.item_tit_box > a > strong'):
    ws.Cells(number,1).Value="삼성 노트북"
    ws.Cells(number,2).Value=j.text
    number+=1
    
driver.get('http://samsungbsmall.com/goods/goods_list.php?cateCd=005001003') ##디스플레이

html=driver.page_source
soup=BeautifulSoup(html,'html.parser')

for k in soup.select('#contents > div > div.content > div.goods_list_item > div.goods_list > div > div > ul > li > div > div.item_info_cont > div.item_tit_box > a > strong'):
    ws.Cells(number,1).Value="삼성 디스플레이"
    ws.Cells(number,2).Value=k.text
    number+=1
    
driver.get('http://samsungbsmall.com/goods/goods_list.php?cateCd=006001001') ##사이니지

html=driver.page_source
soup=BeautifulSoup(html,'html.parser')

for l in soup.select('#contents > div > div.content > div.goods_list_item > div.goods_list > div > div > ul > li > div > div.item_info_cont > div.item_tit_box > a > strong'):
    ws.Cells(number,1).Value="삼성 사이니지"
    ws.Cells(number,2).Value=l.text
    number+=1

### 주봉정보시스템(주)
ws.Cells(number,1).Value="주봉정보시스템"
number+=1

driver.get('http://www.joobongb2b.co.kr/shop/list.html?cateno=1') ##데스크탑

while(1): 
    for page in range(3,12):
        try:
            html=driver.page_source
            soup=BeautifulSoup(html,'html.parser')
            for i in soup.select('#bbslist > div.product-list.product-list--type2 > div.col-12.product-list__item > div.cont-bx > p.title > a'):
                ws.Cells(number,1).Value="삼성 데스크탑"
                ws.Cells(number,2).Value=i.text
                number+=1
            driver.find_element_by_xpath('//*[@id="bbslist"]/div[2]/ul/li['+str(page)+']/a').click()
        except:
            break
    try:
        driver.find_element_by_xpath('//*[@id="bbslist"]/div[2]/ul/li[12]/a').click()
    except:
        break

driver.get('http://www.joobongb2b.co.kr/shop/list.html?cateno=2')    ### 노트북
while(1): 
    for page in range(3,12):
        try:
            html=driver.page_source
            soup=BeautifulSoup(html,'html.parser')
            for i in soup.select('#bbslist > div.product-list.product-list--type2 > div.col-12.product-list__item > div.cont-bx > p.title > a'):
                ws.Cells(number,1).Value="삼성 노트북"
                ws.Cells(number,2).Value=i.text
                number+=1
            driver.find_element_by_xpath('//*[@id="bbslist"]/div[2]/ul/li['+str(page)+']/a').click()
        except:
            break
    try:
        driver.find_element_by_xpath('//*[@id="bbslist"]/div[2]/ul/li[12]/a').click()
    except:
        break
    
driver.get('http://www.joobongb2b.co.kr/shop/list.html?cateno=3')    ### 모니터
while(1): 
    for page in range(3,12):
        try:
            html=driver.page_source
            soup=BeautifulSoup(html,'html.parser')
            for i in soup.select('#bbslist > div.product-list > div > a > div.cont-bx > p.title'):
                ws.Cells(number,1).Value="삼성 모니터"
                ws.Cells(number,2).Value=i.text
                number+=1
            driver.find_element_by_xpath('//*[@id="bbslist"]/div[2]/ul/li['+str(page)+']/a').click()
        except:
            break
    try:
        driver.find_element_by_xpath('//*[@id="bbslist"]/div[2]/ul/li[12]/a').click()
    except:
        break
    
driver.get('http://www.joobongb2b.co.kr/shop/list.html?cateno=5')    ### 사이니지
while(1): 
    for page in range(3,12):
        try:
            html=driver.page_source
            soup=BeautifulSoup(html,'html.parser')
            for i in soup.select('#bbslist > div.product-list > div > a > div.cont-bx > p.title'):
                ws.Cells(number,1).Value="삼성 사이니지"
                ws.Cells(number,2).Value=i.text
                number+=1
            driver.find_element_by_xpath('//*[@id="bbslist"]/div[2]/ul/li['+str(page)+']/a').click()
        except:
            break
    try:
        driver.find_element_by_xpath('//*[@id="bbslist"]/div[2]/ul/li[12]/a').click()
    except:
        break


### (주) 애니텍
ws.Cells(number,1).Value="애니텍"
number+=1
page=1
while(1):
    try:
        driver.get('http://anytec.co.kr/main/shop/list.php?ca_id=1010&sort=&sortodr=&page='+str(page)) ##노트북
        for i in range(1,17):
            driver.find_element_by_xpath('//*[@id="sct_wrap"]/li['+str(i)+']/div/div[1]/a/img').click()
            html=driver.page_source
            soup=BeautifulSoup(html,'html.parser')
            for j in soup.select('#sit_ov > div.sit_ov_wr > div.sit_ov_tbl > table > tbody > tr:nth-child(2) > td'):
                ws.CElls(number,1).Value="삼성 노트북"
                ws.Cells(number,2).Value=j.text
                number+=1
            driver.back()
    except:
        break
    page+=1
    
page=1
while(1):
    try:
        driver.get('http://anytec.co.kr/main/shop/list.php?ca_id=1020&sort=&sortodr=&page='+str(page)) ##데스크탑/올인원
        for i in range(1,17):
            driver.find_element_by_xpath('//*[@id="sct_wrap"]/li['+str(i)+']/div/div[1]/a/img').click()
            html=driver.page_source
            soup=BeautifulSoup(html,'html.parser')
            for j in soup.select('#sit_ov > div.sit_ov_wr > div.sit_ov_tbl > table > tbody > tr:nth-child(2) > td'):
                ws.CElls(number,1).Value="삼성 데스크탑"
                ws.Cells(number,2).Value=j.text
                number+=1
            driver.back()
    except:
        break
    page+=1
    
page=1
while(1):
    try:
        driver.get('http://anytec.co.kr/main/shop/list.php?ca_id=1030&sort=&sortodr=&page='+str(page)) ##모니터
        for i in range(1,17):
            driver.find_element_by_xpath('//*[@id="sct_wrap"]/li['+str(i)+']/div/div[1]/a/img').click()
            html=driver.page_source
            soup=BeautifulSoup(html,'html.parser')
            for j in soup.select('#sit_ov > div.sit_ov_wr > div.sit_ov_tbl > table > tbody > tr:nth-child(2) > td'):
                ws.Cells(number,1).Value="삼성 모니터"
                ws.Cells(number,2).Value=j.text
                number+=1
            driver.back()
    except:
        break
    page+=1
    
page=1
while(1):
    try:    
        driver.get('http://anytec.co.kr/main/shop/list.php?ca_id=2010&sort=&sortodr=&page='+str(page)) ##사이니지
        for i in range(1,17):
            driver.find_element_by_xpath('//*[@id="sct_wrap"]/li['+str(i)+']/div/div[1]/a/img').click()
            html=driver.page_source
            soup=BeautifulSoup(html,'html.parser')
            for j in soup.select('#sit_ov > div.sit_ov_wr > div.sit_ov_tbl > table > tbody > tr:nth-child(2) > td'):
                ws.CElls(number,1).Value="삼성 사이니지"
                ws.Cells(number,2).Value=j.text
                number+=1
            driver.back()
    except:
        break
    page+=1
    
    
    
## (주)우현티앤씨
ws.Cells(number,1).Value="(주)우현티앤씨"
number+=1

driver.get('http://www.woohyuntnc.co.kr/goods/goods_list.php?cateCd=005001') ##노트북

html=driver.page_source
soup=BeautifulSoup(html,'html.parser')
for i in soup.select('#contents > div > div > div.goods_list_item > div.goods_list > div > div > ul > li > div > div.item_info_cont > div.item_tit_box > a > strong'):
    ws.Cells(number,1).Value="삼성 노트북"
    ws.Cells(number,2).Value=i.text
    number+=1
    
driver.get('http://www.woohyuntnc.co.kr/goods/goods_list.php?cateCd=005002') ##모니터

html=driver.page_source
soup=BeautifulSoup(html,'html.parser')
for i in soup.select('#contents > div > div > div.goods_list_item > div.goods_list > div > div > ul > li > div > div.item_info_cont > div.item_tit_box > a > strong'):
    ws.Cells(number,1).Value="삼성 모니터"
    ws.Cells(number,2).Value=i.text
    number+=1
    
driver.get('http://www.woohyuntnc.co.kr/goods/goods_list.php?cateCd=008') ##사이니지

html=driver.page_source
soup=BeautifulSoup(html,'html.parser')
for i in soup.select('#contents > div > div > div.goods_list_item > div.goods_list > div > div > ul > li > div > div.item_info_cont > div.item_tit_box > a > strong'):
    ws.Cells(number,1).Value="삼성 사이니지"
    ws.Cells(number,2).Value=i.text
    number+=1
    
### (주) 도연
ws.Cells(number,1).Value="(주) 도연"
number+=1

driver.get('https://doyeonb2b.com/shop.php?cat_no=29&sw=&sk=&st=&goPage=GoodList&offset=0') 

html=driver.page_source
soup=BeautifulSoup(html,'html.parser')

url=(['https://doyeonb2b.com/shop.php?goPage=GoodList&cat_no=29','https://doyeonb2b.com/shop.php?goPage=GoodList&cat_no=28','https://doyeonb2b.com/shop.php?goPage=GoodList&cat_no=8',
      'https://doyeonb2b.com/shop.php?goPage=GoodList&cat_no=288','https://doyeonb2b.com/shop.php?goPage=GoodList&cat_no=289','https://doyeonb2b.com/shop.php?goPage=GoodList&cat_no=198',
      'https://doyeonb2b.com/shop.php?goPage=GoodList&cat_no=282','https://doyeonb2b.com/shop.php?goPage=GoodList&cat_no=263','https://doyeonb2b.com/shop.php?goPage=GoodList&cat_no=195',
      'https://doyeonb2b.com/shop.php?goPage=GoodList&cat_no=200''https://doyeonb2b.com/shop.php?goPage=GoodList&cat_no=197','https://doyeonb2b.com/shop.php?goPage=GoodList&cat_no=238',
      'https://doyeonb2b.com/shop.php?goPage=GoodList&cat_no=236','https://doyeonb2b.com/shop.php?goPage=GoodList&cat_no=239','https://doyeonb2b.com/shop.php?goPage=GoodList&cat_no=168',
      'https://doyeonb2b.com/shop.php?goPage=GoodList&cat_no=116','https://doyeonb2b.com/shop.php?goPage=GoodList&cat_no=117','https://doyeonb2b.com/shop.php?goPage=GoodList&cat_no=119',
      'https://doyeonb2b.com/shop.php?goPage=GoodList&cat_no=156'])

for link in url:
    try:
        driver.get(link)
        html=driver.page_source
        soup=BeautifulSoup(html,'html.parser')
        for i in soup.select('#contentArea > div.real-cont > div.product-list > ul > li > h3 > strong'):
            ws.Cells(number,2).Value=i.text
            number+=1
    except:
        break
    try:
        driver.get(link+'&sw=&sk=&st=&goPage=GoodList&offset=6')
        html=driver.page_source
        soup=BeautifulSoup(html,'html.parser')
        for i in soup.select('#contentArea > div.real-cont > div.product-list > ul > li > h3 > strong'):
            ws.Cells(number,2).Value=i.text
            number+=1
    except:
        break
    
number=1 ## 크롤링 엑셀
number2=4 ##키워드 엑셀
add=3
add1=0 ##추가할지 말지
while(1):
    try:
        if ws.Cells(number,1).Value in ws.Cells(number2,3).Value:
            number+=1
            number2=3
            add1=0
            break
        else:
            number2+=1
            add1=1
        if add1==1:
            ws1.Cells(10,add).Value=keyword
            number+=1
    except:
        break