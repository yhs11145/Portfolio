import sys,os,time
from selenium import webdriver
from bs4 import BeautifulSoup

if getattr(sys, 'frozen', False):
    Chrome_path = os.path.join(sys._MEIPASS, "ChromeDriver.exe")
    driver = webdriver.Chrome(Chrome_path)
else:
    driver=webdriver.Chrome()

id=input('아이디를 입력하세요: ')
pw=input('비밀번호를 입력하세요: ')
i=1

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
        driver.find_element_by_xpath('//*[@id="sidebar-tabs-5"]/div/div[1]/div/treecontrol/ul/li[6]/treeitem/ul/li[4]/i[1]').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="sidebar-tabs-5"]/div/div[1]/div/treecontrol/ul/li[6]/treeitem/ul/li[4]/treeitem/ul/li[8]/div').click()
        time.sleep(2)
        driver.find_element_by_xpath('/html/body/ui-view/div[2]/div/div[2]/div[3]/div/div/div/div[1]/ul/li[2]/a').click()
    except:
        print("retry")
        driver.refresh()
        continue
    while(1):
        try:
             time.sleep(2)
             driver.find_element_by_xpath('//*[@id="online_prodlist_grid_paginate"]/span/a['+str(i)+']').click()
             time.sleep(5)
             driver.find_element_by_xpath('//*[@id="select-slave"]').click()
             time.sleep(2)
             driver.find_element_by_xpath('/html/body/ui-view/div[2]/div/div[2]/div[3]/div/div/div/div[2]/div[1]/div[2]/div[10]/button').click()
             time.sleep(2)
             driver.find_element_by_xpath('//*[@id="prod_linkage_modify"]/div/div[3]/button[1]').click()
             i=i+1
             time.sleep(10)
             if i==11:
                 driver.find_element_by_xpath('//*[@id="online_prodlist_grid_next"]').click()
                 i=1
                 time.sleep(5)
        except:
            break
    html=driver.page_source
    soup=BeautifulSoup(html,'html.parser')
    for j in soup.select('div > ul.a-content-nav-tabs > li:nth-child(2) > a > span'):
        print(j.string)
        if int(j.string)>0:
            print("남아있다")
            driver.get('https://app.playauto.io/#!/home')
            i=1
            break
        else:
            sys.exit()
          
     
     



