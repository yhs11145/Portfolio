import sys,os,time
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys

if getattr(sys, 'frozen', False):
    chrome_path = os.path.join(sys._MEIPASS, "chromedriver.exe")
    driver = webdriver.Chrome(chrome_path)
else:
    driver=webdriver.Chrome()

def aesmsale():
    id=input('옥션아이디를 입력하세요: ')
    pw=input('옥션비밀번호를 입력하세요: ')

    driver.get('http://www.esmplus.com/Home/Home#TDM396')
    driver.find_element_by_id("Id").send_keys(id)
    driver.find_element_by_id("Password").send_keys(pw)
    driver.find_element_by_xpath('//*[@id="btnLogOn"]/img').click()
    time.sleep(2)
    driver.get("http://www.esmplus.com/Sell/SingleGoodsMng?menuCode=TDM396")
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="divAcumlSum"]/table/tbody/tr[1]/td[3]/a').click()
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="selPageSize"]/option[7]').click()
    time.sleep(2)
    while(1):
        driver.find_element_by_xpath('//*[@id="gridcolumn-1014-textEl"]').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="goodsContents"]/div[1]/div[1]/div[1]/span[2]/a').click()
        time.sleep(2)
        driver.switch_to.window(driver.window_handles[1])
        driver.find_element_by_xpath('//*[@id="siteTypeIAC"]/input').click()
        driver.maximize_window()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="SellStateChangeStop"]').click()
        time.sleep(300)
        driver.switch_to.window(driver.window_handles[1])
        driver.find_element_by_xpath('//*[@id="popFooter"]/a/img').click()
        time.sleep(5)
        driver.switch_to.window(driver.window_handles[0])

def aesmstop():
    id=input('옥션아이디를 입력하세요: ')
    pw=input('옥션비밀번호를 입력하세요: ')

    driver.get('http://www.esmplus.com/Home/Home#TDM396')
    driver.find_element_by_id("Id").send_keys(id)
    driver.find_element_by_id("Password").send_keys(pw)
    driver.find_element_by_xpath('//*[@id="btnLogOn"]/img').click()
    time.sleep(2)
    driver.get("http://www.esmplus.com/Sell/SingleGoodsMng?menuCode=TDM396")
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="divAcumlSum"]/table/tbody/tr[1]/td[5]/a').click()
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="selPageSize"]/option[7]').click()
    time.sleep(2)
    while(1):
         driver.find_element_by_xpath('//*[@id="gridcolumn-1014-textEl"]').click()
         time.sleep(2)
         driver.find_element_by_xpath('//*[@id="goodsContents"]/div[1]/div[1]/div[1]/span[9]/a').click()
         time.sleep(2)
         driver.switch_to.window(driver.window_handles[1])
         driver.maximize_window()
         time.sleep(2)
         driver.find_element_by_xpath('//*[@id="aSave"]').click()
         driver.switch_to.alert.accept()
         time.sleep(2)
         driver.switch_to.window(driver.window_handles[1])
         time.sleep(300)
         driver.find_element_by_xpath('//*[@id="popFooter"]/a').click()
         time.sleep(5)
         driver.switch_to.window(driver.window_handles[0])
def gesmsale():
    id=input('g마켓아이디를 입력하세요: ')
    pw=input('g마켓비밀번호를 입력하세요: ')

    driver.get('http://www.esmplus.com/Home/Home#TDM396')
    driver.find_element_by_id("Id").send_keys(id)
    driver.find_element_by_id("Password").send_keys(pw)
    driver.find_element_by_xpath('//*[@id="btnLogOn"]/img').click()
    time.sleep(2)
    driver.get("http://www.esmplus.com/Sell/SingleGoodsMng?menuCode=TDM396")
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="divAcumlSum"]/table/tbody/tr[2]/td[3]/a').click()
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="selPageSize"]/option[7]').click()
    time.sleep(2)
    while(1):
        driver.find_element_by_xpath('//*[@id="gridcolumn-1014-textEl"]').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="goodsContents"]/div[1]/div[1]/div[1]/span[2]/a').click()
        time.sleep(2)
        driver.switch_to.window(driver.window_handles[1])
        driver.find_element_by_xpath('//*[@id="siteTypeGMKT"]/input').click()
        time.sleep(2)
        driver.maximize_window()
        driver.find_element_by_xpath('//*[@id="SellStateChangeStop"]').click()
        time.sleep(300)
        driver.switch_to.window(driver.window_handles[1])
        driver.find_element_by_xpath('//*[@id="popFooter"]/a/img').click()
        time.sleep(5)
        driver.switch_to.window(driver.window_handles[0])
def gesmstop():
    id=input('아이디를 입력하세요: ')
    pw=input('비밀번호를 입력하세요: ')

    driver.get('http://www.esmplus.com/Home/Home#TDM396')
    driver.find_element_by_id("Id").send_keys(id)
    driver.find_element_by_id("Password").send_keys(pw)
    driver.find_element_by_xpath('//*[@id="btnLogOn"]/img').click()
    time.sleep(2)
    driver.get("http://www.esmplus.com/Sell/SingleGoodsMng?menuCode=TDM396")
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="divAcumlSum"]/table/tbody/tr[2]/td[5]/a').click()
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="selPageSize"]/option[7]').click()
    time.sleep(2)
    while(1):
         driver.find_element_by_xpath('//*[@id="gridcolumn-1014-textEl"]').click()
         time.sleep(2)
         driver.find_element_by_xpath('//*[@id="goodsContents"]/div[1]/div[1]/div[1]/span[9]/a').click()
         time.sleep(2)
         driver.switch_to.window(driver.window_handles[1])
         driver.maximize_window()
         time.sleep(2)
         driver.find_element_by_xpath('//*[@id="aSave"]').click()
         driver.switch_to.alert.accept()
         time.sleep(2)
         driver.switch_to.window(driver.window_handles[1])
         time.sleep(300)
         driver.find_element_by_xpath('//*[@id="popFooter"]/a').click()
         time.sleep(5)
         driver.switch_to.window(driver.window_handles[0])
def auction():
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
            driver.find_element_by_xpath('//*[@id="sidebar-tabs-5"]/div/div[1]/div/treecontrol/ul/li[3]/treeitem/ul/li[4]/i[1]').click()
            time.sleep(2)
            driver.find_element_by_xpath('//*[@id="sidebar-tabs-5"]/div/div[1]/div/treecontrol/ul/li[3]/treeitem/ul/li[4]/treeitem/ul/li[1]/div').click()
            time.sleep(2)
            driver.find_element_by_xpath('/html/body/ui-view/div[2]/div/div[2]/div[3]/div/div/div/div[1]/ul/li[3]/a').click()
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
                driver.find_element_by_xpath('/html/body/ui-view/div[2]/div/div[2]/div[3]/div/div/div/div[2]/div[1]/div[2]/div[3]/button').click()
                time.sleep(2)
                driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[3]/div/div[2]/button[1]').click()
                i=i+1
                time.sleep(10)
                if i==11:
                    try:
                        driver.find_element_by_xpath('//*[@id="online_prodlist_grid_next"]').click()
                        i=1
                    except:
                        break
            except:
                break
        html=driver.page_source
        soup=BeautifulSoup(html,'html.parser')
        for j in soup.select('div > ul.a-content-nav-tabs > li:nth-child(3) > a > span'):
            print(j.string)
            if int(j.string)>0:
                print("남아있다")
                time.sleep(60)
                driver.get('https://app.playauto.io/#!/home')
                i=1
                break
            else:
                return True

