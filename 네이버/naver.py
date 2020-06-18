import sys,os,time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import urllib.parse
import urllib.request
import random

if getattr(sys, 'frozen', False):
    Chrome_path = os.path.join(sys._MEIPASS, "ChromeDriver.exe")
    driver = webdriver.Chrome(Chrome_path)
else:
    driver=webdriver.Chrome()

if __name__ == "__main__":
    name=input("검색어를 입력하세요: ")
    store=input("스토어를 입력하세요: ")
    driver.get('https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query='+str(name))
    time.sleep(random.randrange(1,60))
    driver.get('https://search.naver.com/search.naver?query='+str(name)+'&where=post&sm=tab_nmr&nso=')
    driver.find_element_by_xpath('//*[@id="sp_blog_'+str(random.randrange(1,11))+'"]/dl/dt/a').click()
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(random.randrange(1,60))
    for j in range(1,11):
        time.sleep(2)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        driver.execute_script("window.scrollTo(document.body.scrollHeight, 0);")
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    url="https://search.shopping.naver.com/search/all.nhn?pagingIndex={}"
    for page in range(50):
        a=1
        values={
            'query': name
            }
        params=urllib.parse.urlencode(values)
        urls=url.format(page+1)
        urlss=urls+"&"+params
        print("URL=",urlss)
        res=urllib.request.urlopen(urlss)
        soup=BeautifulSoup(res,"html.parser")
        for i in soup.select('div > ul > li > div > p > a.mall_img'):
            if store in i.text:
                driver.get(urlss)
                time.sleep(1)
                driver.find_element_by_xpath('//*[@id="_search_list"]/div[1]/ul/li['+str(a)+']/div[2]/div/a').click()
                driver.switch_to.window(driver.window_handles[0])
                html=driver.page_source
                soup=BeautifulSoup(html,'html.parser')
                time.sleep(3)
            a+=1
                