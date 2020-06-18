from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sys,os,time
from selenium import webdriver

if getattr(sys, 'frozen', False):
     Chrome_path = os.path.join(sys._MEIPASS, "ChromeDriver.exe")
     driver = webdriver.Chrome(Chrome_path)
else:
     driver=webdriver.Chrome()

def auction():
     id=str1.get()
     pw=str2.get()
     driver.get('https://www.esmplus.com/Home/Home#TDM396')
     driver.find_element_by_id("Id").send_keys(id)
     driver.find_element_by_id("Password").send_keys(pw)
     driver.find_element_by_xpath('//*[@id="btnLogOn"]/img').click()
     driver.get("https://www.esmplus.com/Sell/SingleGoodsMng?menuCode=TDM396")
     driver.find_element_by_xpath('//*[@id="divAcumlSum"]/table/tbody/tr[1]/td[3]/a').click()
     driver.find_element_by_xpath('//*[@id="selPageSize"]/option[7]').click()
     for i in range(3,13):
          time.sleep(2)
          driver.find_element_by_xpath('//*[@id="pagging_GSM010"]/a['+str(i)+']').click()
          time.sleep(5)
          driver.find_element_by_xpath('//*[@id="goodsAddtion"]/span[2]/a').click()
               
def gmarket():
     id=str1.get()
     pw=str2.get()
     driver.get('https://www.esmplus.com/Home/Home#TDM396')
     driver.find_element_by_id("Id").send_keys(id)
     driver.find_element_by_id("Password").send_keys(pw)
     driver.find_element_by_xpath('//*[@id="btnLogOn"]/img').click()
     driver.get("https://www.esmplus.com/Sell/SingleGoodsMng?menuCode=TDM396")
     driver.find_element_by_xpath('//*[@id="divAcumlSum"]/table/tbody/tr[2]/td[3]/a').click()
     driver.find_element_by_xpath('//*[@id="selPageSize"]/option[7]').click()
     for i in range(3,13):
          time.sleep(2)
          driver.find_element_by_xpath('//*[@id="pagging_GSM010"]/a['+str(i)+']').click()
          time.sleep(5)
          driver.find_element_by_xpath('//*[@id="goodsAddtion"]/span[2]/a').click()

def click():
     messagebox.showinfo("실행합니다",str0.get())
     if str0.get()=='auction':
          auction()
     else:
          gmarket()


win=Tk()
win.title("esm plus 엑셀")
win.geometry('400x200')
str0=StringVar()
str1=StringVar()
str2=StringVar()

label1=Label(win,text="id",anchor='s')
label1.grid(column=0,row=0)
label2=Label(win,text="pw",anchor='s')
label2.grid(column=0,row=1)

textbox1=ttk.Entry(win,width=20,textvariable=str1)
textbox1.grid(column=1,row=0)
textbox2=ttk.Entry(win,width=20,textvariable=str2)
textbox2.grid(column=1,row=1)

combo=ttk.Combobox(win,width=20,textvariable=str0)
combo['values']=('auction','gmarket')
combo.grid(column=0,row=2)

combo.set("마켓선택")
action=ttk.Button(win,text="누르세요.",command=click)
action.grid(column=0,row=3)




win.mainloop()