def auctionsale():
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
            driver.find_element_by_xpath('//*[@id="sidebar-tabs-5"]/div/div[1]/div/treecontrol/ul/li[3]/treeitem/ul/li[4]/i[1]').click()
            time.sleep(2)
            driver.find_element_by_xpath('//*[@id="sidebar-tabs-5"]/div/div[1]/div/treecontrol/ul/li[3]/treeitem/ul/li[4]/treeitem/ul/li[2]/div').click()
            time.sleep(2)
            driver.find_element_by_xpath('/html/body/ui-view/div[2]/div/div[2]/div[3]/div/div/div/div[1]/ul/li[3]/a').click()
        except:
            print("에러")
            driver.refresh()
            time.sleep(5)
            continue
        while(1):
            try:
                time.sleep(5)
                driver.find_element_by_xpath('//*[@id="select-slave"]').click()
                time.sleep(2)
                driver.find_element_by_xpath('/html/body/ui-view/div[2]/div/div[2]/div[3]/div/div/div/div[2]/div[1]/div[2]/div[10]/button').click()
                time.sleep(2)
                driver.find_element_by_xpath('//*[@id="prod_linkage_modify"]/div/div[3]/button[1]').click()
                i=i+1
                time.sleep(10)
            except:
                break
        html=driver.page_source
        soup=BeautifulSoup(html,'html.parser')
        for j in soup.select('div > ul.a-content-nav-tabs > li:nth-child(3) > a > span'):
            print(j.string)
            if int(j.string)>0:
                print("남아있다")
                driver.get('https://app.playauto.io/#!/home')
                i=1
                break
            else:
                return True
            
def auctionsteady():
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
            driver.find_element_by_xpath('//*[@id="sidebar-tabs-5"]/div/div[1]/div/treecontrol/ul/li[3]/treeitem/ul/li[4]/i[1]').click()
            time.sleep(2)
            driver.find_element_by_xpath('//*[@id="sidebar-tabs-5"]/div/div[1]/div/treecontrol/ul/li[3]/treeitem/ul/li[4]/treeitem/ul/li[3]/div').click()
            time.sleep(2)
            driver.find_element_by_xpath('/html/body/ui-view/div[2]/div/div[2]/div[3]/div/div/div/div[1]/ul/li[3]/a').click()
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
                 driver.find_element_by_xpath('/html/body/ui-view/div[2]/div/div[2]/div[3]/div/div/div/div[2]/div[1]/div[2]/div[3]/button').click()
                 time.sleep(2)
                 driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[3]/div/div[2]/button[1]').click()
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
        for j in soup.select('div > ul.a-content-nav-tabs > li:nth-child(3) > a > span'):
            print(j.string)
            if int(j.string)>0:
                print("남아있다")
                driver.get('https://app.playauto.io/#!/home')
                i=1
                break
            else:
                return True

def gmarket():
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
            driver.find_element_by_xpath('//*[@id="sidebar-tabs-5"]/div/div[1]/div/treecontrol/ul/li[4]/treeitem/ul/li[4]/i[1]').click()
            time.sleep(2)
            driver.find_element_by_xpath('//*[@id="sidebar-tabs-5"]/div/div[1]/div/treecontrol/ul/li[4]/treeitem/ul/li[4]/treeitem/ul/li[1]/div').click()
            time.sleep(2)
            driver.find_element_by_xpath('/html/body/ui-view/div[2]/div/div[2]/div[3]/div/div/div/div[1]/ul/li[3]/a').click()
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
                driver.find_element_by_xpath('/html/body/ui-view/div[2]/div/div[2]/div[3]/div/div/div/div[2]/div[1]/div[2]/div[3]/button').click()
                time.sleep(2)
                driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[3]/div/div[2]/button[1]').click()
                i=i+1
                time.sleep(10)
                if i==11:
                    try:
                        driver.find_element_by_xpath('//*[@id="online_prodlist_grid_next"]').click()
                        i=1
                    except:
                        break
            except:
                break
        html=driver.page_source
        soup=BeautifulSoup(html,'html.parser')
        for j in soup.select('div > ul.a-content-nav-tabs > li:nth-child(3) > a > span'):
            print(j.string)
            if int(j.string)>0:
                print("남아있다")
                driver.get('https://app.playauto.io/#!/home')
                i=1
                break
            else:
                return True

def gmarketsale():
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
            driver.find_element_by_xpath('//*[@id="sidebar-tabs-5"]/div/div[1]/div/treecontrol/ul/li[4]/treeitem/ul/li[4]/i[1]').click()
            time.sleep(2)
            driver.find_element_by_xpath('//*[@id="sidebar-tabs-5"]/div/div[1]/div/treecontrol/ul/li[4]/treeitem/ul/li[4]/treeitem/ul/li[2]/div').click()
            time.sleep(2)
            driver.find_element_by_xpath('/html/body/ui-view/div[2]/div/div[2]/div[3]/div/div/div/div[1]/ul/li[3]/a').click()
        except:
            print("retry")
            driver.refresh()
            continue        
        while(1):
            try:
                time.sleep(5)
                driver.find_element_by_xpath('//*[@id="select-slave"]').click()
                time.sleep(2)
                driver.find_element_by_xpath('/html/body/ui-view/div[2]/div/div[2]/div[3]/div/div/div/div[2]/div[1]/div[2]/div[10]/button').click()
                time.sleep(2)
                driver.find_element_by_xpath('//*[@id="prod_linkage_modify"]/div/div[3]/button[1]').click()
                i=i+1
                time.sleep(10)
            except:
                break
        html=driver.page_source
        soup=BeautifulSoup(html,'html.parser')
        for j in soup.select('div > ul.a-content-nav-tabs > li:nth-child(3) > a > span'):
            print(j.string)
            if int(j.string)>0:
                print("남아있다")
                driver.get('https://app.playauto.io/#!/home')
                i=1
                break
            else:
                return True

def gmarketsteady():
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
            driver.find_element_by_xpath('//*[@id="sidebar-tabs-5"]/div/div[1]/div/treecontrol/ul/li[4]/treeitem/ul/li[4]/i[1]').click()
            time.sleep(2)
            driver.find_element_by_xpath('//*[@id="sidebar-tabs-5"]/div/div[1]/div/treecontrol/ul/li[4]/treeitem/ul/li[4]/treeitem/ul/li[3]/div').click()
            time.sleep(2)
            driver.find_element_by_xpath('/html/body/ui-view/div[2]/div/div[2]/div[3]/div/div/div/div[1]/ul/li[3]/a').click()
            break
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
                driver.find_element_by_xpath('/html/body/ui-view/div[2]/div/div[2]/div[3]/div/div/div/div[2]/div[1]/div[2]/div[3]/button').click()
                time.sleep(2)
                driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[3]/div/div[2]/button[1]').click()
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
        for j in soup.select('div > ul.a-content-nav-tabs > li:nth-child(3) > a > span'):
            print(j.string)
            if int(j.string)>0:
                print("남아있다")
                driver.get('https://app.playauto.io/#!/home')
                i=1
                break
            else:
                return True

