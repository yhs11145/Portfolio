import sys,os,time
from selenium import webdriver
from bs4 import BeautifulSoup
import win32com.client

if getattr(sys, 'frozen', False):
    Chrome_path = os.path.join(sys._MEIPASS, "ChromeDriver.exe")
    driver = webdriver.Chrome(Chrome_path)
else:
    driver=webdriver.Chrome()


##아싸컴
page=0
i=2
j=1
excel=win32com.client.Dispatch("Excel.Application")
excel.Visible=True
wb=excel.workbooks.Open(os.getcwd()+'\price.xlsx')
ws=wb.Worksheets('아싸컴')
#wb=excel.workbooks.Add()
#ws=wb.WorkSheets("Sheet1")
link=[]

ws.Cells(1,1).Value="이름"
ws.Cells(1,3).Value="가격"
ws.Cells(1,4).Value="윈도우"
ws.Cells(1,5).Value="cpu"
ws.Cells(1,6).Value="RAM"
ws.Cells(1,7).Value="SSD"
ws.Cells(1,8).Value="GPU"

driver.get("https://www.assacom.com/shop/new_sub/all_product.htm?p=top")
time.sleep(2)
html=driver.page_source
soup=BeautifulSoup(html,'html.parser')
for div in soup.findAll('div',attrs={'class':'top_img'}): ##여기까지.
    link.append('https://www.assacom.com'+div.find('a')['href'])
while(1):
    driver.get(link[page])
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="ifodForm"]/div[2]/div[5]/div[1]/span[4]/a').click()
    time.sleep(2)
    html=driver.page_source
    soup=BeautifulSoup(html,'html.parser')
    for name in soup.select('#tb1 > div.es_copy_save > ul > li:nth-child(2)'):
        print(name.text.strip())
    for info in soup.select('table > tbody > tr > td.pro_name'):
        print(info.text.strip())
    if len(link)>=page:
        page+=4
    else:
        break


'''
 i=2
    j=1
    ws=wb.Worksheets('아싸컴')
    #wb=excel.workbooks.Add()
    #ws=wb.WorkSheets("Sheet1")

    ws.Cells(1,1).Value="이름"
    ws.Cells(1,3).Value="가격"
    ws.Cells(1,4).Value="윈도우"
    ws.Cells(1,5).Value="cpu"
    ws.Cells(1,6).Value="RAM"
    ws.Cells(1,7).Value="SSD"
    ws.Cells(1,8).Value="GPU"

    driver.get("https://www.assacom.com/shop/new_sub/all_product.htm?p=top")
    time.sleep(2)
    html=driver.page_source
    soup=BeautifulSoup(html,'html.parser')
    while(1):
        for name in soup.select('div.node_pro > p > a'):
            ws.cells(i,j).Value=name.text.strip()
            j+=1
            if j==4:
                i+=1
                j=1
        i=2
        j=4
        for k in range(2,7):
            for table in soup.select('tbody > tr:nth-child('+str(k)+') > td:nth-child(2) > a'):
                ws.cells(i,j).Value=table.text.strip()
                i+=1
            i=2
            j+=1
        break

    ws.save()

'''