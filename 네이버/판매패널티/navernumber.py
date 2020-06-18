import sys,os,time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import win32com.client

options=Options()
if getattr(sys, 'frozen', False):
    Chrome_path = os.path.join(sys._MEIPASS, "ChromeDriver.exe")
    notgood_path=os.path.join(sys._MEIPASS, "hdanmfijddamndfaabibmcafmnhhmebi.crx")
    options.add_extension(notgood_path)
    driver = webdriver.Chrome(Chrome_path,chrome_options=options)
else:
    options.add_extension('hdanmfijddamndfaabibmcafmnhhmebi.crx')
    driver=webdriver.Chrome(chrome_options=options)
    
excel=win32com.client.Dispatch("Excel.Application")
excel.Visible=True
wb = excel.Workbooks.Add()
ws = wb.Worksheets("Sheet1")

id="dorothymaster7@gmail.com"
pw="akdntmzlqhem1@"

while(1):
    try:
        driver.get('https://app.playauto.io/login.html')
        time.sleep(2)
        driver.find_element_by_name("email").send_keys(id)
        driver.find_element_by_name("password").send_keys(pw)
        driver.find_element_by_xpath('/html/body/div[3]/div/div/form/div/div[5]/div/button').click()
        time.sleep(5)
        break
    except:
        driver.find_element_by_xpath('/html/body/div[5]/div[7]/div/button').click()
        driver.refresh()
        break
j=1   
while(1):
    try:
        for i in range(13,26):
            time.sleep(2)
            driver.get('https://app.playauto.io/#!/online/product/list')
            driver.find_element_by_xpath('//*[@id="navbarHeight"]/div[1]/div[1]/ul/li[2]/a').click()
            driver.find_element_by_xpath('//*[@id="navbarHeight"]/div[1]/div[1]/ul/li[2]/ul/li['+str(i)+']/div[2]').click()
            time.sleep(2)
            driver.switch_to.window(driver.window_handles[1])
            time.sleep(5)
            try:
                driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/button/span').click()
            except:
                pass
            html=driver.page_source
            soup=BeautifulSoup(html,'html.parser')
            for name in soup.select('#seller-lnb > div > div:nth-child(1) > div.store > a > span.shop'):
                ws.Cells(j,1).Value=name.text.strip()
            for number1 in soup.select('#seller-content > ui-view > div > div.seller-sub-content > div > div.panel-wrap.flex-col-6.flex-col-md-12.order-md-10.order-xs-10 > div > div.panel-body.pd-mo-reset > div:nth-child(2) > ul > li:nth-child(1) > span.number-area > a:nth-child(1)'):
                ws.Cells(j,2).Value=number1.text.strip()      
            for number2 in soup.select('#seller-content > ui-view > div > div.seller-sub-content > div > div.panel-wrap.flex-col-6.flex-col-md-12.order-md-10.order-xs-10 > div > div.panel-body.pd-mo-reset > div:nth-child(2) > ul > li:nth-child(1) > span.number-area > a:nth-child(3)'):
                ws.Cells(j,3).Value=number2.text.strip()
            driver.close()
            driver.switch_to.window(driver.window_handles[0])
            j+=1          
            
        break
    except:
        driver.refresh()


    