def interpark():
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
            driver.find_element_by_xpath('//*[@id="sidebar-tabs-5"]/div/div[1]/div/treecontrol/ul/li[5]/treeitem/ul/li[3]/i[1]').click()
            time.sleep(2)
            driver.find_element_by_xpath('//*[@id="sidebar-tabs-5"]/div/div[1]/div/treecontrol/ul/li[5]/treeitem/ul/li[3]/treeitem/ul/li[1]/div').click()
            time.sleep(2)
            driver.find_element_by_xpath('/html/body/ui-view/div[2]/div/div[2]/div[3]/div/div/div/div[1]/ul/li[2]/a').click()
        except:
            print("판매탭에러")
            driver.refresh()
            continue
        while(1):
            try:
                time.sleep(2)
                driver.find_element_by_xpath('//*[@id="online_prodlist_grid_paginate"]/span/a['+str(i)+']').click()
                time.sleep(5)
                driver.find_element_by_xpath('//*[@id="select-slave"]').click()
                time.sleep(2)
                driver.find_element_by_xpath('/html/body/ui-view/div[2]/div/div[2]/div[3]/div/div/div/div[2]/div[1]/div[2]/div[3]/button').click()
                time.sleep(2)
                driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[3]/div/div[2]/button[1]').click()
                i=i+1
                time.sleep(10)
                if i==11:
                    try:
                        driver.find_element_by_xpath('//*[@id="online_prodlist_grid_next"]').click()
                        i=1
                    except:
                        break
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
                return True

def interparksale():
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
            driver.find_element_by_xpath('//*[@id="sidebar-tabs-5"]/div/div[1]/div/treecontrol/ul/li[5]/treeitem/ul/li[3]/i[1]').click()
            time.sleep(2)
            driver.find_element_by_xpath('//*[@id="sidebar-tabs-5"]/div/div[1]/div/treecontrol/ul/li[5]/treeitem/ul/li[3]/treeitem/ul/li[2]/div').click()
            time.sleep(2)
            driver.find_element_by_xpath('/html/body/ui-view/div[2]/div/div[2]/div[3]/div/div/div/div[1]/ul/li[2]/a').click()
        except:
            print("retry")
            driver.refresh()
            continue
        while(1):
            try:
                 time.sleep(5)
                 driver.find_element_by_xpath('//*[@id="select-slave"]').click()
                 time.sleep(2)
                 driver.find_element_by_xpath('/html/body/ui-view/div[2]/div/div[2]/div[3]/div/div/div/div[2]/div[1]/div[2]/div[10]/button').click()
                 time.sleep(2)
                 driver.find_element_by_xpath('//*[@id="prod_linkage_modify"]/div/div[3]/button[1]').click()
                 i=i+1
                 time.sleep(10)
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
                return True

def interparksteady():
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
            driver.find_element_by_xpath('//*[@id="sidebar-tabs-5"]/div/div[1]/div/treecontrol/ul/li[5]/treeitem/ul/li[3]/i[1]').click()
            time.sleep(2)
            driver.find_element_by_xpath('//*[@id="sidebar-tabs-5"]/div/div[1]/div/treecontrol/ul/li[5]/treeitem/ul/li[3]/treeitem/ul/li[3]/div').click()
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
                 driver.find_element_by_xpath('/html/body/ui-view/div[2]/div/div[2]/div[3]/div/div/div/div[2]/div[1]/div[2]/div[3]/button').click()
                 time.sleep(2)
                 driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[3]/div/div[2]/button[1]').click()
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
                return True

def naver():
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
            driver.find_element_by_xpath('//*[@id="sidebar-tabs-5"]/div/div[1]/div/treecontrol/ul/li[6]/treeitem/ul/li[4]/treeitem/ul/li[1]/div').click()
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
                driver.find_element_by_xpath('/html/body/ui-view/div[2]/div/div[2]/div[3]/div/div/div/div[2]/div[1]/div[2]/div[3]/button').click()
                time.sleep(2)
                driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[3]/div/div[2]/button[1]').click()
                i=i+1
                time.sleep(10)
                if i==11:
                    try:
                        driver.find_element_by_xpath('//*[@id="online_prodlist_grid_next"]').click()
                        i=1
                    except:
                        break
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
                return True

def naversale():
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
            driver.find_element_by_xpath('//*[@id="sidebar-tabs-5"]/div/div[1]/div/treecontrol/ul/li[6]/treeitem/ul/li[4]/treeitem/ul/li[2]/div').click()
            time.sleep(2)
            driver.find_element_by_xpath('/html/body/ui-view/div[2]/div/div[2]/div[3]/div/div/div/div[1]/ul/li[2]/a').click()
        except:
            print("retry")
            driver.refresh()
            continue
        while(1):
            try:
                 time.sleep(5)
                 driver.find_element_by_xpath('//*[@id="select-slave"]').click()
                 time.sleep(2)
                 driver.find_element_by_xpath('/html/body/ui-view/div[2]/div/div[2]/div[3]/div/div/div/div[2]/div[1]/div[2]/div[10]/button').click()
                 time.sleep(2)
                 driver.find_element_by_xpath('//*[@id="prod_linkage_modify"]/div/div[3]/button[1]').click()
                 i=i+1
                 time.sleep(10)
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
                return True

def naversteady():
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
            driver.find_element_by_xpath('//*[@id="sidebar-tabs-5"]/div/div[1]/div/treecontrol/ul/li[6]/treeitem/ul/li[4]/treeitem/ul/li[3]/div').click()
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
                 driver.find_element_by_xpath('/html/body/ui-view/div[2]/div/div[2]/div[3]/div/div/div/div[2]/div[1]/div[2]/div[3]/button').click()
                 time.sleep(2)
                 driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[3]/div/div[2]/button[1]').click()
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
                return True

def bun():
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
            driver.find_element_by_xpath('//*[@id="sidebar-tabs-5"]/div/div[1]/div/treecontrol/ul/li[7]/treeitem/ul/li[4]/i[1]').click()
            time.sleep(2)
            driver.find_element_by_xpath('//*[@id="sidebar-tabs-5"]/div/div[1]/div/treecontrol/ul/li[7]/treeitem/ul/li[4]/treeitem/ul/li[1]/div').click()
            time.sleep(2)
            driver.find_element_by_xpath('/html/body/ui-view/div[2]/div/div[2]/div[3]/div/div/div/div[1]/ul/li[3]/a').click()
        except:
            print("에러")
            driver.refresh()
            time.sleep(5)
            continue
        while(1):
            try:
                 time.sleep(2)
                 driver.find_element_by_xpath('//*[@id="online_prodlist_grid_paginate"]/span/a['+str(i)+']').click()
                 time.sleep(5)
                 driver.find_element_by_xpath('//*[@id="select-slave"]').click()
                 time.sleep(2)
                 driver.find_element_by_xpath('/html/body/ui-view/div[2]/div/div[2]/div[3]/div/div/div/div[2]/div[1]/div[2]/div[3]/button').click()
                 time.sleep(2)
                 driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[3]/div/div[2]/button[1]').click()
                 i=i+1
                 time.sleep(10)
                 if i==11:
                     try:
                         driver.find.element_by_xpath('//*[@id="online_prodlist_grid_next"]').click()
                         i=1
                     except:
                         break
            except:
                break
        html=driver.page_source
        soup=BeautifulSoup(html,'html.parser')
        for j in soup.select('div > ul.a-content-nav-tabs > li:nth-child(3) > a > span'):
            print(j.string)
            if int(j.string)>0:
                print("남아있다")
                driver.get('https://app.playauto.io/#!/home')
                i=1
                break
            else:
                return True

