import sys,os,time
from selenium import webdriver
from bs4 import BeautifulSoup
import win32com.client

if getattr(sys, 'frozen', False):
    Chrome_path = os.path.join(sys._MEIPASS, "ChromeDriver.exe")
    driver = webdriver.Chrome(Chrome_path)
else:
    driver=webdriver.Chrome()


j=2
cnt=0
excel=win32com.client.Dispatch("Excel.Application")
excel.Visible=True
wb=excel.workbooks.Open(os.getcwd()+'\price.xlsx')
ws=wb.Worksheets('블루아이티')
#wb=excel.workbooks.Add()
#ws=wb.WorkSheets("Sheet1")

url=(['https://www.blueit.co.kr/skin/shop/basicwide/system_list_include_plist.php?group_no=&group_type=&cate1=&cate2=&game=&sprice=300000&eprice=400000&event_no=&pc_title=30~40만원대',
'https://www.blueit.co.kr/skin/shop/basicwide/system_list_include_plist.php?group_no=&group_type=&cate1=&cate2=&game=&sprice=400000&eprice=500000&event_no=&pc_title=40~50만원대',
'https://www.blueit.co.kr/skin/shop/basicwide/system_list_include_plist.php?group_no=&group_type=&cate1=&cate2=&game=&sprice=500000&eprice=600000&event_no=&pc_title=50~60만원대',
'https://www.blueit.co.kr/skin/shop/basicwide/system_list_include_plist.php?group_no=&group_type=&cate1=&cate2=&game=&sprice=600000&eprice=700000&event_no=&pc_title=60~70만원대',
'https://www.blueit.co.kr/skin/shop/basicwide/system_list_include_plist.php?group_no=&group_type=&cate1=&cate2=&game=&sprice=700000&eprice=800000&event_no=&pc_title=70~80만원대',
'https://www.blueit.co.kr/skin/shop/basicwide/system_list_include_plist.php?group_no=&group_type=&cate1=&cate2=&game=&sprice=800000&eprice=900000&event_no=&pc_title=80~90만원대',
'https://www.blueit.co.kr/skin/shop/basicwide/system_list_include_plist.php?group_no=&group_type=&cate1=&cate2=&game=&sprice=900000&eprice=1000000&event_no=&pc_title=90~100만원대',
'https://www.blueit.co.kr/skin/shop/basicwide/system_list_include_plist.php?group_no=&group_type=&cate1=&cate2=&game=&sprice=1000000&eprice=1200000&event_no=&pc_title=100~120만원대',
'https://www.blueit.co.kr/skin/shop/basicwide/system_list_include_plist.php?group_no=&group_type=&cate1=&cate2=&game=&sprice=1200000&eprice=1500000&event_no=&pc_title=120~150만원대',
'https://www.blueit.co.kr/skin/shop/basicwide/system_list_include_plist.php?group_no=&group_type=&cate1=&cate2=&game=&sprice=1500000&eprice=2000000&event_no=&pc_title=150~200만원대',
'https://www.blueit.co.kr/skin/shop/basicwide/system_list_include_plist.php?group_no=&group_type=&cate1=&cate2=&game=&sprice=2000000&eprice=3000000&event_no=&pc_title=200~300만원대',
'https://www.blueit.co.kr/skin/shop/basicwide/system_list_include_plist.php?group_no=&group_type=&cate1=&cate2=&game=&sprice=3000000&eprice=10000000&event_no=&pc_title=300만원대 이상'])

for i in url:
    k=2
    driver.get(i)
    time.sleep(2)
    html=driver.page_source
    soup=BeautifulSoup(html,'html.parser')
    for name in soup.select('body > form > table > tbody > tr > td > table:nth-child(3) > tbody > tr > td > table > tbody > tr > td > table:nth-child(1) > tbody > tr > td > b > a > font:nth-child(1)'):
        ws.Cells(j,1).Value=name.text.strip()
        j+=1
        cnt+=1
    j-=cnt
    cnt=0
    for info in soup.select('body > form > table > tbody > tr > td > table:nth-child(3) > tbody > tr > td > table > tbody > tr > td> table:nth-child(2) > tbody > tr > td > span'):
        ws.Cells(j,k).Value=info.text.strip()
        if '완본체 PC 사은품' in info.text.strip():
            j+=1
            cnt+=1
            k=1
        k+=1
    j-=cnt
    cnt=0
    for price in soup.select('body > form > table > tbody > tr > td > table:nth-child(3) > tbody > tr > td > table > tbody > tr > td > table:nth-child(3) > tbody > tr:nth-child(2) > td > a'):
        ws.Cells(j,20).Value=price.text.strip()
        j+=1
    