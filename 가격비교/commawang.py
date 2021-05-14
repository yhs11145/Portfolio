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
ws=wb.Worksheets('컴마왕')

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
j=3

url=(['http://www.commawang.co.kr/skin/shop/basic/system_list_include_plist.php?group_no=&group_type=&cate1=&cate2=9270&game=&sprice=&eprice=&event_no=&pc_title=컴마왕스튜디오 월간추천견적&origin_ctgr1=&origin_ctgr2=&type=',
'http://www.commawang.co.kr/skin/shop/basic/system_list_include_plist.php?group_no=&group_type=&cate1=&cate2=9063&game=&sprice=&eprice=&event_no=&pc_title=20만원대 기본웹서핑용&origin_ctgr1=&origin_ctgr2=&type=',
'http://www.commawang.co.kr/skin/shop/basic/system_list_include_plist.php?group_no=&group_type=&cate1=&cate2=7823&game=&sprice=&eprice=&event_no=&pc_title=30만원대 사무용&origin_ctgr1=&origin_ctgr2=&type=',
'http://www.commawang.co.kr/skin/shop/basic/system_list_include_plist.php?group_no=&group_type=&cate1=&cate2=8726&game=&sprice=&eprice=&event_no=&pc_title=40만원대 기본게임용&origin_ctgr1=&origin_ctgr2=&type=',
'http://www.commawang.co.kr/skin/shop/basic/system_list_include_plist.php?group_no=&group_type=&cate1=&cate2=8727&game=&sprice=&eprice=&event_no=&pc_title=50만원대 하급게임용&origin_ctgr1=&origin_ctgr2=&type=',
'http://www.commawang.co.kr/skin/shop/basic/system_list_include_plist.php?group_no=&group_type=&cate1=&cate2=8613&game=&sprice=&eprice=&event_no=&pc_title=60만원대 중급게임용&origin_ctgr1=&origin_ctgr2=&type=',
'http://www.commawang.co.kr/skin/shop/basic/system_list_include_plist.php?group_no=&group_type=&cate1=&cate2=8831&game=&sprice=&eprice=&event_no=&pc_title=70만원대 상급게임용&origin_ctgr1=&origin_ctgr2=&type=',
'http://www.commawang.co.kr/skin/shop/basic/system_list_include_plist.php?group_no=&group_type=&cate1=&cate2=8832&game=&sprice=&eprice=&event_no=&pc_title=80만원대 고급게임용&origin_ctgr1=&origin_ctgr2=&type=',
'http://www.commawang.co.kr/skin/shop/basic/system_list_include_plist.php?group_no=&group_type=&cate1=&cate2=8081&game=&sprice=&eprice=&event_no=&pc_title=90만원대 최고급게임용&origin_ctgr1=&origin_ctgr2=&type=',
'http://www.commawang.co.kr/skin/shop/basic/system_list_include_plist.php?group_no=&group_type=&cate1=&cate2=8819&game=&sprice=&eprice=&event_no=&pc_title=100만원대 이상 전문가용&origin_ctgr1=&origin_ctgr2=&type=',
'http://www.commawang.co.kr/skin/shop/basic/system_list_include_plist.php?group_no=&group_type=&cate1=&cate2=9056&game=&sprice=&eprice=&event_no=&pc_title=150만원대 하이엔드 방송용&origin_ctgr1=&origin_ctgr2=&type=',
'http://www.commawang.co.kr/skin/shop/basic/system_list_include_plist.php?group_no=&group_type=&cate1=&cate2=9065&game=&sprice=&eprice=&event_no=&pc_title=250만원대 판타스틱 고사양&origin_ctgr1=&origin_ctgr2=&type=',
'http://www.commawang.co.kr/skin/shop/basic/system_list_include_plist.php?group_no=&group_type=&cate1=&cate2=8780&game=&sprice=&eprice=&event_no=&pc_title=오버클럭 PC&origin_ctgr1=&origin_ctgr2=&type=',
'http://www.commawang.co.kr/skin/shop/basic/system_list_include_plist.php?group_no=&group_type=&cate1=&cate2=9060&game=&sprice=&eprice=&event_no=&pc_title=일체형 수랭 PC&origin_ctgr1=&origin_ctgr2=&type=',
'http://www.commawang.co.kr/skin/shop/basic/system_list_include_plist.php?group_no=&group_type=&cate1=&cate2=9053&game=&sprice=&eprice=&event_no=&pc_title=커스텀 수냉 PC&origin_ctgr1=&origin_ctgr2=&type=',
'http://www.commawang.co.kr/skin/shop/basic/system_list_include_plist.php?group_no=&group_type=&cate1=&cate2=9205&game=&sprice=&eprice=&event_no=&pc_title=라이젠 3세대 PC&origin_ctgr1=&origin_ctgr2=&type=',
'http://www.commawang.co.kr/skin/shop/basic/system_list_include_plist.php?group_no=&group_type=&cate1=&cate2=9240&game=&sprice=&eprice=&event_no=&pc_title=인텔 10세대 PC&origin_ctgr1=&origin_ctgr2=&type=',
'http://www.commawang.co.kr/skin/shop/basic/system_list_include_plist.php?group_no=&group_type=&cate1=&cate2=8890&game=&sprice=&eprice=&event_no=&pc_title=윈도우10 탑재 PC&origin_ctgr1=&origin_ctgr2=&type=',
'http://www.commawang.co.kr/skin/shop/basic/system_list_include_plist.php?group_no=&group_type=&cate1=&cate2=8909&game=&sprice=&eprice=&event_no=&pc_title=모니터 본체 패키지&origin_ctgr1=&origin_ctgr2=&type=',
'http://www.commawang.co.kr/skin/shop/basic/system_list_include_plist.php?group_no=&group_type=&cate1=6573&cate2=8890&game=&sprice=700000&eprice=899999&event_no=&pc_title=70-80만원대 탑재PC&origin_ctgr1=9003&origin_ctgr2=9005&type=',
'http://www.commawang.co.kr/skin/shop/basic/system_list_include_plist.php?group_no=&group_type=&cate1=6573&cate2=8890&game=&sprice=900000&eprice=1099999&event_no=&pc_title=90-100만원대 탑재PC&origin_ctgr1=9003&origin_ctgr2=9006&type=',
'http://www.commawang.co.kr/skin/shop/basic/system_list_include_plist.php?group_no=&group_type=&cate1=6573&cate2=8890&game=&sprice=1100000&eprice=1499999&event_no=&pc_title=110-140만원대 탑재PC&origin_ctgr1=9003&origin_ctgr2=9007&type=',
'http://www.commawang.co.kr/skin/shop/basic/system_list_include_plist.php?group_no=&group_type=&cate1=6573&cate2=8890&game=&sprice=1500000&eprice=1999999&event_no=&pc_title=150-190만원대 탑재PC&origin_ctgr1=9003&origin_ctgr2=9207&type=',
'http://www.commawang.co.kr/skin/shop/basic/system_list_include_plist.php?group_no=&group_type=&cate1=6573&cate2=8890&game=&sprice=2000000&eprice=2147483647&event_no=&pc_title=200만원 이상 패키지&origin_ctgr1=9003&origin_ctgr2=9208&type=',
'http://www.commawang.co.kr/skin/shop/basic/system_list_include_plist.php?group_no=&group_type=&cate1=6573&cate2=8909&game=&sprice=800000&eprice=1099999&event_no=&pc_title=80-100만원대 패키지&origin_ctgr1=9010&origin_ctgr2=9013&type=',
'http://www.commawang.co.kr/skin/shop/basic/system_list_include_plist.php?group_no=&group_type=&cate1=6573&cate2=8909&game=&sprice=1100000&eprice=1399999&event_no=&pc_title=110-130만원대 패키지&origin_ctgr1=9010&origin_ctgr2=9014&type=',
'http://www.commawang.co.kr/skin/shop/basic/system_list_include_plist.php?group_no=&group_type=&cate1=6573&cate2=8909&game=&sprice=1400000&eprice=1999999&event_no=&pc_title=140-190만원대 패키지&origin_ctgr1=9010&origin_ctgr2=9015&type=',
'http://www.commawang.co.kr/skin/shop/basic/system_list_include_plist.php?group_no=&group_type=&cate1=6573&cate2=8909&game=&sprice=2000000&eprice=2147483647&event_no=&pc_title=200만원 이상 패키지&origin_ctgr1=9010&origin_ctgr2=9017&type='])

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
    for price in soup.select('tbody > tr > td > table:nth-child(3) > tbody > tr:nth-child(2) > td > a'):
        ws.Cells(i,2).Value=price.text.strip()
        i+=1
    i-=cnt
    for info in soup.select('tbody > tr > td > table:nth-child(2) > tbody > tr > td > span'):
        ws.Cells(i,j).Value=info.text.strip()
        j+=1
        if "스트리머" in info.text.strip():
            i+=1
            j=3
    cnt=0