def bunsale():
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
            driver.find_element_by_xpath('//*[@id="sidebar-tabs-5"]/div/div[1]/div/treecontrol/ul/li[7]/treeitem/ul/li[4]/i[1]').click()
            time.sleep(2)
            driver.find_element_by_xpath('//*[@id="sidebar-tabs-5"]/div/div[1]/div/treecontrol/ul/li[7]/treeitem/ul/li[4]/treeitem/ul/li[2]/div').click()
            time.sleep(2)
            driver.find_element_by_xpath('/html/body/ui-view/div[2]/div/div[2]/div[3]/div/div/div/div[1]/ul/li[3]/a').click()
        except:
            print("에러")
            driver.refresh()
            continue  
        while(1):
            try:  
                 time.sleep(2)
                 driver.find_element_by_xpath('//*[@id="select-slave"]').click()
                 time.sleep(5)
                 driver.find_element_by_xpath('/html/body/ui-view/div[2]/div/div[2]/div[3]/div/div/div/div[2]/div[1]/div[2]/div[10]/button').click()
                 time.sleep(2)
                 driver.find_element_by_xpath('//*[@id="prod_linkage_modify"]/div/div[3]/button[1]').click()
                 i=i+1
                 time.sleep(10)
            except:
                break
        html=driver.page_source
        soup=BeautifulSoup(html,'html.parser')
        for j in soup.select('div > ul.a-content-nav-tabs > li:nth-child(3) > a > span'):
            print(j.string)
            if int(j.string)>0:
                print("남아있다")
                driver.get('https://app.playauto.io/#!/home')
                i=1
                break
            else:
                return True

def bunsteady():
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
            driver.find_element_by_xpath('//*[@id="sidebar-tabs-5"]/div/div[1]/div/treecontrol/ul/li[7]/treeitem/ul/li[4]/i[1]').click()
            time.sleep(2)
            driver.find_element_by_xpath('//*[@id="sidebar-tabs-5"]/div/div[1]/div/treecontrol/ul/li[7]/treeitem/ul/li[4]/treeitem/ul/li[3]/div').click()
            time.sleep(2)
            driver.find_element_by_xpath('/html/body/ui-view/div[2]/div/div[2]/div[3]/div/div/div/div[1]/ul/li[3]/a').click()
        except:
            print("에러")
            driver.refresh()
            time.sleep(5)
            continue   
        while(1):
            try:  
                 time.sleep(2)
                 driver.find_element_by_xpath('//*[@id="online_prodlist_grid_paginate"]/span/a['+str(i)+']').click()
                 time.sleep(5)
                 driver.find_element_by_xpath('//*[@id="select-slave"]').click()
                 time.sleep(2)
                 driver.find_element_by_xpath('/html/body/ui-view/div[2]/div/div[2]/div[3]/div/div/div/div[2]/div[1]/div[2]/div[3]/button').click()
                 time.sleep(2)
                 driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[3]/div/div[2]/button[1]').click()
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
        for j in soup.select('div > ul.a-content-nav-tabs > li:nth-child(3) > a > span'):
            print(j.string)
            if int(j.string)>0:
                print("남아있다")
                driver.get('https://app.playauto.io/#!/home')
                i=1
                break
            else:
                return True
def nh():
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
            driver.find_element_by_xpath('//*[@id="sidebar-tabs-5"]/div/div[1]/div/treecontrol/ul/li[8]/treeitem/ul/li[2]/i[1]').click()
            time.sleep(2)
            driver.find_element_by_xpath('//*[@id="sidebar-tabs-5"]/div/div[1]/div/treecontrol/ul/li[8]/treeitem/ul/li[2]/treeitem/ul/li[1]/div').click()
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
                driver.find_element_by_xpath('/html/body/ui-view/div[2]/div/div[2]/div[3]/div/div/div/div[2]/div[1]/div[2]/div[3]/button').click()
                time.sleep(2)
                driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[3]/div/div[2]/button[1]').click()
                i=i+1
                time.sleep(10)
                if i==11:
                    try:
                        driver.find_element_by_xpath('//*[@id="online_prodlist_grid_next"]').click()
                        i=1
                    except:
                        break
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
                return True

def nhsale():
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
            driver.find_element_by_xpath('//*[@id="sidebar-tabs-5"]/div/div[1]/div/treecontrol/ul/li[8]/treeitem/ul/li[2]/i[1]').click()
            time.sleep(2)
            driver.find_element_by_xpath('//*[@id="sidebar-tabs-5"]/div/div[1]/div/treecontrol/ul/li[8]/treeitem/ul/li[2]/treeitem/ul/li[2]/div').click()
            time.sleep(2)
            driver.find_element_by_xpath('/html/body/ui-view/div[2]/div/div[2]/div[3]/div/div/div/div[1]/ul/li[2]/a').click()
        except:
            print("retry")
            driver.refresh()
            continue
        while(1):
            try:
                 time.sleep(5)
                 driver.find_element_by_xpath('//*[@id="select-slave"]').click()
                 time.sleep(2)
                 driver.find_element_by_xpath('/html/body/ui-view/div[2]/div/div[2]/div[3]/div/div/div/div[2]/div[1]/div[2]/div[10]/button').click()
                 time.sleep(2)
                 driver.find_element_by_xpath('//*[@id="prod_linkage_modify"]/div/div[3]/button[1]').click()
                 i=i+1
                 time.sleep(10)
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
                return True

def nhsteady():
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
            driver.find_element_by_xpath('//*[@id="sidebar-tabs-5"]/div/div[1]/div/treecontrol/ul/li[8]/treeitem/ul/li[2]/i[1]').click()
            time.sleep(2)
            driver.find_element_by_xpath('//*[@id="sidebar-tabs-5"]/div/div[1]/div/treecontrol/ul/li[8]/treeitem/ul/li[2]/treeitem/ul/li[3]/div').click()
            time.sleep(2)
            driver.find_element_by_xpath('/html/body/ui-view/div[2]/div/div[2]/div[3]/div/div/div/div[1]/ul/li[2]/a').click()
        except:
            print("판매탭에러")
            driver.refresh()
            continue
        while(1):
            try:
                 time.sleep(2)
                 driver.find_element_by_xpath('//*[@id="online_prodlist_grid_paginate"]/span/a['+str(i)+']').click()
                 time.sleep(5)
                 driver.find_element_by_xpath('//*[@id="select-slave"]').click()
                 time.sleep(2)
                 driver.find_element_by_xpath('/html/body/ui-view/div[2]/div/div[2]/div[3]/div/div/div/div[2]/div[1]/div[2]/div[3]/button').click()
                 time.sleep(2)
                 driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[3]/div/div[2]/button[1]').click()
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
                return True


