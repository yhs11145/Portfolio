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
    slack.chat.post_message('#pythonmessage','위메프 딜->>>'+ordermessage)
    
driver.get('https://front.wemakeprice.com/deal/603256843')
time.sleep(5)
html=driver.page_source
soup=BeautifulSoup(html,'html.parser')
for i in soup.select('#_infoDescription > div:nth-child(3) > div.box_inputarea > span > strong'):
    slack_data(i.text.strip())
driver.quit()