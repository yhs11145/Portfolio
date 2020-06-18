import sys,os,time
from selenium import webdriver
from bs4 import BeautifulSoup
import win32com.client

excel=win32com.client.Dispatch("Excel.Application")
excel.Visible=True
wb=excel.Workbooks.Add()
ws=wb.Worksheets("Sheet1")

def interparkb():
     l=1
     m=3
     html=driver.page_source
     soup=BeautifulSoup(html,'html.parser')
     for k in soup.select('div > treecontrol > ul > li:nth-child(2) > div'):
          ws.Cells(l,1).Value=k.text
     for i in range(2,3):
          for k in soup.select('div > treecontrol > ul > li:nth-child(2) > treeitem > ul > li:nth-child('+str(i)+') > div'):
               ws.Cells(l,2).Value=k.text
          driver.find_element_by_xpath('//*[@id="sidebar-tabs-5"]/div/div[1]/div/treecontrol/ul/li[2]/treeitem/ul/li['+str(i)+']/i[1]').click()
          for j in range(1,4):
               html=driver.page_source
               soup=BeautifulSoup(html,'html.parser')
               for k in soup.select('treecontrol > ul > li:nth-child(2) > treeitem > ul > li:nth-child('+str(i)+') > treeitem > ul > li:nth-child('+str(j)+') > div'):
                    ws.Cells(l,m).Value=k.text
                    m+=1
          l+=1
          m=3
                    
def auction():
     l=2
     m=3
     html=driver.page_source
     soup=BeautifulSoup(html,'html.parser')
     for k in soup.select('div > treecontrol > ul > li:nth-child(3) > div'):
          ws.Cells(2,1).Value=k.text
     for i in range(2,6):
          for k in soup.select('div > treecontrol > ul > li:nth-child(3) > treeitem > ul > li:nth-child('+str(i)+') > div'):
               ws.Cells(l,2).Value=k.text
          driver.find_element_by_xpath('//*[@id="sidebar-tabs-5"]/div/div[1]/div/treecontrol/ul/li[3]/treeitem/ul/li['+str(i)+']/i[1]').click()
          for j in range(1,4):
               html=driver.page_source
               soup=BeautifulSoup(html,'html.parser')
               for k in soup.select('treecontrol > ul > li:nth-child(3) > treeitem > ul > li:nth-child('+str(i)+') > treeitem > ul > li:nth-child('+str(j)+') > div'):
                    ws.Cells(l,m).Value=k.text
                    m+=1
          l+=1
          m=3

def gmarket():
     l=6
     m=3
     html=driver.page_source
     soup=BeautifulSoup(html,'html.parser')
     for k in soup.select('div > treecontrol > ul > li:nth-child(4) > div'):
          ws.Cells(l,1).Value=k.text
     for i in range(2,6):
          for k in soup.select('div > treecontrol > ul > li:nth-child(4) > treeitem > ul > li:nth-child('+str(i)+') > div'):
               ws.Cells(l,2).Value=k.text
          driver.find_element_by_xpath('//*[@id="sidebar-tabs-5"]/div/div[1]/div/treecontrol/ul/li[4]/treeitem/ul/li['+str(i)+']/i[1]').click()
          for j in range(1,4):
               html=driver.page_source
               soup=BeautifulSoup(html,'html.parser')
               for k in soup.select('treecontrol > ul > li:nth-child(4) > treeitem > ul > li:nth-child('+str(i)+') > treeitem > ul > li:nth-child('+str(j)+') > div'):
                    ws.Cells(l,m).Value=k.text
                    m+=1
          l+=1
          m=3

def interpark():##10
     l=10
     m=3
     html=driver.page_source
     soup=BeautifulSoup(html,'html.parser')
     for k in soup.select('div > treecontrol > ul > li:nth-child(5) > div'):
          ws.Cells(l,1).Value=k.text
     for i in range(2,5):
          for k in soup.select('div > treecontrol > ul > li:nth-child(5) > treeitem > ul > li:nth-child('+str(i)+') > div'):
               ws.Cells(l,2).Value=k.text
          driver.find_element_by_xpath('//*[@id="sidebar-tabs-5"]/div/div[1]/div/treecontrol/ul/li[5]/treeitem/ul/li['+str(i)+']/i[1]').click()
          for j in range(1,4):
               html=driver.page_source
               soup=BeautifulSoup(html,'html.parser')
               for k in soup.select('treecontrol > ul > li:nth-child(5) > treeitem > ul > li:nth-child('+str(i)+') > treeitem > ul > li:nth-child('+str(j)+') > div'):
                    ws.Cells(l,m).Value=k.text
                    m+=1
          l+=1
          m=3