def auction2():
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
            driver.find_element_by_xpath('//*[@id="sidebar-tabs-5"]/div/div[1]/div/treecontrol/ul/li[8]/treeitem/ul/li[2]/i[1]').click()
            time.sleep(2)
            driver.find_element_by_xpath('//*[@id="sidebar-tabs-5"]/div/div[1]/div/treecontrol/ul/li[8]/treeitem/ul/li[2]/treeitem/ul/li[1]/div').click()
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
                driver.find_element_by_xpath('/html/body/ui-view/div[2]/div/div[2]/div[3]/div/div/div/div[2]/div[1]/div[2]/div[3]/button').click()
                time.sleep(2)
                driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[3]/div/div[2]/button[1]').click()
                i=i+1
                time.sleep(10)
                if i==11:
                    try:
                        driver.find_element_by_xpath('//*[@id="online_prodlist_grid_next"]').click()
                        i=1
                    except:
                        break
            except:
                break
        html=driver.page_source
        soup=BeautifulSoup(html,'html.parser')
        for j in soup.select('div > ul.a-content-nav-tabs > li:nth-child(3) > a > span'):
            print(j.string)
            if int(j.string)>0:
                print("남아있다")
                driver.get('https://app.playauto.io/#!/home')
                i=1
                break
            else:
                return True

def auctionsale2():
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
            driver.find_element_by_xpath('//*[@id="sidebar-tabs-5"]/div/div[1]/div/treecontrol/ul/li[3]/treeitem/ul/li[3]/i[1]').click()
            time.sleep(2)
            driver.find_element_by_xpath('//*[@id="sidebar-tabs-5"]/div/div[1]/div/treecontrol/ul/li[3]/treeitem/ul/li[3]/treeitem/ul/li[2]/div').click()
            time.sleep(2)
            driver.find_element_by_xpath('/html/body/ui-view/div[2]/div/div[2]/div[3]/div/div/div/div[1]/ul/li[3]/a').click()
        except:
            print("retry")
            driver.refresh()
            continue
        while(1):
            try:
                 time.sleep(5)
                 driver.find_element_by_xpath('//*[@id="select-slave"]').click()
                 time.sleep(2)
                 driver.find_element_by_xpath('/html/body/ui-view/div[2]/div/div[2]/div[3]/div/div/div/div[2]/div[1]/div[2]/div[10]/button').click()
                 time.sleep(2)
                 driver.find_element_by_xpath('//*[@id="prod_linkage_modify"]/div/div[3]/button[1]').click()
                 i=i+1
                 time.sleep(10)
            except:
                break
        html=driver.page_source
        soup=BeautifulSoup(html,'html.parser')
        for j in soup.select('div > ul.a-content-nav-tabs > li:nth-child(3) > a > span'):
            print(j.string)
            if int(j.string)>0:
                print("남아있다")
                driver.get('https://app.playauto.io/#!/home')
                i=1
                break
            else:
                return True

def auctionsteady2():
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
            driver.find_element_by_xpath('//*[@id="sidebar-tabs-5"]/div/div[1]/div/treecontrol/ul/li[3]/treeitem/ul/li[3]/i[1]').click()
            time.sleep(2)
            driver.find_element_by_xpath('//*[@id="sidebar-tabs-5"]/div/div[1]/div/treecontrol/ul/li[3]/treeitem/ul/li[3]/treeitem/ul/li[3]/div').click()
            time.sleep(2)
            driver.find_element_by_xpath('/html/body/ui-view/div[2]/div/div[2]/div[3]/div/div/div/div[1]/ul/li[3]/a').click()
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
                 driver.find_element_by_xpath('/html/body/ui-view/div[2]/div/div[2]/div[3]/div/div/div/div[2]/div[1]/div[2]/div[3]/button').click()
                 time.sleep(2)
                 driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[3]/div/div[2]/button[1]').click()
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
        for j in soup.select('div > ul.a-content-nav-tabs > li:nth-child(3) > a > span'):
            print(j.string)
            if int(j.string)>0:
                print("남아있다")
                driver.get('https://app.playauto.io/#!/home')
                i=1
                break
            else:
                return True

def gmarket2():
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
            driver.find_element_by_xpath('//*[@id="sidebar-tabs-5"]/div/div[1]/div/treecontrol/ul/li[4]/treeitem/ul/li[3]/i[1]').click()
            time.sleep(2)
            driver.find_element_by_xpath('//*[@id="sidebar-tabs-5"]/div/div[1]/div/treecontrol/ul/li[4]/treeitem/ul/li[3]/treeitem/ul/li[1]/div').click()
            time.sleep(2)
            driver.find_element_by_xpath('/html/body/ui-view/div[2]/div/div[2]/div[3]/div/div/div/div[1]/ul/li[3]/a').click()
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
                driver.find_element_by_xpath('/html/body/ui-view/div[2]/div/div[2]/div[3]/div/div/div/div[2]/div[1]/div[2]/div[3]/button').click()
                time.sleep(2)
                driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[3]/div/div[2]/button[1]').click()
                i=i+1
                time.sleep(10)
                if i==11:
                    try:
                        driver.find_element_by_xpath('//*[@id="online_prodlist_grid_next"]').click()
                        i=1
                    except:
                        break
            except:
                break
        html=driver.page_source
        soup=BeautifulSoup(html,'html.parser')
        for j in soup.select('div > ul.a-content-nav-tabs > li:nth-child(3) > a > span'):
            print(j.string)
            if int(j.string)>0:
                print("남아있다")
                driver.get('https://app.playauto.io/#!/home')
                i=1
                break
            else:
                return True

def gmarketsale2():
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
            driver.find_element_by_xpath('//*[@id="sidebar-tabs-5"]/div/div[1]/div/treecontrol/ul/li[4]/treeitem/ul/li[3]/i[1]').click()
            time.sleep(2)
            driver.find_element_by_xpath('//*[@id="sidebar-tabs-5"]/div/div[1]/div/treecontrol/ul/li[4]/treeitem/ul/li[3]/treeitem/ul/li[2]/div').click()
            time.sleep(2)
            driver.find_element_by_xpath('/html/body/ui-view/div[2]/div/div[2]/div[3]/div/div/div/div[1]/ul/li[3]/a').click()
        except:
            print("retry")
            driver.refresh()
            continue
        while(1):
            try:
                time.sleep(5)
                driver.find_element_by_xpath('//*[@id="select-slave"]').click()
                time.sleep(2)
                driver.find_element_by_xpath('/html/body/ui-view/div[2]/div/div[2]/div[3]/div/div/div/div[2]/div[1]/div[2]/div[10]/button').click()
                time.sleep(2)
                driver.find_element_by_xpath('//*[@id="prod_linkage_modify"]/div/div[3]/button[1]').click()
                i=i+1
                time.sleep(10)
            except:
                break
        html=driver.page_source
        soup=BeautifulSoup(html,'html.parser')
        for j in soup.select('div > ul.a-content-nav-tabs > li:nth-child(3) > a > span'):
            print(j.string)
            if int(j.string)>0:
                print("남아있다")
                driver.get('https://app.playauto.io/#!/home')
                i=1
                break
            else:
                return True

