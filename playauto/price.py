from selenium import webdriver
import sys,os,time

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
    try:
        time.sleep(2)
        driver.get("https://app.playauto.io/#!/order/shipment/payment_list")
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="payment_shipment_grid"]/thead/tr/th[1]/input').click()
        driver.find_element_by_xpath('/html/body/ui-view/div[2]/div/div[2]/div[3]/div/div/div/div[2]/div[1]/div[1]/div[3]/button/i/span[1]').click()
        driver.find_element_by_xpath('/html/body/ui-view/div[2]/div/div[2]/div[3]/div/div/div/div[2]/div[1]/div[1]/div[3]/ul/li[2]/a').click()
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[3]/div/div[3]/button[1]').click()
        time.sleep(2)
        driver.close()
        break
    except:
        driver.refresh()

