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
ws=wb.Worksheets('프리플로우')
page=1

driver.get('http://www.hellopc.co.kr/src/category/?cate_menu=1&category=1')
time.sleep(2)
while(1):
    driver.find_element_by_xpath('//*[@id="limit"]/option[3]').click()
    time.sleep(2)
    while(1):
        i=1
        j=2
        html=driver.page_source
        soup=BeautifulSoup(html,'html.parser')
        time.sleep(2)
        for name in soup.select('#list_body > li:nth-child('+str(i)+') > div > a > dl > dt:nth-child(1) > span.clo_O'):
            ws.Cells(i,1).Value=name.text.strip()
            for info in soup.select('#list_body > li:nth-child('+str(i)+') > div > a > dl > dd'):
                ws.Cells(i,j).Value=info.text.strip()
                j+=1
            i+=1
            j=2
    page+=1
    if driver.find_element_by_xpath('//*[@id="pageLi"]').value==page:
        driver.find_element_by_css_selector('li#pageLi.next_page').click() 
    else:
        break