def gmarketsteady2():
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
            driver.find_element_by_xpath('//*[@id="sidebar-tabs-5"]/div/div[1]/div/treecontrol/ul/li[4]/treeitem/ul/li[3]/i[1]').click()
            time.sleep(2)
            driver.find_element_by_xpath('//*[@id="sidebar-tabs-5"]/div/div[1]/div/treecontrol/ul/li[4]/treeitem/ul/li[3]/treeitem/ul/li[3]/div').click()
            time.sleep(2)
            driver.find_element_by_xpath('/html/body/ui-view/div[2]/div/div[2]/div[3]/div/div/div/div[1]/ul/li[3]/a').click()
        except:
            print("판매탭에러")
            driver.refresh()
            continue
        while(1):
            try:
                time.sleep(2)
                driver.find_element_by_xpath('//*[@id="online_prodlist_grid_paginate"]/span/a['+str(i)+']').click()
                time.sleep(5)
                driver.find_element_by_xpath('//*[@id="select-slave"]').click()
                time.sleep(2)
                driver.find_element_by_xpath('/html/body/ui-view/div[2]/div/div[2]/div[3]/div/div/div/div[2]/div[1]/div[2]/div[3]/button').click()
                time.sleep(2)
                driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[3]/div/div[2]/button[1]').click()
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
        for j in soup.select('div > ul.a-content-nav-tabs > li:nth-child(3) > a > span'):
            print(j.string)
            if int(j.string)>0:
                print("남아있다")
                driver.get('https://app.playauto.io/#!/home')
                i=1
                break
            else:
                return True

def interpark2():
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
            driver.find_element_by_xpath('//*[@id="sidebar-tabs-5"]/div/div[1]/div/treecontrol/ul/li[5]/treeitem/ul/li[2]/i[1]').click()
            time.sleep(2)
            driver.find_element_by_xpath('//*[@id="sidebar-tabs-5"]/div/div[1]/div/treecontrol/ul/li[5]/treeitem/ul/li[2]/treeitem/ul/li[1]/div').click()
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
                driver.find_element_by_xpath('/html/body/ui-view/div[2]/div/div[2]/div[3]/div/div/div/div[2]/div[1]/div[2]/div[3]/button').click()
                time.sleep(2)
                driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[3]/div/div[2]/button[1]').click()
                i=i+1
                time.sleep(10)
                if i==11:
                    try:
                        driver.find_element_by_xpath('//*[@id="online_prodlist_grid_next"]').click()
                        i=1
                    except:
                        break
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
                return True

def interparksale2():
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
            driver.find_element_by_xpath('//*[@id="sidebar-tabs-5"]/div/div[1]/div/treecontrol/ul/li[5]/treeitem/ul/li[2]/i[1]').click()
            time.sleep(2)
            driver.find_element_by_xpath('//*[@id="sidebar-tabs-5"]/div/div[1]/div/treecontrol/ul/li[5]/treeitem/ul/li[2]/treeitem/ul/li[2]/div').click()
            time.sleep(2)
            driver.find_element_by_xpath('/html/body/ui-view/div[2]/div/div[2]/div[3]/div/div/div/div[1]/ul/li[2]/a').click()
        except:
            print("판매탭에러")
            driver.refresh()
            continue
        while(1):
            try:
                 time.sleep(5)
                 driver.find_element_by_xpath('//*[@id="select-slave"]').click()
                 time.sleep(2)
                 driver.find_element_by_xpath('/html/body/ui-view/div[2]/div/div[2]/div[3]/div/div/div/div[2]/div[1]/div[2]/div[10]/button').click()
                 time.sleep(2)
                 driver.find_element_by_xpath('//*[@id="prod_linkage_modify"]/div/div[3]/button[1]').click()
                 i=i+1
                 time.sleep(10)
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
                return True

def interparksteady2():
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
            driver.find_element_by_xpath('//*[@id="sidebar-tabs-5"]/div/div[1]/div/treecontrol/ul/li[5]/treeitem/ul/li[2]/i[1]').click()
            time.sleep(2)
            driver.find_element_by_xpath('//*[@id="sidebar-tabs-5"]/div/div[1]/div/treecontrol/ul/li[5]/treeitem/ul/li[2]/treeitem/ul/li[3]/div').click()
            time.sleep(2)
            driver.find_element_by_xpath('/html/body/ui-view/div[2]/div/div[2]/div[3]/div/div/div/div[1]/ul/li[2]/a').click()
        except:
            print("판매탭에러")
            driver.refresh()
            continue
        while(1):
            try:
                 time.sleep(2)
                 driver.find_element_by_xpath('//*[@id="online_prodlist_grid_paginate"]/span/a['+str(i)+']').click()
                 time.sleep(5)
                 driver.find_element_by_xpath('//*[@id="select-slave"]').click()
                 time.sleep(2)
                 driver.find_element_by_xpath('/html/body/ui-view/div[2]/div/div[2]/div[3]/div/div/div/div[2]/div[1]/div[2]/div[3]/button').click()
                 time.sleep(2)
                 driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[3]/div/div[2]/button[1]').click()
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
                return True

def naver2():
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
            driver.find_element_by_xpath('//*[@id="sidebar-tabs-5"]/div/div[1]/div/treecontrol/ul/li[6]/treeitem/ul/li[3]/i[1]').click()
            time.sleep(2)
            driver.find_element_by_xpath('//*[@id="sidebar-tabs-5"]/div/div[1]/div/treecontrol/ul/li[6]/treeitem/ul/li[3]/treeitem/ul/li[1]/div').click()
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
                driver.find_element_by_xpath('/html/body/ui-view/div[2]/div/div[2]/div[3]/div/div/div/div[2]/div[1]/div[2]/div[3]/button').click()
                time.sleep(2)
                driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[3]/div/div[2]/button[1]').click()
                i=i+1
                time.sleep(10)
                if i==11:
                    try:
                        driver.find_element_by_xpath('//*[@id="online_prodlist_grid_next"]').click()
                        i=1
                    except:
                        break
            except:
                break
        html=driver.page_source
        soup=BeautifulSoup(html,'html.parser')
        for j in soup.select('div > ul.a-content-nav-tabs > li:nth-child(2) > a > span'):
            print(j.string)
            if int(j.string)>0:
                print("남아있다")
                i=1
                driver.get('https://app.playauto.io/#!/home')
                i=1
                break
            else:
                return True

def naversale2():
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
            driver.find_element_by_xpath('//*[@id="sidebar-tabs-5"]/div/div[1]/div/treecontrol/ul/li[6]/treeitem/ul/li[3]/i[1]').click()
            time.sleep(2)
            driver.find_element_by_xpath('//*[@id="sidebar-tabs-5"]/div/div[1]/div/treecontrol/ul/li[6]/treeitem/ul/li[3]/treeitem/ul/li[2]/div').click()
            time.sleep(2)
            driver.find_element_by_xpath('/html/body/ui-view/div[2]/div/div[2]/div[3]/div/div/div/div[1]/ul/li[2]/a').click()
        except:
            print("판매탭에러")
            driver.refresh()
            continue
        while(1):
            try:
                 time.sleep(5)
                 driver.find_element_by_xpath('//*[@id="select-slave"]').click()
                 time.sleep(2)
                 driver.find_element_by_xpath('/html/body/ui-view/div[2]/div/div[2]/div[3]/div/div/div/div[2]/div[1]/div[2]/div[10]/button').click()
                 time.sleep(2)
                 driver.find_element_by_xpath('//*[@id="prod_linkage_modify"]/div/div[3]/button[1]').click()
                 i=i+1
                 time.sleep(10)
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
                return True
