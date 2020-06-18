from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import win32com.client
import sys,os,time
from selenium.webdriver.common.action_chains import ActionChains
import pyperclip

if getattr(sys, 'frozen', False):
    Chrome_path = os.path.join(sys._MEIPASS, "ChromeDriver.exe")
    driver = webdriver.Chrome(Chrome_path)
else:
    driver=webdriver.Chrome()

excel=win32com.client.Dispatch("Excel.Application")
excel.Visible=True
wb = excel.Workbooks.Add()
ws = wb.Worksheets("Sheet1")

def copy_input(xpath, input):
    pyperclip.copy(input)
    driver.find_element_by_xpath(xpath).click()
    ActionChains(driver).key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()
    time.sleep(1)
    
driver.get('https://partner.talk.naver.com/')
time.sleep(2)
driver.find_element_by_xpath('//*[@id="visual"]/div/a[1]').click()


id="sellingcorp"
pw="tpfqudtls123!"
time.sleep(1)
copy_input('//*[@id="id"]',id)
copy_input('//*[@id="pw"]',pw)
time.sleep(5)
driver.find_element_by_xpath('//*[@id="log.login"]').click()
time.sleep(2)


idlist=['https://partner.talk.naver.com/web/accounts/100875156','https://partner.talk.naver.com/web/accounts/100848257','https://partner.talk.naver.com/web/accounts/100847995',
        'https://partner.talk.naver.com/web/accounts/100833362','https://partner.talk.naver.com/web/accounts/100769764','https://partner.talk.naver.com/web/accounts/100718452',
        'https://partner.talk.naver.com/web/accounts/100702749','https://partner.talk.naver.com/web/accounts/100681854','https://partner.talk.naver.com/web/accounts/100681679',
        'https://partner.talk.naver.com/web/accounts/100676606','https://partner.talk.naver.com/web/accounts/100566692']

j=2
for i in range(0,11):
    driver.get(idlist[i])
    time.sleep(5)
    html=driver.page_source
    soup=BeautifulSoup(html,'html.parser')
    for name in soup.select('#container > div.lnb > div > div.info_seller > div.seller_state > p > a'):
        ws.Cells(j,2).Value=name.text.strip()
    for steady in soup.select('#container > div.content > div > div > div:nth-child(1) > div.content_box.account_box > div.box_container.layout_fluid > div:nth-child(1) > div.item_dash_counseling > a > span > span'):
        ws.Cells(j,3).Value=steady.text.strip()
    for now in soup.select('#container > div.content > div > div > div:nth-child(1) > div.content_box.account_box > div.box_container.layout_fluid > div:nth-child(2) > div.item_dash_counseling > a > span > span'):
        ws.Cells(j,4).Value=now.text.strip()
    for stop in soup.select('#container > div.content > div > div > div:nth-child(1) > div.content_box.account_box > div.box_container.layout_fluid > div:nth-child(3) > div.item_dash_counseling > a > span > span'):
        ws.Cells(j,5).Value=stop.text.strip()
    j+=1
