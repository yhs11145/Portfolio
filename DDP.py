import sys,os,time
from PyQt5 import QtCore, QtGui, QtWidgets
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import win32com.client

if getattr(sys, 'frozen', False):
    Chrome_path = os.path.join(sys._MEIPASS, "ChromeDriver.exe")
    driver = webdriver.Chrome(Chrome_path)
else:
    driver=webdriver.Chrome()


excel=win32com.client.Dispatch("Excel.Application")
excel.Visible=True
url=input("경로를 입력하세요")
wb=excel.workbooks.Open(url)
ws=wb.ActiveSheet

id='dorothy385'
pw='zlqhem12'

driver.get('http://dometopia.com/member/login')
driver.find_element_by_name("userid").send_keys(id)
driver.find_element_by_name("password").send_keys(pw)
driver.find_element_by_xpath('//*[@id="doto_login"]/div[3]/div[1]/form/div/input[3]').click()
time.sleep(5)

while True:
    try:
        driver.switch_to.window(driver.window_handles[1])
        driver.close()
    except:
        break

driver.switch_to.window(driver.window_handles[0])

for i in range(2,int(ws.Cells(1,1).Value)+2):
    number=ws.Cells(i,1).Value
    driver.get('http://dometopia.com/goods/search?search_text='+str(int(number)))
    html=driver.page_source
    soup=BeautifulSoup(html,'html.parser')
    for j in soup.select('table > tbody > tr > td > dl > dd > span > b'):
        ws.Cells(i,2).Value=j.string