from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys,os,time
from slacker import Slacker

if getattr(sys, 'frozen', False):
        Chrome_path = os.path.join(sys._MEIPASS, "ChromeDriver.exe")
        driver = webdriver.Chrome(Chrome_path)
else:
    driver=webdriver.Chrome()

def slack_data(ordermessage):
    token="xoxb-1017448255248-1176108620737-4RfMXuHZuEcRFEtfLXPWgx2E"
    slack=Slacker(token)
    slack.chat.post_message('#pythonmessage',ordermessage)

id="sellallmaster@gmail.com"
pw="akdntmzlqhem1@"
driver.get('https://app.playauto.io/login.html')
time.sleep(2)
driver.find_element_by_name("email").send_keys(id)
driver.find_element_by_name("password").send_keys(pw)
driver.find_element_by_xpath('/html/body/div[3]/div/div/form/div/div[5]/div/button').click()
time.sleep(5)
while(1):
    try:
        driver.get('https://app.playauto.io/#!/order/shipment/integrated_list')
        time.sleep(5)
        driver.find_element_by_xpath('//*[@id="integrated_shipment_grid_searchbar"]/div/div[1]/div[1]/div/div/button').click()
        time.sleep(5)
        try:
            #driver.find_element_by_xpath('/html/body/div[1]/div/div/form/div/div[2]/label/input').click()
            driver.find_element_by_xpath('//*[@id="goAction"]').click()
            time.sleep(5)
            driver.find_element_by_xpath('//*[@id="integrated_shipment_grid_searchbar"]/div/div[1]/div[2]/div/div/button').click()
            time.sleep(5)
            driver.find_element_by_xpath('//*[@id="goAction"]').click()
            time.sleep(5)
        except:
            print("대주문수집오류")
            pass
        driver.get('https://app.playauto.io/#!/order/customer_inquiry/list')
        time.sleep(5)
        try:
            driver.find_element_by_xpath('//*[@id="customer_inquiry_grid_searchbar"]/div/div[1]/div[1]/div/div/button').click()
            time.sleep(5)
            driver.find_element_by_xpath('/html/body/div[1]/div/div/form/div/div[3]/div/div[2]/button[1]').click()
        except:
            print("대문의수집오류")
            pass
        time.sleep(600)
        while(1):##주문발주
            try:
                driver.get('https://app.playauto.io/#!/etc/work')
                driver.refresh()
                time.sleep(10)
                driver.find_element_by_xpath('//*[@id="search-detail-state"]/option[4]').click()
                driver.find_element_by_xpath('//*[@id="search-detail-job_cate"]/option[5]').click()
                driver.find_element_by_xpath('//*[@id="sidebar-tabs-1"]/div/div[2]/div[1]/div/div/button').click()
                time.sleep(5)
                html=driver.page_source
                soup=BeautifulSoup(html,'html.parser')
                for i in soup.select('div > div.text-bold.page-number-box'):
                    print(i.text)
                    slack_data('주문발주'+i.text)
                if int(i.string)>=105:
                    break
                else:##주문발주 오류시
                    while(1):
                        print("주문발주오류")
                        driver.get('https://app.playauto.io/#!/etc/work')
                        driver.refresh()
                        time.sleep(10)
                        driver.find_element_by_xpath('//*[@id="search-detail-state"]/option[4]').click()
                        driver.find_element_by_xpath('//*[@id="search-detail-job_cate"]/option[5]').click()
                        driver.find_element_by_xpath('//*[@id="sidebar-tabs-1"]/div/div[2]/div[1]/div/div/button').click()
                        time.sleep(5)
                        driver.find_element_by_css_selector('div.ui-grid-header > div > div > div > div > div > div.ui-grid-header-cell.ui-grid-clearfix.ui-grid-coluiGrid-0005 > div > div > div').click()
                        driver.find_element_by_xpath('/html/body/ui-view/div[2]/div/div[2]/div[3]/div/div/div/div[2]/div[1]/div[1]/div[2]/button').click()
                        time.sleep(2)
                        driver.find_element_by_xpath('/html/body/ui-view/div[2]/div/div[2]/div[3]/div/div/div/div[2]/div[1]/div[1]/div[2]/ul/li[1]/a').click()
                        time.sleep(2)
                        driver.find_element_by_xpath('/html/body/div[8]/div[7]/div/button').click()
                        time.sleep(60)
                        html=driver.page_source
                        soup=BeautifulSoup(html,'html.parser')
                        for i in soup.select('div > div.text-bold.page-number-box'):
                            print(i.text)
                        if int(i.string)>0:
                            continue
                        else:
                            pass
                        print("주문발주오류로 재수집")
                        driver.get('https://app.playauto.io/#!/order/shipment/integrated_list')
                        time.sleep(5)
                        driver.find_element_by_xpath('//*[@id="integrated_shipment_grid_searchbar"]/div/div[1]/div[1]/div/div/button').click()
                        time.sleep(5)
                        driver.find_element_by_xpath('/html/body/div[1]/div/div/form/div/div[2]/label/input').click()
                        driver.find_element_by_xpath('//*[@id="goAction"]').click()
                        time.sleep(5)
                        driver.find_element_by_xpath('//*[@id="integrated_shipment_grid_searchbar"]/div/div[1]/div[2]/div/div/button').click()
                        time.sleep(5)
                        driver.find_element_by_xpath('//*[@id="goAction"]').click()
                        time.sleep(600)
                        break
            except Exception as ex:
                print(ex)
                driver.refresh()
                pass
        while(1):##문의수집
            try:
                driver.get('https://app.playauto.io/#!/etc/work')
                driver.refresh()
                time.sleep(10)
                driver.find_element_by_xpath('//*[@id="search-detail-state"]/option[4]').click()
                driver.find_element_by_xpath('//*[@id="search-detail-job_cate"]/option[6]').click()
                driver.find_element_by_xpath('//*[@id="sidebar-tabs-1"]/div/div[2]/div[1]/div/div/button').click()
                time.sleep(5)
                html=driver.page_source
                soup=BeautifulSoup(html,'html.parser')
                for i in soup.select('div > div.text-bold.page-number-box'):
                    print(i.text)
                    slack_data('문의수집'+i.text)
                if int(i.string)>=78:
                    break
                else:
                    while(1):##문의수집 오류시
                        print("문의수집오류")
                        driver.get('https://app.playauto.io/#!/etc/work')
                        driver.refresh()
                        time.sleep(10)
                        driver.find_element_by_xpath('//*[@id="search-detail-state"]/option[4]').click()
                        driver.find_element_by_xpath('//*[@id="search-detail-job_cate"]/option[6]').click()
                        driver.find_element_by_xpath('//*[@id="sidebar-tabs-1"]/div/div[2]/div[1]/div/div/button').click()
                        time.sleep(5)
                        driver.find_element_by_css_selector('div.ui-grid-header > div > div > div > div > div > div.ui-grid-header-cell.ui-grid-clearfix.ui-grid-coluiGrid-0005 > div > div > div').click()
                        driver.find_element_by_xpath('/html/body/ui-view/div[2]/div/div[2]/div[3]/div/div/div/div[2]/div[1]/div[1]/div[2]/button').click()
                        time.sleep(2)
                        driver.find_element_by_xpath('/html/body/ui-view/div[2]/div/div[2]/div[3]/div/div/div/div[2]/div[1]/div[1]/div[2]/ul/li[1]/a').click()
                        time.sleep(2)
                        driver.find_element_by_xpath('/html/body/div[8]/div[7]/div/button').click()
                        time.sleep(60)
                        html=driver.page_source
                        soup=BeautifulSoup(html,'html.parser')
                        for i in soup.select('div > div.text-bold.page-number-box'):
                            print(i.text) 
                        if int(i.string)>0:
                            continue
                        else:
                            pass
                        print("문의수집오류로 재수집")
                        driver.get('https://app.playauto.io/#!/order/customer_inquiry/list')
                        time.sleep(5)
                        driver.find_element_by_xpath('//*[@id="customer_inquiry_grid_searchbar"]/div/div[1]/div[1]/div/div/button').click()
                        time.sleep(5)
                        driver.find_element_by_xpath('/html/body/div[1]/div/div/form/div/div[3]/div/div[2]/button[1]').click()
                        time.sleep(600)
                        break
            except Exception as ex:
                print(ex)
                driver.refresh()
                pass
        while(1):##삭제작업시작
            driver.get('https://app.playauto.io/#!/etc/work')
            driver.refresh()
            time.sleep(10)
            driver.find_element_by_xpath('//*[@id="search-detail-state"]/option[4]').click()
            driver.find_element_by_xpath('//*[@id="search-detail-job_cate"]/option[5]').click()
            driver.find_element_by_xpath('//*[@id="sidebar-tabs-1"]/div/div[2]/div[1]/div/div/button').click()
            time.sleep(5)
            driver.find_element_by_css_selector('div.ui-grid-header > div > div > div > div > div > div.ui-grid-header-cell.ui-grid-clearfix.ui-grid-coluiGrid-0005 > div > div > div').click()
            driver.find_element_by_xpath('/html/body/ui-view/div[2]/div/div[2]/div[3]/div/div/div/div[2]/div[1]/div[1]/div[2]/button').click()
            time.sleep(2)
            driver.find_element_by_xpath('/html/body/ui-view/div[2]/div/div[2]/div[3]/div/div/div/div[2]/div[1]/div[1]/div[2]/ul/li[1]/a').click()
            time.sleep(2)
            driver.find_element_by_xpath('/html/body/div[8]/div[7]/div/button').click()
            time.sleep(60)
            html=driver.page_source
            soup=BeautifulSoup(html,'html.parser')
            for i in soup.select('div > div.text-bold.page-number-box'):
                print(i.text)
            if int(i.string)>0:
                pass
            else:
                break
        while(1):
            driver.get('https://app.playauto.io/#!/etc/work')
            driver.refresh()
            time.sleep(10)
            driver.find_element_by_xpath('//*[@id="search-detail-state"]/option[4]').click()
            driver.find_element_by_xpath('//*[@id="search-detail-job_cate"]/option[6]').click()
            driver.find_element_by_xpath('//*[@id="sidebar-tabs-1"]/div/div[2]/div[1]/div/div/button').click()
            time.sleep(5)
            driver.find_element_by_css_selector('div.ui-grid-header > div > div > div > div > div > div.ui-grid-header-cell.ui-grid-clearfix.ui-grid-coluiGrid-0005 > div > div > div').click()
            driver.find_element_by_xpath('/html/body/ui-view/div[2]/div/div[2]/div[3]/div/div/div/div[2]/div[1]/div[1]/div[2]/button').click()
            time.sleep(2)
            driver.find_element_by_xpath('/html/body/ui-view/div[2]/div/div[2]/div[3]/div/div/div/div[2]/div[1]/div[1]/div[2]/ul/li[1]/a').click()
            time.sleep(2)
            driver.find_element_by_xpath('/html/body/div[8]/div[7]/div/button').click()
            time.sleep(60)
            html=driver.page_source
            soup=BeautifulSoup(html,'html.parser')
            for i in soup.select('div > div.text-bold.page-number-box'):
                print(i.text)
            if int(i.string)>0:
                pass
            else:
                break
        driver.quit()
        break
    except:
        driver.refresh()
        print("refresh")
        time.sleep(5)
        continue

        