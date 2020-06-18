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
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="sidebar-tabs-5"]/div/div[1]/div/treecontrol/ul/li[7]/treeitem/ul/li[3]/i[1]').click()
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="sidebar-tabs-5"]/div/div[1]/div/treecontrol/ul/li[7]/treeitem/ul/li[3]/treeitem/ul/li[1]/div').click()
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/ui-view/div[2]/div/div[2]/div[3]/div/div/div/div[1]/ul/li[3]/a').click()
except:
    print("retry")
    driver.refresh()
    continue
while(1):
    try:
        time.sleep(5)
        driver.find_element_by_css_selector('div.ui-grid-header > div > div > div > div > div > div.ui-grid-header-cell.ui-grid-clearfix.ui-grid-coluiGrid-0005 > div > div > div').click()
        time.sleep(2)
        driver.find_element_by_xpath('/html/body/ui-view/div[2]/div/div[2]/div[3]/div/div/div/div[2]/div[1]/div[2]/div[3]/button').click()
        time.sleep(2)
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[3]/div/div[2]/button[1]').click()
        time.sleep(10)
        try:
            driver.find_element_by_xpath('//*[@id="shop_product_grid"]/div/div[2]/div[1]/div[1]/button[3]').click()
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
        break
    else:
        sys.exit()
     
     



