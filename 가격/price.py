import win32com.client
from selenium import webdriver
from bs4 import BeautifulSoup
import sys, os, time

if getattr(sys, 'frozen', False):
    Chrome_path = os.path.join(sys._MEIPASS, "ChromeDriver.exe")
    driver = webdriver.Chrome(Chrome_path)
else:
    driver=webdriver.Chrome()
'''    
excel=win32com.client.Dispatch("Excel.Application")
excel.Visible=True
url=input("엑셀 파일 경로를 입력하세요. :")
wb=excel.workbooks.Open(url)
ws=wb.ActiveSheet
'''

driver.get('http://danawa.com/')##다나와 접속
product=input("상품명을 입력하세요") ##상품명입력
driver.find_element_by_xpath('//*[@id="AKCSearch"]').send_keys(product)
driver.find_element_by_xpath('//*[@id="srchFRM_TOP"]/fieldset/div[1]/button/span').click()
time.sleep(2)
html=driver.page_source
soup=BeautifulSoup(html,'html.parser')
    
for url in soup.find_all('p',class_='prod_name'):##링크 가져오기 
    print(url.find('a')['href'])
    print(url.text.strip())#3상품명 가져오기
for price in soup.find_all('p',class_='price_sect'):##가격 가져오기
    print(price.find('a').text.strip())