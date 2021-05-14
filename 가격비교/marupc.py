import sys,os,time
from selenium import webdriver
from bs4 import BeautifulSoup
import win32com.client

if getattr(sys, 'frozen', False):
    Chrome_path = os.path.join(sys._MEIPASS, "ChromeDriver.exe")
    driver = webdriver.Chrome(Chrome_path)
else:
    driver=webdriver.Chrome()


##driver.get('https://smartstore.naver.com/coolzen/products/2780184986')
driver.get("https://smartstore.naver.com/marupc/products/2095714252")

time.sleep(2)
driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div[2]/fieldset/div[6]/div[1]/a').click()
time.sleep(2)
html=driver.page_source
soup=BeautifulSoup(html,'html.parser')
for name in soup.select('#content > div > div._2-I30XS1lA > div._2QCa6wHHPy > fieldset > div.Klq2ZNy50Z > div:nth-child(1) > ul'):
    print(name.get_text('\n'))
