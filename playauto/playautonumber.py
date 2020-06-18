import sys,os,time
from selenium import webdriver
from bs4 import BeautifulSoup


def interparkb():
     html=driver.page_source
     soup=BeautifulSoup(html,'html.parser')
     for k in soup.select('div > treecontrol > ul > li:nth-child(2) > div'):
          print(k.text,end=' ')
     for i in range(2,3):
          for k in soup.select('div > treecontrol > ul > li:nth-child(2) > treeitem > ul > li:nth-child('+str(i)+') > div'):
               print(k.text,end=' ')
          driver.find_element_by_xpath('//*[@id="sidebar-tabs-5"]/div/div[1]/div/treecontrol/ul/li[2]/treeitem/ul/li['+str(i)+']/i[1]').click()
          for j in range(2,3):
               html=driver.page_source
               soup=BeautifulSoup(html,'html.parser')
               for k in soup.select('treecontrol > ul > li:nth-child(2) > treeitem > ul > li:nth-child('+str(i)+') > treeitem > ul > li:nth-child('+str(j)+') > div'):
                    print(k.text,end=' ')
                    
def auction():
     html=driver.page_source
     soup=BeautifulSoup(html,'html.parser')
     for k in soup.select('div > treecontrol > ul > li:nth-child(3) > div'):
          print(k.text,end=' ')
     for i in range(2,5):
          for k in soup.select('div > treecontrol > ul > li:nth-child(3) > treeitem > ul > li:nth-child('+str(i)+') > div'):
               print(k.text,end=' ')
          driver.find_element_by_xpath('//*[@id="sidebar-tabs-5"]/div/div[1]/div/treecontrol/ul/li[3]/treeitem/ul/li['+str(i)+']/i[1]').click()
          for j in range(2,3):
               html=driver.page_source
               soup=BeautifulSoup(html,'html.parser')
               for k in soup.select('treecontrol > ul > li:nth-child(3) > treeitem > ul > li:nth-child('+str(i)+') > treeitem > ul > li:nth-child('+str(j)+') > div'):
                    print(k.text,end=' ')

def gmarket():
     html=driver.page_source
     soup=BeautifulSoup(html,'html.parser')
     for k in soup.select('div > treecontrol > ul > li:nth-child(4) > div'):
          print(k.text,end=' ')
     for i in range(2,5):
          for k in soup.select('div > treecontrol > ul > li:nth-child(4) > treeitem > ul > li:nth-child('+str(i)+') > div'):
               print(k.text,end=' ')
          driver.find_element_by_xpath('//*[@id="sidebar-tabs-5"]/div/div[1]/div/treecontrol/ul/li[4]/treeitem/ul/li['+str(i)+']/i[1]').click()
          for j in range(2,3):
               html=driver.page_source
               soup=BeautifulSoup(html,'html.parser')
               for k in soup.select('treecontrol > ul > li:nth-child(4) > treeitem > ul > li:nth-child('+str(i)+') > treeitem > ul > li:nth-child('+str(j)+') > div'):
                    print(k.text,end=' ')

def interpark():
     html=driver.page_source
     soup=BeautifulSoup(html,'html.parser')
     for k in soup.select('div > treecontrol > ul > li:nth-child(5) > div'):
          print(k.text,end=' ')
     for i in range(2,4):
          for k in soup.select('div > treecontrol > ul > li:nth-child(5) > treeitem > ul > li:nth-child('+str(i)+') > div'):
               print(k.text,end=' ')
          driver.find_element_by_xpath('//*[@id="sidebar-tabs-5"]/div/div[1]/div/treecontrol/ul/li[5]/treeitem/ul/li['+str(i)+']/i[1]').click()
          for j in range(2,3):
               html=driver.page_source
               soup=BeautifulSoup(html,'html.parser')
               for k in soup.select('treecontrol > ul > li:nth-child(5) > treeitem > ul > li:nth-child('+str(i)+') > treeitem > ul > li:nth-child('+str(j)+') > div'):
                    print(k.text,end=' ')

