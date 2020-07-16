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
    

excel=win32com.client.Dispatch("Excel.Application")
excel.Visible=True
url=input("엑셀 파일 경로를 입력하세요. :")
wb=excel.workbooks.Open(url)
ws=wb.ActiveSheet
i=2
id="selling"
pw="claeo123"

driver.get("http://www.ssaul.co.kr/ssaul.html")
driver.find_element_by_id('ids').send_keys(id)
driver.find_element_by_id('pws').send_keys(pw)
driver.find_element_by_xpath('/html/body/div/div[1]/form/div/div/input').click()

while(1):
    j=23
    productname=ws.Cells(i,1).Value
    if productname is not None:
        try: 
            driver.find_element_by_xpath('//*[@id="header"]/div[1]/div/div[1]/div/div/form/input[1]').send_keys(productname)
            driver.find_element_by_xpath('//*[@id="header"]/div[1]/div/div[1]/div/div/form/input[2]').click()
            try:
                driver.find_element_by_xpath('//*[@id="pic"]').click()
                html=driver.page_source
                soup=BeautifulSoup(html,'html.parser')
                for option in soup.select('#detail > div > div.detailView_orderInfoBox > dl > strong > strong > table > tbody > tr > td.left'): ##옵션명
                    ws.Cells(i,j).Value=option.text
                    j+=1
                j=43
                for count in soup.select('#detail > div > div.detailView_orderInfoBox > dl > strong > strong > table > tbody > tr > td.right'):#3당일출고가능
                    ws.Cells(i,j).Value=count.text
                    j+=1
                j=63
                for order in soup.select('#detail > div > div.detailView_orderInfoBox > dl > strong > strong > table > tbody > tr > td.add'):##익일출고가능
                    ws.Cells(i,j).Value=order.text
                    j+=1
                i+=1
            except:
                ws.Cells(i,23).Value=str("상품이 없습니다.")
                i+=1
                pass
        except:
            driver.get('http://www.ssaul.co.kr/ssaul.html') ##서버 페이지 오류시 다시 접속
            ws.Cells(i,23).Value=str("상품명오류")
            i+=1
            driver.find_element_by_id('ids').send_keys(id)
            driver.find_element_by_id('pws').send_keys(pw)
            driver.find_element_by_xpath('/html/body/div/div[1]/form/div/div/input').click()
            pass
    else:
        break
    
driver.close()
sys.exit(0)