def naversteady2():
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
            driver.find_element_by_xpath('//*[@id="sidebar-tabs-5"]/div/div[1]/div/treecontrol/ul/li[6]/treeitem/ul/li[3]/i[1]').click()
            time.sleep(2)
            driver.find_element_by_xpath('//*[@id="sidebar-tabs-5"]/div/div[1]/div/treecontrol/ul/li[6]/treeitem/ul/li[3]/treeitem/ul/li[3]/div').click()
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
                 driver.find_element_by_xpath('/html/body/ui-view/div[2]/div/div[2]/div[3]/div/div/div/div[2]/div[1]/div[2]/div[3]/button').click()
                 time.sleep(2)
                 driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[3]/div/div[2]/button[1]').click()
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
                return True

def bun2():
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
            driver.find_element_by_xpath('//*[@id="sidebar-tabs-5"]/div/div[1]/div/treecontrol/ul/li[7]/treeitem/ul/li[3]/i[1]').click()
            time.sleep(2)
            driver.find_element_by_xpath('//*[@id="sidebar-tabs-5"]/div/div[1]/div/treecontrol/ul/li[7]/treeitem/ul/li[3]/treeitem/ul/li[1]/div').click()
            time.sleep(2)
            driver.find_element_by_xpath('/html/body/ui-view/div[2]/div/div[2]/div[3]/div/div/div/div[1]/ul/li[3]/a').click()
        except:
            print("에러")
            driver.refresh()
            continue
        while(1):
            try:
                 time.sleep(2)
                 driver.find_element_by_xpath('//*[@id="online_prodlist_grid_paginate"]/span/a['+str(i)+']').click()
                 time.sleep(5)
                 driver.find_element_by_xpath('//*[@id="select-slave"]').click()
                 time.sleep(2)
                 driver.find_element_by_xpath('/html/body/ui-view/div[2]/div/div[2]/div[3]/div/div/div/div[2]/div[1]/div[2]/div[3]/button').click()
                 time.sleep(2)
                 driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[3]/div/div[2]/button[1]').click()
                 i=i+1
                 time.sleep(10)
                 if i==11:
                     try:
                         driver.find.element_by_xpath('//*[@id="online_prodlist_grid_next"]').click()
                         i=1
                     except:
                         break
            except:
                break
        html=driver.page_source
        soup=BeautifulSoup(html,'html.parser')
        for j in soup.select('div > ul.a-content-nav-tabs > li:nth-child(3) > a > span'):
            print(j.string)
            if int(j.string)>0:
                print("남아있다")
                driver.get('https://app.playauto.io/#!/home')
                i=1
                break
            else:
                return True

def bunsale2():
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
            driver.find_element_by_xpath('//*[@id="sidebar-tabs-5"]/div/div[1]/div/treecontrol/ul/li[7]/treeitem/ul/li[3]/i[1]').click()
            time.sleep(2)
            driver.find_element_by_xpath('//*[@id="sidebar-tabs-5"]/div/div[1]/div/treecontrol/ul/li[7]/treeitem/ul/li[3]/treeitem/ul/li[2]/div').click()
            time.sleep(2)
            driver.find_element_by_xpath('/html/body/ui-view/div[2]/div/div[2]/div[3]/div/div/div/div[1]/ul/li[3]/a').click()
        except:
            print("판매탭에러")
            driver.refresh()
            continue
        while(1):
            try:  
                 time.sleep(2)
                 driver.find_element_by_xpath('//*[@id="select-slave"]').click()
                 time.sleep(5)
                 driver.find_element_by_xpath('/html/body/ui-view/div[2]/div/div[2]/div[4]/div/div/div/div[2]/div[1]/div[2]/div[10]/button').click()
                 time.sleep(2)
                 driver.find_element_by_xpath('//*[@id="prod_linkage_modify"]/div/div[3]/button[1]').click()
                 i=i+1
                 time.sleep(10)
            except:
                break
        html=driver.page_source
        soup=BeautifulSoup(html,'html.parser')
        for j in soup.select('div > ul.a-content-nav-tabs > li:nth-child(3) > a > span'):
            print(j.string)
            if int(j.string)>0:
                print("남아있다")
                driver.get('https://app.playauto.io/#!/home')
                i=1
                break
            else:
                return True

def bunsteady2():
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
            driver.find_element_by_xpath('//*[@id="sidebar-tabs-5"]/div/div[1]/div/treecontrol/ul/li[7]/treeitem/ul/li[3]/i[1]').click()
            time.sleep(2)
            driver.find_element_by_xpath('//*[@id="sidebar-tabs-5"]/div/div[1]/div/treecontrol/ul/li[7]/treeitem/ul/li[3]/treeitem/ul/li[3]/div').click()
            time.sleep(2)
            driver.find_element_by_xpath('/html/body/ui-view/div[2]/div/div[2]/div[3]/div/div/div/div[1]/ul/li[3]/a').click()
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
                 driver.find_element_by_xpath('/html/body/ui-view/div[2]/div/div[2]/div[3]/div/div/div/div[2]/div[1]/div[2]/div[3]/button').click()
                 time.sleep(2)
                 driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[3]/div/div[2]/button[1]').click()
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
        for j in soup.select('div > ul.a-content-nav-tabs > li:nth-child(3) > a > span'):
            print(j.string)
            if int(j.string)>0:
                print("남아있다")
                driver.get('https://app.playauto.io/#!/home')
                i=1
                break
            else:
                return True

def nh2():
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
            driver.find_element_by_xpath('//*[@id="sidebar-tabs-5"]/div/div[1]/div/treecontrol/ul/li[8]/treeitem/ul/li[3]/i[1]').click()
            time.sleep(2)
            driver.find_element_by_xpath('//*[@id="sidebar-tabs-5"]/div/div[1]/div/treecontrol/ul/li[8]/treeitem/ul/li[3]/treeitem/ul/li[1]/div').click()
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
                driver.find_element_by_xpath('/html/body/ui-view/div[2]/div/div[2]/div[3]/div/div/div/div[2]/div[1]/div[2]/div[3]/button').click()
                time.sleep(2)
                driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[3]/div/div[2]/button[1]').click()
                i=i+1
                time.sleep(10)
                if i==11:
                    try:
                        driver.find_element_by_xpath('//*[@id="online_prodlist_grid_next"]').click()
                        i=1
                    except:
                        break
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
                return True

def nhsale2():
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
            driver.find_element_by_xpath('//*[@id="sidebar-tabs-5"]/div/div[1]/div/treecontrol/ul/li[8]/treeitem/ul/li[3]/i[1]').click()
            time.sleep(2)
            driver.find_element_by_xpath('//*[@id="sidebar-tabs-5"]/div/div[1]/div/treecontrol/ul/li[8]/treeitem/ul/li[3]/treeitem/ul/li[2]/div').click()
            time.sleep(2)
            driver.find_element_by_xpath('/html/body/ui-view/div[2]/div/div[2]/div[3]/div/div/div/div[1]/ul/li[2]/a').click()
        except:
            print("판매탭에러")
            driver.refresh()
            continue
        while(1):
            try:
                 time.sleep(5)
                 driver.find_element_by_xpath('//*[@id="select-slave"]').click()
                 time.sleep(2)
                 driver.find_element_by_xpath('/html/body/ui-view/div[2]/div/div[2]/div[3]/div/div/div/div[2]/div[1]/div[2]/div[10]/button').click()
                 time.sleep(2)
                 driver.find_element_by_xpath('//*[@id="prod_linkage_modify"]/div/div[3]/button[1]').click()
                 i=i+1
                 time.sleep(10)
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
                return True