def naver():##13
     l=13
     m=3
     html=driver.page_source
     soup=BeautifulSoup(html,'html.parser')
     for k in soup.select('div > treecontrol > ul > li:nth-child(6) > div'):
          ws.Cells(l,1).Value=k.text
     for i in range(2,7):
          for k in soup.select('div > treecontrol > ul > li:nth-child(6) > treeitem > ul > li:nth-child('+str(i)+') > div'):
               ws.Cells(l,2).Value=k.text
          driver.find_element_by_xpath('//*[@id="sidebar-tabs-5"]/div/div[1]/div/treecontrol/ul/li[6]/treeitem/ul/li['+str(i)+']/i[1]').click()
          for j in range(1,4):
               html=driver.page_source
               soup=BeautifulSoup(html,'html.parser')
               for k in soup.select('treecontrol > ul > li:nth-child(6) > treeitem > ul > li:nth-child('+str(i)+') > treeitem > ul > li:nth-child('+str(j)+') > div'):
                    ws.Cells(l,m).Value=k.text
                    m+=1
          l+=1
          m=3

def bun():##18
     l=18
     m=3
     html=driver.page_source
     soup=BeautifulSoup(html,'html.parser')
     for k in soup.select('div > treecontrol > ul > li:nth-child(7) > div'):
          ws.Cells(l,1).Value=k.text
     for i in range(2,6):
          for k in soup.select('div > treecontrol > ul > li:nth-child(7) > treeitem > ul > li:nth-child('+str(i)+') > div'):
               ws.Cells(l,2).Value=k.text
          driver.find_element_by_xpath('//*[@id="sidebar-tabs-5"]/div/div[1]/div/treecontrol/ul/li[7]/treeitem/ul/li['+str(i)+']/i[1]').click()
          for j in range(1,4):
               html=driver.page_source
               soup=BeautifulSoup(html,'html.parser')
               for k in soup.select('treecontrol > ul > li:nth-child(7) > treeitem > ul > li:nth-child('+str(i)+') > treeitem > ul > li:nth-child('+str(j)+') > div'):
                    ws.Cells(l,m).Value=k.text
                    m+=1
          l+=1
          m=3
               
def coupang():##22
     l=22
     m=3
     html=driver.page_source
     soup=BeautifulSoup(html,'html.parser')
     for k in soup.select('div > treecontrol > ul > li:nth-child(8) > div'):
          ws.Cells(l,1).Value=k.text
     for i in range(2,3):
          for k in soup.select('div > treecontrol > ul > li:nth-child(8) > treeitem > ul > li:nth-child('+str(i)+') > div'):
               ws.Cells(l,2).Value=k.text
          driver.find_element_by_xpath('//*[@id="sidebar-tabs-5"]/div/div[1]/div/treecontrol/ul/li[8]/treeitem/ul/li['+str(i)+']/i[1]').click()
          for j in range(1,4):
               html=driver.page_source
               soup=BeautifulSoup(html,'html.parser')
               for k in soup.select('treecontrol > ul > li:nth-child(8) > treeitem > ul > li:nth-child('+str(i)+') > treeitem > ul > li:nth-child('+str(j)+') > div'):
                    ws.Cells(l,m).Value=k.text
                    m+=1
          l+=1
          m=3

def nhmarket():
     l=23
     m=3
     html=driver.page_source
     soup=BeautifulSoup(html,'html.parser')
     for k in soup.select('div > treecontrol > ul > li:nth-child(9) > div'):
          ws.Cells(l,1).Value=k.text
     for i in range(2,5):
          for k in soup.select('div > treecontrol > ul > li:nth-child(9) > treeitem > ul > li:nth-child('+str(i)+') > div'):
               ws.Cells(l,2).Value=k.text
          driver.find_element_by_xpath('//*[@id="sidebar-tabs-5"]/div/div[1]/div/treecontrol/ul/li[9]/treeitem/ul/li['+str(i)+']/i[1]').click()
          for j in range(1,4):
               html=driver.page_source
               soup=BeautifulSoup(html,'html.parser')
               for k in soup.select('treecontrol > ul > li:nth-child(9) > treeitem > ul > li:nth-child('+str(i)+') > treeitem > ul > li:nth-child('+str(j)+') > div'):
                    ws.Cells(l,m).Value=k.text
                    m+=1
          l+=1
          m=3

