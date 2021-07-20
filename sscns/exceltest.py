import sys,os,time
from selenium import webdriver
from bs4 import BeautifulSoup
from datetime import datetime
import win32com.client


excel=win32com.client.Dispatch("Excel.Application") ##크롤링 엑셀
excel.Visible=True
wb = excel.workbooks.Open(os.getcwd()+'\\test.xlsx')
ws = wb.Worksheets("Sheet1")

url=input("제목을 입력하세요") ## 키워드 엑셀
wb1=excel.workbooks.Open(os.getcwd()+'\\'+url)
ws1=wb1.Worksheets("제품명키워드")


number=1 ## 크롤링 엑셀
number2=3 ##키워드 엑셀
number3=4
add=3
add1=0 ##추가할지 말지


first=[]
while(1):
    first.append(ws.Cells(number,2).Value)
    if ws.Cells(number,2).Value is None:
        break
    number+=1
second=[]
while(1):
    second.append(ws1.Cells(number2,4).Value)
    if ws1.Cells(number2,4).Value is None:
        break
    number2+=1
    
    
list=['[판매]삼성 데스크탑/ DB400T7Y-Z303C']
list2=['DB400T7A-Z2A/C','DB400T7Y-Z303C']
for i in first:
    for j in second:
        if second in first:
            continue
    print(i)
    
#listn2=0
#listn1=0
#for i in first:
#    for j in second:
#        if second in first:
#            continue
#    print(i)
        
    
    
        
        



#while(1):
 #   if :
 #       number+=1
 #       number2=3
 #   else:
 #       number2+=1
#    if ws1.Cells(number2,4).Value is None:
 #       ws1.Cells(number3,10).Value=ws.Cells(number,2).Value
 #       number3+=1
 #       number2=3
 #       number+=1
 #   if ws.Cells(number,2).Value is None:
 #       break
