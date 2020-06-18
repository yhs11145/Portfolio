from bs4 import BeautifulSoup
import requests
import urllib.parse
import sys,os,time
import win32com.client
    
excel=win32com.client.Dispatch("Excel.Application")
excel.Visible=True
url='/네이버블로그.xlsx'
wb=excel.workbooks.Open(os.getcwd()+url)
ws=wb.ActiveSheet

i=1
while(1):
    if ws.Cells(i,1).Value is not None:
        j=2
        start=1
        product=ws.Cells(i,1).Value
        url="https://search.naver.com/search.naver?where=post&sm=tab_jum&start={}"
        while(1):
            values={
                'query':product
            }
            params=urllib.parse.urlencode(values)
            urls=url.format(start)
            urlss=urls+"&"+params
            #print("URL=",urlss)
            html=urllib.request.urlopen(urlss).read()
            soup=BeautifulSoup(html,'html.parser')
            for pagenumber in range(1,11):
                for blogurl in soup.select('#sp_blog_'+str(pagenumber)+' > dl > dd.txt_block > span > a.url'):
                    ws.Cells(i,j).Value=blogurl.get('href')
                    j+=1
            start+=10
            if start==91:
                break  
        i+=1
    else:
        break
    