def nhsteady2():
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
            driver.find_element_by_xpath('//*[@id="sidebar-tabs-5"]/div/div[1]/div/treecontrol/ul/li[8]/treeitem/ul/li[3]/i[1]').click()
            time.sleep(2)
            driver.find_element_by_xpath('//*[@id="sidebar-tabs-5"]/div/div[1]/div/treecontrol/ul/li[8]/treeitem/ul/li[3]/treeitem/ul/li[3]/div').click()
            time.sleep(2)
            driver.find_element_by_xpath('/html/body/ui-view/div[2]/div/div[2]/div[3]/div/div/div/div[1]/ul/li[2]/a').click()
        except:
            print("판매탭에러")
            driver.refresh()
            continue
        while(1):
            try:
                 time.sleep(2)
                 driver.find_element_by_xpath('//*[@id="online_prodlist_grid_paginate"]/span/a['+str(i)+']').click()
                 time.sleep(5)
                 driver.find_element_by_xpath('//*[@id="select-slave"]').click()
                 time.sleep(2)
                 driver.find_element_by_xpath('/html/body/ui-view/div[2]/div/div[2]/div[3]/div/div/div/div[2]/div[1]/div[2]/div[3]/button').click()
                 time.sleep(2)
                 driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[3]/div/div[2]/button[1]').click()
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
                return True

def allsteady():
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
            driver.find_element_by_xpath('//*[@id="sidebar-tabs-5"]/div/div[1]/div/treecontrol/ul/li[1]/treeitem/ul/li[3]/div').click()
            time.sleep(2)
            driver.find_element_by_xpath('/html/body/ui-view/div[2]/div/div[2]/div[3]/div/div/div/div[1]/ul/li[3]/a').click()
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
                 driver.find_element_by_xpath('/html/body/ui-view/div[2]/div/div[2]/div[3]/div/div/div/div[2]/div[1]/div[2]/div[3]/button').click()
                 time.sleep(2)
                 driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[3]/div/div[2]/button[1]').click()
                 i=i+1
                 time.sleep(20)
                 if i==11:
                     driver.find_element_by_xpath('//*[@id="online_prodlist_grid_next"]').click()
                     i=1
                     time.sleep(5)
            except:
                break
        html=driver.page_source
        soup=BeautifulSoup(html,'html.parser')
        for j in soup.select('div > ul.a-content-nav-tabs > li:nth-child(3) > a > span'):
            print(j.string)
            if int(j.string)>0:
                print("남아있다")
                driver.get('https://app.playauto.io/#!/home')
                i=1
                break
            else:
                return allsteady2()

def allsteady2():
    i=1

    while(1):
        driver.get('https://app.playauto.io/#!/online/product/list')
        time.sleep(5)
        try:
            driver.find_element_by_xpath('//*[@id="online_prodlist_grid_searchbar"]/div/ul/li[2]/a').click()
            time.sleep(2)
            driver.find_element_by_xpath('//*[@id="sidebar-tabs-5"]/div/div[1]/div/treecontrol/ul/li[1]/treeitem/ul/li[3]/div').click()
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
                 driver.find_element_by_xpath('/html/body/ui-view/div[2]/div/div[2]/div[3]/div/div/div/div[2]/div[1]/div[2]/div[3]/button').click()
                 time.sleep(2)
                 driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[3]/div/div[2]/button[1]').click()
                 i=i+1
                 time.sleep(20)
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
                return True

if __name__ == '__main__':
    while True:
        id=input("아이디를 입력해주세요 : ")
        pw=input("비밀번호를 입력해주세요 : ")

        all3=input("전체계정의 수정대기로 이동하시겠습니까? y or n")
        if all3.lower()=='y':
            allsteady()
        else:
            pass

        account=int(input(" 계정을 선택해주세요 : 1번 - 도로시 2번 - 세일파이코리아:  "))
        market=int(input(" 마켓을 선택하세요 : 1번 - 옥션 2번 - g마켓 3번 - 인터파크 4번 - 스마트스토어 5번 - 11번가 6번- nh마켓 : "))
        doit=int(input("무엇을 할지 선택하세 요 : 1번 - 판매중 2번 - 수정대기 3번 - 판매대기 :"))
        if account==1 and market==1 and doit==1:
            auctionsale()
        elif account==1 and market==1 and doit==2:
            auctionsteady()
        elif account==1 and market==1 and doit==3:
            auction()
        elif account==1 and market==2 and doit==1:
            gmarketsale()
        elif account==1 and market==2 and doit==2:
            gmarketsteady()
        elif account==1 and market==2 and doit==3:
            gmarket()
        elif account==1 and market==3 and doit==1:
            interparksale()
        elif account==1 and market==3 and doit==2:
            interparksteady()
        elif account==1 and market==3 and doit==3:
            interpark()
        elif account==1 and market==4 and doit==1:
            naversale()
        elif account==1 and market==4 and doit==2:
            naversteady()
        elif account==1 and market==4 and doit==3:
            naver()
        elif account==1 and market==5 and doit==1:
            bunsale()
        elif account==1 and market==5 and doit==2:
            bunsteady()
        elif account==1 and market==5 and doit==3:
            bun()
        elif account==1 and market==6 and doit==1:
            nhsale()
        elif account==1 and market==6 and doit==2:
            nhsteady()
        elif account==1 and market==6 and doit==3:
            nh()
        elif account==2 and market==1 and doit==1:
            auctionsale2()
        elif account==2 and market==1 and doit==2:
            auctionsteady2()
        elif account==2 and market==1 and doit==3:
            auction2()
        elif account==2 and market==2 and doit==1:
            gmarketsale2()
        elif account==2 and market==2 and doit==2:
            gmarketsteady2()
        elif account==2 and market==2 and doit==3:
            gmarket2()
        elif account==2 and market==3 and doit==1:
            interparksale2()
        elif account==2 and market==3 and doit==2:
            interparksteady2()
        elif account==2 and market==3 and doit==3:
            interpark2()
        elif account==2 and market==4 and doit==1:
            naversale2()
        elif account==2 and market==4 and doit==2:
            naversteady2()
        elif account==2 and market==4 and doit==3:
            naver2()
        elif account==2 and market==5 and doit==1:
            bunsale2()
        elif account==2 and market==5 and doit==2:
            bunsteady2()
        elif account==2 and market==5 and doit==3:
            bun2()
        elif account==2 and market==6 and doit==1:
            nhsale2()
        elif account==2 and market==6 and doit==2:
            nhsteady2()
        elif account==2 and market==6 and doit==3:
            nh2()
        else:
            pass
               
        esm=input("esm plus를 실행하실겁니까? y or n : ")
        if esm.lower()=='y':
            id2=input("아이디를 입력하세요")
            pw2=input("비밀번호를 입력하세요")
            doit2=int(input("무엇을 실행하실겁니까? -- 옥션판매가능 1번 옥션판매중지 2번 gmarket판매가능 3번 gmarket판매중지 4번 "))
            if doit2==1:
                aesmsale()
            elif doit2==2:
                aesmstop()
            elif doit2==3:
                gesmsale()
            elif doit2==4:
                gesmstop()
        else:
            pass

        exitdo=input("작업을 중지하시겠습니까? y or n ;")
        if exitdo.lower()=='y':
            sys.exit()
        else:
            continue