def kakao():
     l=26
     m=3
     html=driver.page_source
     soup=BeautifulSoup(html,'html.parser')
     for k in soup.select('div > treecontrol > ul > li:nth-child(10) > div'):
          ws.Cells(l,1).Value=k.text
     for i in range(2,3):
          for k in soup.select('div > treecontrol > ul > li:nth-child(10) > treeitem > ul > li:nth-child('+str(i)+') > div'):
               ws.Cells(l,2).Value=k.text
          driver.find_element_by_xpath('//*[@id="sidebar-tabs-5"]/div/div[1]/div/treecontrol/ul/li[10]/treeitem/ul/li['+str(i)+']/i[1]').click()
          for j in range(1,4):
               html=driver.page_source
               soup=BeautifulSoup(html,'html.parser')
               for k in soup.select('treecontrol > ul > li:nth-child(10) > treeitem > ul > li:nth-child('+str(i)+') > treeitem > ul > li:nth-child('+str(j)+') > div'):
                    ws.Cells(l,m).Value=k.text
                    m+=1
          l+=1
          m=3

def we():
     l=27
     m=3
     html=driver.page_source
     soup=BeautifulSoup(html,'html.parser')
     for k in soup.select('div > treecontrol > ul > li:nth-child(11) > div'):
          ws.Cells(l,1).Value=k.text
     for i in range(2,4):
          for k in soup.select('div > treecontrol > ul > li:nth-child(11) > treeitem > ul > li:nth-child('+str(i)+') > div'):
               ws.Cells(l,2).Value=k.text
          driver.find_element_by_xpath('//*[@id="sidebar-tabs-5"]/div/div[1]/div/treecontrol/ul/li[11]/treeitem/ul/li['+str(i)+']/i[1]').click()
          for j in range(1,4):
               html=driver.page_source
               soup=BeautifulSoup(html,'html.parser')
               for k in soup.select('treecontrol > ul > li:nth-child(11) > treeitem > ul > li:nth-child('+str(i)+') > treeitem > ul > li:nth-child('+str(j)+') > div'):
                    ws.Cells(l,m).Value=k.text
                    m+=1
          l+=1
          m=3

def timon():
     l=29
     m=3
     html=driver.page_source
     soup=BeautifulSoup(html,'html.parser')
     for k in soup.select('div > treecontrol > ul > li:nth-child(12) > div'):
          ws.Cells(l,1).Value=k.text
     for i in range(2,3):
          for k in soup.select('div > treecontrol > ul > li:nth-child(12) > treeitem > ul > li:nth-child('+str(i)+') > div'):
               ws.Cells(l,2).Value=k.text
          driver.find_element_by_xpath('//*[@id="sidebar-tabs-5"]/div/div[1]/div/treecontrol/ul/li[12]/treeitem/ul/li['+str(i)+']/i[1]').click()
          for j in range(1,4):
               html=driver.page_source
               soup=BeautifulSoup(html,'html.parser')
               for k in soup.select('treecontrol > ul > li:nth-child(12) > treeitem > ul > li:nth-child('+str(i)+') > treeitem > ul > li:nth-child('+str(j)+') > div'):
                    ws.Cells(l,m).Value=k.text
                    m+=1
          l+=1
          m=3
     

if getattr(sys, 'frozen', False):
    Chrome_path = os.path.join(sys._MEIPASS, "ChromeDriver.exe")
    driver = webdriver.Chrome(Chrome_path)
else:
    driver=webdriver.Chrome()

id='dolcevitamaster7@gmail.com'
pw='akdntmzlqhem1@'

driver.get('https://app.playauto.io/login.html')
time.sleep(2)
driver.find_element_by_name("email").send_keys(id)
driver.find_element_by_name("password").send_keys(pw)
driver.find_element_by_xpath('/html/body/div[3]/div/div/form/div/div[5]/div/button').click()
time.sleep(5)

while(1):
    driver.get('https://app.playauto.io/#!/online/product/list')
    time.sleep(5)
    try:
         driver.find_element_by_xpath('//*[@id="online_product_grid_searchbar"]/div/ul/li[2]/a').click()
         time.sleep(5)
         interparkb()
         auction()
         gmarket()
         interpark()
         naver()
         bun()
         coupang()
         nhmarket()
         kakao()
         we()
         timon()
         time.sleep(2)
         break
    except:
         driver.refresh()