def naver():
     html=driver.page_source
     soup=BeautifulSoup(html,'html.parser')
     for k in soup.select('div > treecontrol > ul > li:nth-child(6) > div'):
          print(k.text,end=' ')
     for i in range(2,5):
          for k in soup.select('div > treecontrol > ul > li:nth-child(6) > treeitem > ul > li:nth-child('+str(i)+') > div'):
               print(k.text,end=' ')
          driver.find_element_by_xpath('//*[@id="sidebar-tabs-5"]/div/div[1]/div/treecontrol/ul/li[6]/treeitem/ul/li['+str(i)+']/i[1]').click()
          for j in range(2,3):
               html=driver.page_source
               soup=BeautifulSoup(html,'html.parser')
               for k in soup.select('treecontrol > ul > li:nth-child(6) > treeitem > ul > li:nth-child('+str(i)+') > treeitem > ul > li:nth-child('+str(j)+') > div'):
                    print(k.text,end=' ')

def bun():
     html=driver.page_source
     soup=BeautifulSoup(html,'html.parser')
     for k in soup.select('div > treecontrol > ul > li:nth-child(7) > div'):
          print(k.text,end=' ')
     for i in range(2,5):
          for k in soup.select('div > treecontrol > ul > li:nth-child(7) > treeitem > ul > li:nth-child('+str(i)+') > div'):
               print(k.text,end=' ')
          driver.find_element_by_xpath('//*[@id="sidebar-tabs-5"]/div/div[1]/div/treecontrol/ul/li[7]/treeitem/ul/li['+str(i)+']/i[1]').click()
          for j in range(2,3):
               html=driver.page_source
               soup=BeautifulSoup(html,'html.parser')
               for k in soup.select('treecontrol > ul > li:nth-child(7) > treeitem > ul > li:nth-child('+str(i)+') > treeitem > ul > li:nth-child('+str(j)+') > div'):
                    print(k.text,end=' ')

def nhmarket():
     html=driver.page_source
     soup=BeautifulSoup(html,'html.parser')
     for k in soup.select('div > treecontrol > ul > li:nth-child(8) > div'):
          print(k.text,end=' ')
     for i in range(2,4):
          for k in soup.select('div > treecontrol > ul > li:nth-child(8) > treeitem > ul > li:nth-child('+str(i)+') > div'):
               print(k.text,end=' ')
          driver.find_element_by_xpath('//*[@id="sidebar-tabs-5"]/div/div[1]/div/treecontrol/ul/li[8]/treeitem/ul/li['+str(i)+']/i[1]').click()
          for j in range(2,3):
               html=driver.page_source
               soup=BeautifulSoup(html,'html.parser')
               for k in soup.select('treecontrol > ul > li:nth-child(8) > treeitem > ul > li:nth-child('+str(i)+') > treeitem > ul > li:nth-child('+str(j)+') > div'):
                    print(k.text,end=' ')

def we():
     html=driver.page_source
     soup=BeautifulSoup(html,'html.parser')
     for k in soup.select('div > treecontrol > ul > li:nth-child(9) > div'):
          print(k.text,end=' ')
     for i in range(2,3):
          for k in soup.select('div > treecontrol > ul > li:nth-child(9) > treeitem > ul > li:nth-child('+str(i)+') > div'):
               print(k.text,end=' ')
          driver.find_element_by_xpath('//*[@id="sidebar-tabs-5"]/div/div[1]/div/treecontrol/ul/li[9]/treeitem/ul/li['+str(i)+']/i[1]').click()
          for j in range(2,3):
               html=driver.page_source
               soup=BeautifulSoup(html,'html.parser')
               for k in soup.select('treecontrol > ul > li:nth-child(9) > treeitem > ul > li:nth-child('+str(i)+') > treeitem > ul > li:nth-child('+str(j)+') > div'):
                    print(k.text,end=' ')
     

if getattr(sys, 'frozen', False):
    Chrome_path = os.path.join(sys._MEIPASS, "ChromeDriver.exe")
    driver = webdriver.Chrome(Chrome_path)
else:
    driver=webdriver.Chrome()

id='sellallmaster@gmail.com'
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
         driver.find_element_by_xpath('//*[@id="online_prodlist_grid_searchbar"]/div/ul/li[2]/a').click()
         time.sleep(2)
         break
    except:
         driver.refresh()

interparkb()
print()
auction()
print()
gmarket()
print()
interpark()
print()
naver()
print()
bun()
print()
nhmarket()
print()
we()
