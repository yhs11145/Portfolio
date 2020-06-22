from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys,os,time
import win32com.client

if getattr(sys, 'frozen', False):
    Chrome_path = os.path.join(sys._MEIPASS, "ChromeDriver.exe")
    driver = webdriver.Chrome(Chrome_path)
else:
    driver=webdriver.Chrome()

excelnumber=1
excel = win32com.client.Dispatch("Excel.Application")
excel.Visible = True
wb = excel.Workbooks.Add()
ws = wb.Worksheets("Sheet1")
ws.Cells(1,1).Value="상품명"
ws.Cells(1,2).Value="카테고리"
ws.Cells(1,3).Value="메인이미지"
ws.Cells(1,4).Value="소비자가격"
ws.Cells(1,5).Value="최종판매가"
ws.Cells(1,6).Value="도매가"
ws.Cells(1,7).Value="배송비"
ws.Cells(1,8).Value="제품코드"
ws.Cells(1,9).Value="브랜드"
ws.Cells(1,10).Value="원산지"
for i in range(11,21):
    ws.Cells(1,i).Value="상세이미지_"+str(excelnumber)
    excelnumber+=1
excelnumber=1
for i in range(21,41):
    ws.Cells(1,i).Value="옵션_"+str(excelnumber)
    excelnumber+=1
excelnumber=1
for i in range(41,91):
    ws.Cells(1,i).Value="상세정보_"+str(excelnumber)
    excelnumber+=1


id="selling"
pw="claeo123"
productnumber=1
pagenumber=5
e=2

driver.get("http://www.ssaul.co.kr/ssaul.html")
driver.find_element_by_id('ids').send_keys(id)
driver.find_element_by_id('pws').send_keys(pw)
driver.find_element_by_xpath('/html/body/div/div[1]/form/div/div/input').click()


search=int(input("1.카테고리 2.검색어"))

while(1):
    if search==1:
        html=driver.page_source
        soup=BeautifulSoup(html,'html.parser')
        for i in range(0,13):
            for category in soup.select('#m'+str(i)+' > a > span'):
                print(category.text.strip())
        print("---------------------------------")
        number1=int(input("대분류 카테고리 선택 : "))
        for category2 in soup.select('#_'+str(number1-1)+' > ul > li > a > span'):
            print(category2.text.strip())
        print("---------------------------------")
        number2=int(input("중분류 카테고리 선택 : "))
        for category3 in soup.select('#__'+str(number1-1)+' > li:nth-child('+str(number2)+') > ul > li > a > span'):
            print(category3.text.strip())
            selection=1
        for category3 in soup.select('#_'+str(number1-1)+' > ul > li:nth-child('+str(number2)+') > ul > li > a > span'):
            print(category3.text.strip())
            selection=2
        number3=int(input("소분류 카테고리 선택 : "))
        if selection==1:
            for category3 in soup.select('#__'+str(number1-1)+' > li:nth-child('+str(number2)+') > ul > li:nth-child('+str(number3)+') > a'):
                driver.get("http://ssaul.co.kr"+category3.get('href'))
        else:
            for category3 in soup.select('#_'+str(number1-1)+' > ul > li:nth-child('+str(number2)+') > ul > li:nth-child('+str(number3)+') > a'):
                driver.get("http://ssaul.co.kr"+category3.get('href'))
        break
    elif search==2:
        productname=input("검색어를 입력하세요")
        driver.find_element_by_xpath('//*[@id="header"]/div[1]/div/div[1]/div/div/form/input[1]').send_keys(productname)
        driver.find_element_by_xpath('//*[@id="header"]/div[1]/div/div[1]/div/div/form/input[2]').click()
        break
    else:
        print("잘못입력했어요. 다시입력하세요.")
        pass

while(1):
    j=11
    try:
        driver.find_element_by_xpath('//*[@id="specialTab01"]/ul/li['+str(productnumber)+']/a[2]').click()
    except:
        try:
            driver.find_element_by_xpath('//*[@id="specialListBox"]/div[3]/ul/li['+str(pagenumber)+']/a').click()
            pagenumber+=1
            productnumber=1
            driver.find_element_by_xpath('//*[@id="specialTab01"]/ul/li['+str(productnumber)+']/a[2]').click()
        except:
            break
    time.sleep(2)
    html=driver.page_source
    soup=BeautifulSoup(html,'html.parser')
    for name in soup.select('#detail > div > div.detailView_productName > p'):
        ws.Cells(e,1).Value=name.text.strip()
    for category in soup.select('#content > div.locations > span'):
        ws.Cells(e,2).Value=category.text.strip()
    for mainimage in soup.select('#detail > div > div.detailView_pic250 > img'):
        ws.Cells(e,3).Value='http://ssaul.co.kr/'+mainimage.get('src')
    for price in soup.select('#detail > div > div.detailView_orderInfoBox > dl > dd > strong > strong'):
        ws.Cells(e,4).Value=price.text.strip()
    for redprice in soup.select('#detail > div > div.detailView_orderInfoBox > dl > strong > strong > dd.fs16._red'):
        ws.Cells(e,5).Value=redprice.text.strip()##최종판매가
    for sellerprice in soup.select('#detail > div > div.detailView_orderInfoBox > dl > strong > strong > dd.BuSt.fs14'):
        ws.Cells(e,6).Value=sellerprice.text.strip()##도매가
    for delivery in soup.select('#detail > div > div.detailView_orderInfoBox > dl > strong > strong > dd:nth-child(7)'):
        ws.Cells(e,7).Value=delivery.text.strip()#배송비
    for code in soup.select('#detail > div > div.detailView_orderInfoBox > dl > strong > strong > dd:nth-child(9)'):
        ws.Cells(e,8).Value=code.text.strip()#제품코드
    for brand in soup.select('#detail > div > div.detailView_orderInfoBox > dl > strong > strong > dd:nth-child(11)'):
        ws.Cells(e,9).Value=brand.text.strip()#브랜드
    for made in soup.select('#detail > div > div.detailView_orderInfoBox > dl > strong > strong > dd.detailView_product_orderInfo_line.MB15'):
        ws.Cells(e,10).Value=made.text.strip()#원산지
    for redprice2 in soup.select('#detail > div > div.detailView_orderInfoBox > dl > strong > strong > dt.fs14._red'):
        ws.Cells(e,7).Value=code.text.strip()#배송비
        ws.Cells(e,8).Value=brand.text.strip()#코드
        for brand2 in soup.select('#detail > div > div.detailView_orderInfoBox > dl > strong > strong > dd:nth-child(13)'):
            ws.Cells(e,9).Value=brand2.text.strip()#코드
    for detailimage in soup.select('#content > strong > strong > div.pic780Wrap > div.detail_product_data > span > table > tbody > tr > td > img'):
        ws.Cells(e,j).Value='http://ssaul.co.kr/'+detailimage.get('src')
        j+=1
    for detailimage in soup.select('#content > strong > strong > div.pic780Wrap > div.detail_product_data > span > p > img'):
        ws.Cells(e,j).Value='http://ssaul.co.kr'+detailimage.get('src')
        j+=1
    j=21
    for option in soup.select('#detail > div > div.detailView_orderInfoBox > dl > strong > strong > table > tbody > tr > td.left'):
        ws.Cells(e,j).Value=option.text.strip()
        j+=1
    j=41
    for description in soup.select('#content > strong > strong > div.basicInfo7 > table > tbody > tr > td'):
        ws.Cells(e,j).Value=description.text.strip()
        j+=1
    e+=1
    productnumber+=1
    driver.execute_script("window.history.go(-1)")
    



