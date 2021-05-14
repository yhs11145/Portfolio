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
ws=wb.Worksheets('팝콘피씨')

ws.Cells(1,1).Value="이름"
ws.Cells(1,2).Value="가격"
ws.Cells(1,3).Value="윈도우"
ws.Cells(1,4).Value="모니터"
ws.Cells(1,5).Value="cpu"
ws.Cells(1,6).Value="cooler"
ws.Cells(1,7).Value="ram"
ws.Cells(1,8).Value="minboard"
ws.Cells(1,9).Value="vga"
ws.Cells(1,10).Value="lan"
ws.Cells(1,11).Value="ssd"
ws.Cells(1,12).Value="hdd"
ws.Cells(1,13).Value="odd"
ws.Cells(1,14).Value="case"
ws.Cells(1,15).Value="power"

i=2
cnt=0
j=3
page=3

url=(['http://popcornpc.co.kr/skin/shop/basic/system_list_include_plist.php?group_no=&group_type=&cate1=&cate2=11015&game=&sprice=&eprice=&event_no=&pc_title=완제품컴퓨터_전체보기',
'http://popcornpc.co.kr/skin/shop/basic/system_list_include_plist.php?group_no=&group_type=&cate1=&cate2=11040&game=&sprice=&eprice=&event_no=&pc_title=',
'http://popcornpc.co.kr/skin/shop/basic/system_list_include_plist.php?group_no=&group_type=&cate1=&cate2=11039&game=&sprice=&eprice=&event_no=&pc_title=라이젠컴퓨터_(3세대)',
'http://popcornpc.co.kr/skin/shop/basic/system_list_include_plist.php?group_no=&group_type=&cate1=&cate2=11135&game=&sprice=&eprice=&event_no=&pc_title=본체 모니터패키지',
'http://popcornpc.co.kr/skin/shop/basic/system_list_include_plist.php?group_no=&group_type=&cate1=&cate2=11254&game=&sprice=&eprice=&event_no=&pc_title=사무',
'http://popcornpc.co.kr/skin/shop/basic/system_list_include_plist.php?group_no=&group_type=&cate1=&cate2=11019&game=&sprice=&eprice=&event_no=&pc_title=사무 / 가정용 / 멀티미디어',
'http://popcornpc.co.kr/skin/shop/basic/system_list_include_plist.php?group_no=&group_type=&cate1=&cate2=11021&game=&sprice=&eprice=&event_no=&pc_title=3D게임 / 디자인 / 개인방송'])

for link in url:
    driver.get(link)
    time.sleep(2)
    html=driver.page_source
    soup=BeautifulSoup(html,'html.parser')
    for name in soup.select('tbody > tr > td > table:nth-child(1) > tbody > tr:nth-child(2) > td > b > a > font:nth-child(1)'):
        ws.Cells(i,1).Value=name.text.strip()
        i+=1
        cnt+=1
    i-=cnt
    for price in soup.select('tbody > tr > td > table:nth-child(1) > tbody > tr:nth-child(3) > td > a'):
        ws.Cells(i,2).Value=price.text.strip()
        i+=1
    i-=cnt
    for info in soup.select('tbody > tr > td > table:nth-child(2) > tbody > tr > td > table > tbody > tr > td > div'):
        ws.Cells(i,j).Value=info.text.strip()
        j+=1
        if '출장' in info.text.strip():
            i+=1
            j=3
    cnt=0


        


        