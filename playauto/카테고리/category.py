import sys, os, time
import win32com.client
from selenium import webdriver
from bs4 import BeautifulSoup

if getattr(sys, 'frozen', False):
    Chrome_path = os.path.join(sys._MEIPASS, "ChromeDriver.exe")
    driver = webdriver.Chrome(Chrome_path)
else:
    driver=webdriver.Chrome()

excel=win32com.client.Dispatch("Excel.Application")
excel.Visible=True
url=input("엑셀 파일 경로를 입력하세요. :")
wb=excel.workbooks.Open(url)
ws=wb.ActiveSheet


id=input('아이디를 입력하세요: ')
pw=input('비밀번호를 입력하세요: ')

driver.get('https://app.playauto.io/#!/settings/category')
time.sleep(2)
driver.find_element_by_name("email").send_keys(id)
driver.find_element_by_name("password").send_keys(pw)
driver.find_element_by_xpath('/html/body/div[3]/div/div/form/div/div[5]/div/button').click()
time.sleep(2)

while(1):
    try:
        for k in range(700,1000):
            try:
                driver.find_element_by_xpath('//*[@id="modal-notice-content-'+str(k)+'"]/div[1]/button').click()
            except:
                pass        
        time.sleep(2)
        break
    except:
        print("팝업창에러")
        time.sleep(2)
        pass

driver.get('https://app.playauto.io/#!/settings/category')
time.sleep(5)
for i in range(2,int(ws.Cells(1,1).Value)+2):
     number=ws.Cells(i,1).Value
     driver.find_element_by_xpath("//*[@id="+str(number)+"]/span").click()
     time.sleep(5)
     driver.find_element_by_xpath('//*[@id="infoSidebar"]/div[1]/div[1]/div[3]').click()
     time.sleep(5)
     driver.find_element_by_xpath('//*[@id="matchingInfo_0"]/div/form/div[5]/div/label/input').click()
     time.sleep(5)
     driver.find_element_by_xpath('//*[@id="matchingInfo_0"]/div/form/div[5]/div/button[1]').click()
     time.sleep(5)
     driver.find_element_by_xpath('//*[@id="infoSidebar"]/div[3]/div[1]/div[3]').click()
     time.sleep(5)
     driver.find_element_by_xpath('//*[@id="matchingInfo_2"]/div/form/div[6]/div/label/input').click()
     time.sleep(5)
     driver.find_element_by_xpath('//*[@id="matchingInfo_2"]/div/form/div[6]/div/button[1]').click()
     time.sleep(5)
     driver.find_element_by_xpath('//*[@id="infoSidebar"]/div[5]/div[1]/div[3]').click()
     time.sleep(5)
     driver.find_element_by_xpath('//*[@id="matchingInfo_4"]/div/form/div[3]/div/label/input').click()
     time.sleep(5)
     driver.find_element_by_xpath('//*[@id="matchingInfo_4"]/div/form/div[3]/div/button[1]').click()
     time.sleep(5)
     driver.find_element_by_xpath('//*[@id="infoSidebar"]/div[8]/div[1]/div[3]').click()
     time.sleep(5)
     driver.find_element_by_xpath('//*[@id="matchingInfo_7"]/div/form/div[3]/div/label/input').click()
     time.sleep(5)
     driver.find_element_by_xpath('//*[@id="matchingInfo_7"]/div/form/div[3]/div/button[1]').click()
     time.sleep(5)
     driver.find_element_by_xpath('//*[@id="infoSidebar"]/div[9]/div[1]/div[3]').click()
     time.sleep(5)
     driver.find_element_by_xpath('//*[@id="matchingInfo_8"]/div/form/div[4]/div/label/input').click()
     time.sleep(5)
     driver.find_element_by_xpath('//*[@id="matchingInfo_8"]/div/form/div[4]/div/button[1]').click()
     time.sleep(5)
