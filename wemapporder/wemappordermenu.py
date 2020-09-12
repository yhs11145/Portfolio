# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'wemappordermenu.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
'''
from PyQt5 import QtCore, QtGui, QtWidgets
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys,os,time
from datetime import datetime,timedelta
from bs4 import BeautifulSoup
import win32com.client
from email.mime.base import MIMEBase
import smtplib
from email.mime.text import MIMEText
from email import encoders
from winsound import Beep
'''
'''
if getattr():
        how to write code?find it
else:
    driver=webdriver.Chrome()
'''


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(368, 171)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 30, 318, 99))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.comboBox.setObjectName("comboBox")##아이디입력란 생성
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout.addWidget(self.comboBox, 0, 1, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 2, 1, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 1, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 1, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "위메프주문"))
        self.label.setText(_translate("MainWindow", "아이디 :"))
        self.comboBox.setItemText(0, _translate("MainWindow", "formidab"))
        self.comboBox.setItemText(1, _translate("MainWindow", "kyl5479@nate.com"))
        self.comboBox.setItemText(2, _translate("MainWindow", "wpdhksl1004@naver.com"))
        self.comboBox.setItemText(3, _translate("MainWindow", "park27402@naver.com"))
        self.comboBox.setItemText(4, _translate("MainWindow", "hong3437@naver.com"))
        self.comboBox.setItemText(5, _translate("MainWindow", "nma9090@hanmail.net"))
        self.comboBox.setItemText(6, _translate("MainWindow", "laboum23@naver.com"))
        self.comboBox.setItemText(7, _translate("MainWindow", "myk777@naver.com"))
        self.comboBox.setItemText(8, _translate("MainWindow", "marketnature"))
        self.comboBox.setItemText(9, _translate("MainWindow", "minicbj@naver.com"))
        self.comboBox.setItemText(10, _translate("MainWindow", "cofbsdl1"))
        self.comboBox.setItemText(11, _translate("MainWindow", "11xlesangm@naver.com"))
        self.comboBox.setItemText(12, _translate("MainWindow", "dorothy385"))
        self.comboBox.setItemText(13, _translate("MainWindow", "hkw0101@gmail.com"))
        self.comboBox.setItemText(14, _translate("MainWindow", "tkdgjs354@naver.com"))
        self.comboBox.setItemText(15, _translate("MainWindow", "yoome123@naver.com"))
        self.comboBox.setItemText(16, _translate("MainWindow", "god3078@gmail.com"))
        self.comboBox.setItemText(17, _translate("MainWindow", "yegyu9933@hanmail.net"))
        self.comboBox.setItemText(18, _translate("MainWindow", "jys8358@naver.com"))
        self.comboBox.setItemText(19, _translate("MainWindow", "intelmc9293@naver.com"))
        self.comboBox.setItemText(20, _translate("MainWindow", "jskss123@nate.com"))
        self.comboBox.setItemText(21, _translate("MainWindow", "kyik8385@naver.com"))
        self.comboBox.setItemText(22, _translate("MainWindow", "qpil552@gmail.com"))
        self.comboBox.setItemText(23, _translate("MainWindow", "89summerkim@gmail.com"))
        self.comboBox.setItemText(24, _translate("MainWindow", "leehaming@naver.com"))
        self.comboBox.setItemText(25, _translate("MainWindow", "tjswn1226@naver.com"))
        self.comboBox.setItemText(26, _translate("MainWindow", "secret4477"))
        self.comboBox.setItemText(27, _translate("MainWindow", "hhhsa00@naver.com"))
        self.comboBox.setItemText(28, _translate("MainWindow", "lee0313"))
        self.comboBox.setItemText(29, _translate("MainWindow", "kambo99@naver.com"))
        self.comboBox.setItemText(30, _translate("MainWindow", "tjdrbs0707@naver.com"))
        self.comboBox.setItemText(31, _translate("MainWindow", "jskss52@naver.com"))
        self.comboBox.setItemText(32, _translate("MainWindow", "dlaudgo84@naver.com"))
        self.comboBox.setItemText(33, _translate("MainWindow", "lee_ham@hanmail.net"))
        self.comboBox.setItemText(34, _translate("MainWindow", "moodo_@hanmail.net"))
        self.comboBox.setItemText(35, _translate("MainWindow", "yd21c85"))
        self.comboBox.setItemText(36, _translate("MainWindow", "jhkimduke@gmail.com"))
        self.comboBox.setItemText(37, _translate("MainWindow", "kyongjungok@naver.com"))
        self.comboBox.setItemText(38, _translate("MainWindow", "trendhunting"))
        self.comboBox.setItemText(39, _translate("MainWindow", "passion110@naver.com"))
        self.comboBox.setItemText(40, _translate("MainWindow", "getho1@hanmail.net"))
        self.comboBox.setItemText(41, _translate("MainWindow", "xpoctopus@naver.com"))
        self.label_2.setText(_translate("MainWindow", "시작날짜"))
        self.label_3.setText(_translate("MainWindow", "끝나는날짜"))
        self.pushButton.setText(_translate("MainWindow", "로그인"))
        self.pushButton.clicked.connect(self.PUSH)

    def PUSH(self):
        idx=self.comboBox.currentIndex()
        id=[['']]##아이디,비밀번호
        data1=self.lineEdit.text()
        data2=self.lineEdit_2.text()
        
          id=[['formidab','dlgoal890@@'],['kyl5479@nate.com','rladufma12'],['wpdhksl1004@naver.com','5flanwnd'],['park27402@naver.com','trend700'],['hong3437@naver.com','gmltmd0812!'],
            ['nma9090@hanmail.net','tmddksla00'],['laboum23@naver.com','jym82051516'],['myk777@naver.com','kk411212!'],['marketnature','@@trend700'],['minicbj@naver.com','jymkk051516kk@'],
            ['cofbsdl1','trend2019!'],['11xlesangm@naver.com','claeo1@3'],['dorothy385','claeo1@3'],['hkw0101@gmail.com','!ghkd02161230'],['tkdgjs354@naver.com','tkdgjs9430'],['yoome123@naver.com','dowk123'],
            ['god3078@gmail.com','tmddksla00!'],['yegyu9933@hanmail.net','shwk1323911!'],['jys8358@naver.com','xgb1021'],['intelmc9293@naver.com','trend700'],['jskss123@nate.com','trend700'],['kyik8385@naver.com','aa05130214*'],
            ['qpil552@gmail.com','qwer6135!!'],['89summerkim@gmail.com','rladufma12##'],['leehaming@naver.com','goldbiga001'],['tjswn1226@naver.com','tjswn2003'],['secret4477','bunny12!'],['hhhsa00@naver.com','tmddksla00!'],
            ['lee0313','lhj0313'],['kambo99@naver.com','rladufma12##'],['tjdrbs0707@naver.com','emp!701711'],['jskss52@naver.com','chlgPfls0912'],['dlaudgo84@naver.com','tei0210!'],['lee_ham@hanmail.net','trend700'],
            ['moodo_@hanmail.net','dlaudtn1'],['yd21c85','wjddudals1!'],['jhkimduke@gmail.com','gusdk330!!'],['kyongjungok@naver.com','wjddudals1!'],['trendhunting','@@trend700'],['passion110@naver.com','wjddudals1!'],
            ['getho1@hanmail.net','wjddudals1!'],['xpoctopus@naver.com','wjddudals1!']]##아이디,비밀번호
            
        excel = win32com.client.Dispatch("Excel.Application")
        excel.Visible=True
        url='/wemapporder.xls'
        wb=excel.workbooks.Open(os.getcwd()+url)
        ws = wb.Worksheets("shippingdata")

        today=datetime.today()
        #lastday=today+timedelta(days=-data)
        i=1
        driver.get('https://front.wemakeprice.com/user/login?returnUrl=https%3A%2F%2Ffront.wemakeprice.com%2Fmain&type=GENERAL&orderYN=N&selectionYN=N')
        time.sleep(2)
        while(1):
            driver.find_element_by_id('_loginId').send_keys(id[idx][0])
            driver.find_element_by_id('_loginPw').send_keys(id[idx][1])
            time.sleep(15)
            driver.find_element_by_xpath('//*[@id="_userLogin"]').click()
            
            time.sleep(2)
        
            driver.get('http://www.wemakeprice.com/mypage/buylist/buylist/'+str(data1)+'/'+str(data2))
            if driver.current_url=='http://www.wemakeprice.com/mypage/buylist/buylist/'+str(data1)+'/'+str(data2):
                break
            else:
                Beep(2500,1000)
                Beep(1000,1000)
                time.sleep(10)
                continue
        time.sleep(2)
        while(1):##딜송장
            for number1 in range(1,6):
                try:
                    driver.find_element_by_xpath('//*[@id="content_area"]/table/tbody/tr['+str(number1)+']/td[1]/a[1]/span').click()
                    time.sleep(2)
                    html=driver.page_source
                    soup=BeautifulSoup(html,'html.parser')
                    ws.Cells(i,1).Value=id[idx][0]
                    for orderdate in soup.select('#content_area > div.box_buylist_info > div.noti_area > span:nth-child(2)'):
                        ws.Cells(i,2).Value=orderdate.text.strip()
                    for name1 in soup.select('#content_area > table.tbl_mypage.tbl_detail > tbody > tr > td.cont.ta_left.fst > div > a > strong > span'):
                        ws.Cells(i,3).Value=name1.text.strip()
                    for productcnt1 in soup.select('#content_area > table.tbl_mypage.tbl_detail > tbody > tr > td:nth-child(2)'):
                        ws.Cells(i,4).Value=productcnt1.text.strip()
                    for ordername1 in soup.select('#content_area > table:nth-child(8) > tbody > tr.fst > td'):
                        ws.Cells(i,5).Value=ordername1.text.strip()
                    for address1 in soup.select('#addr > span > span:nth-child(2)'):
                        ws.Cells(i,6).Value=address1.text.strip()
                    i+=1
                    ws.Cells(i,3).Value=name1.text.strip()
                    ws.Cells(i,4).Value=productcnt1.text.strip()
                    ws.Cells(i,5).Value=ordername1.text.strip()
                    driver.execute_script("window.history.go(-1)")
                    time.sleep(2)
                    driver.find_element_by_xpath('//*[@id="content_area"]/table/tbody/tr['+str(number1)+']/td[4]/a[1]/span').click()
                    time.sleep(2)
                    driver.switch_to.window(driver.window_handles[1])
                    html=driver.page_source
                    soup=BeautifulSoup(html,'html.parser')
                    time.sleep(2)
                    try:##첫번째에러 자세히 검색
                        driver.find_element_by_xpath('//*[@id="wrap"]/div/div[2]/div[2]/table/tbody/tr[1]/td[2]/a').click()
                        html=driver.page_source
                        soup=BeautifulSoup(html,'html.parser')
                        time.sleep(2)
                        for address12 in soup.select('#wrap > div > div.layer_pop_body > table.basic_info > tbody > tr:nth-child(3) > td'):
                            ws.Cells(i,6).Value=address12.text.strip()
                        i-=1
                        for ordernumber1 in soup.select('#wrap > div > div.layer_pop_body > table.basic_info > tbody > tr:nth-child(4) > td:nth-child(4)'):
                            ws.Cells(i,7).Value=ordernumber1.text.strip()
                        for tax1 in soup.select('#wrap > div > div.layer_pop_body > table.basic_info > tbody > tr:nth-child(4) > td:nth-child(2)'):
                            ws.Cells(i,8).Value=tax1.text.strip()
                        i+=1
                        ws.Cells(i,7).Value=ordernumber1.text.strip()
                        ws.Cells(i,8).Value=tax1.text.strip()
                        driver.close()
                        driver.switch_to.window(driver.window_handles[0])
                        i+=1
                    except:
                        try:##배송조회
                            for address12 in soup.select('#wrap > div > div.layer_pop_body > table.basic_info > tbody > tr:nth-child(3) > td'):
                                ws.Cells(i,6).Value=address12.text.strip()
                            i-=1
                            for ordernumber1 in soup.select('#wrap > div > div.layer_pop_body > table.basic_info > tbody > tr:nth-child(4) > td:nth-child(4)'):
                                ws.Cells(i,7).Value=ordernumber1.text.strip()
                            for tax1 in soup.select('#wrap > div > div.layer_pop_body > table.basic_info > tbody > tr:nth-child(4) > td:nth-child(2)'):
                                ws.Cells(i,8).Value=tax1.text.strip()
                            i+=1
                            ws.Cells(i,7).Value=ordernumber1.text.strip()
                            ws.Cells(i,8).Value=tax1.text.strip()
                        except:
                            for realdelivery in soup.select('#wrap > div > div.content > div.tbl_invoice > table > tbody > tr > td:nth-child(2) > div > span > span.text_help'):
                                ws.Cells(i,8).Value=realdelivery.text.strip()
                            
                        driver.close()
                        driver.switch_to.window(driver.window_handles[0])
                        i+=1
                except:
                    print("딜송장이 없습니다. 잠시만 기다려주세요.")
                    i+=1
                    time.sleep(2)
                    pass
            break

        driver.get('https://front.wemakeprice.com/mypage/orders?schStartDate='+str(data1)+'&schEndDate='+str(data2))##상품
        time.sleep(2)
        while(1):
            for number in range(1,6):
                try:
                    driver.find_element_by_css_selector('#_contents > div > div > div.mypage_con.fusion_con > div.order_shipps_area.order_list > div.order_shipps_table > table > tbody > tr:nth-child('+str(number)+') > td:nth-child(1) > div > a').click()    
                    #driver.find_element_by_xpath('//*[@id="_contents"]/div/div/div[2]/div[3]/div[2]/table/tbody/tr['+str(number)+']/td[1]/div/a').click()
                    time.sleep(2)
                    html=driver.page_source
                    soup=BeautifulSoup(html,'html.parser')
                    ws.Cells(i,1).Value=id[idx][0]
                    for orderdate2 in soup.select('#_contents > div > div > div.mypage_con > div.order_shipps_area.detail_order > div.order_date_num_area > ul > li:nth-child(1)'):
                        ws.Cells(i,2).Value=orderdate2.text.strip()
                    for name in soup.select('#_contents > div > div > div.mypage_con > div.order_shipps_area.detail_order > div.order_shipps_table > table > tbody > tr > td:nth-child(1) > div > div > div > a'):
                        ws.Cells(i,3).Value=name.text.strip()
                    for productcnt in soup.select('#_contents > div > div > div.mypage_con > div.order_shipps_area.detail_order > div.order_shipps_table > table > tbody > tr > td:nth-child(1) > ul > li > div > span > span.cnt'):
                        ws.Cells(i,4).Value=productcnt.text.strip()
                    for ordername in soup.select('#_contents > div > div > div.mypage_con > div.order_shipps_area.detail_order > div.shipps_info_table > table > tbody > tr:nth-child(1) > td:nth-child(2) > p'):
                        ws.Cells(i,5).Value=ordername.text.strip()
                    for address in soup.select('#_contents > div > div > div.mypage_con > div.order_shipps_area.detail_order > div.shipps_info_table > table > tbody > tr:nth-child(3) > td:nth-child(2) > p.street > span:nth-child(2)'):
                        ws.Cells(i,6).Value=address.text.strip()
                    i+=1
                    ws.Cells(i,3).Value=name.text.strip()
                    ws.Cells(i,4).Value=productcnt.text.strip()
                    ws.Cells(i,5).Value=ordername.text.strip()
                    for address2 in soup.select('#_contents > div > div > div.mypage_con > div.order_shipps_area.detail_order > div.shipps_info_table > table > tbody > tr:nth-child(3) > td:nth-child(2) > p.text_view > span:nth-child(3)'):
                        ws.Cells(i,6).Value=address2.text.strip()
                    i-=1
                    driver.execute_script("window.history.go(-1)")
                    try:##배송조회
                        try:
                            try:
                                driver.find_element_by_xpath('//*[@id="_contents"]/div/div/div[2]/div[3]/div[2]/table/tbody/tr['+str(number)+']/td[3]/a[1]').click()
                            except:
                                driver.find_element_by_xpath('//*[@id="_contents"]/div/div/div[2]/div[2]/div[2]/table/tbody/tr['+str(number)+']/td[3]/a[1]').click()
                        except:
                            driver.find_element_by_xpath('//*[@id="_contents"]/div/div/div[2]/div[4]/div[2]/table/tbody/tr['+str(number)+']/td[3]/a[1]').click()
                            
                        driver.switch_to.window(driver.window_handles[1])
                        html=driver.page_source
                        soup=BeautifulSoup(html,'html.parser')
                        for ordernumber in soup.select('body > div > div.pop_cnt > table.basic_info > tbody > tr:nth-child(2) > td'):#송장번호
                            ws.Cells(i,7).Value=ordernumber.text.strip()
                            i+=1
                            ws.Cells(i,7).Value=ordernumber.text.strip()
                            i-=1
                        for tax in soup.select('body > div > div.pop_cnt > table.basic_info > tbody > tr:nth-child(1) > td'):#택배사
                            ws.Cells(i,8).Value=tax.text.strip()
                            i+=1
                            ws.Cells(i,8).Value=tax.text.strip()   
                        for ordernumber2 in soup.select('body > div > div.pop_cnt > table > tbody > tr:nth-child(1) > td > p'):#직접배송
                            ws.Cells(i,7).Value=ordernumber2.text.strip()
                            ws.Cells(i,8).Value=ordernumber2.text.strip()
                            i+=1
                            ws.Cells(i,7).Value=ordernumber2.text.strip()
                            ws.Cells(i,8).Value=ordernumber2.text.strip()
                        driver.close()
                        driver.switch_to.window(driver.window_handles[0])
                    except:##배송조회
                        try:
                            time.sleep(2)
                            html=driver.page_source
                            soup=BeautifulSoup(html,'html.parser')
                            for ordernumber in soup.select('body > div.ui-dialog > div > div.layer_pop_body > div > div > div > table > tbody > tr > td.check > a'):
                                ws.Cells(i,7).Value=ordernumber.text.strip()
                                i+=1
                                ws.Cells(i,7).Value=ordernumber.text.strip()
                                i-=1
                            for tax in soup.select('body > div.ui-dialog > div > div.layer_pop_body > div > div > div > table > tbody > tr > td.method'):
                                ws.Cells(i,8).Value=tax.text.strip()
                                i+=1
                                ws.Cells(i,8).Value=tax.text.strip()   
                            for ordernumber2 in soup.select('body > div > div.pop_cnt > table > tbody > tr:nth-child(1) > td > p'):
                                ws.Cells(i,7).Value=ordernumber2.text.strip()
                                ws.Cells(i,8).Value=ordernumber2.text.strip()
                                i+=1
                                ws.Cells(i,7).Value=ordernumber2.text.strip()
                                ws.Cells(i,8).Value=ordernumber2.text.strip()                            
                            driver.find_element_by_xpath('/html/body/div[5]/div/a').click()
                            driver.switch_to.window(driver.window_handles[0])
                            pass
                        except:
                            print("송장전송이 끝났습니다. 잠시만 기다리세요")
                            pass    
                    i+=1
                except:##자세히 조회
                    print(driver.current_url)
                    print("합배송에러. 혹은 더이상 없음. 다음페이지를 조회합니다. 잠시만 기다리세요. ")
                    time.sleep(30)
                    pass
            try:
                driver.find_element_by_class_name('btn_next').click()
                time.sleep(2)
            except:
                print("모든 작업이 끝났습니다.")
                Beep(2500,1000)
                driver.get('https://front.wemakeprice.com/logout')
                break

        #ws.SaveAs('C:\\Users\\jys83\\Desktop\\palyauto_weapp\\2_todayinfo\\'+today.strftime("%Y-%m-%d")+id+'.xls')
        ws.SaveAs(os.getcwd()+'/'+today.strftime("%Y-%m-%d")+'_'+id[idx][0]+'.xls')
        print(os.getcwd()+'/'+today.strftime("%Y-%m-%d")+'_'+id[idx][0]+'.xls')
        print("전송완료")
        #s = smtplib.SMTP_SSL('smtp.naver.com', 465)
        #s.login('floweringtown@naver.com','rhsdir27!@#')

        #msg=MIMEBase('multipart','mixed')
        #cont=MIMEText("송장전송완료 엑셀데이터 전송")
        #cont['subject']='송장전송완료알림'
        #cont['From']='floweringtown@naver.com'
        #cont['To']='floweringtown@naver.com'
        #msg.attach(cont)
        #path=os.getcwd()+'/'+today.strftime("%Y-%m-%d")+'_'+id+'.xls'
        #part=MIMEBase("application","octet-stream")
        #part.set_payload(open(path,'rb').read())
        #encoders.encode_base64(part)
        #part.add_header('Content-Disposition', 'attachment; filename=%s'%os.path.basename(path))
        #msg.attach(part)
        #s.sendmail('floweringtown@naver.com','floweringtown@naver.com',msg.as_string())
        #s.quit()
        
        excel.Quit()
        
            



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

