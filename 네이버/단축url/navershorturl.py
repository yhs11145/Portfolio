import os,sys,time
import urllib.request
import win32com.client
import json
'''
excel=win32com.client.Dispatch("Excel.Application")
excel.Visible=True
url=input("경로를 입력하세요")
wb=excel.workbooks.Open(url)
ws=wb.ActiveSheet

celldata=ws.Cells(,).Value.text.strip()
'''

client_id = "hOGdYUQ5RD5vrMvLqEY9" # 개발자센터에서 발급받은 Client ID 값
client_secret = "vDKgGlVENu" # 개발자센터에서 발급받은 Client Secret 값
encText = urllib.parse.quote("google.com")
data = "url=" + encText
url = "https://openapi.naver.com/v1/util/shorturl.json"
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request, data=data.encode("utf-8"))
dict=json.load(response)
rescode = response.getcode()
if(rescode==200):
    #response_body = response.read()
    print(dict['result']['url'])
    #ws.Cells(,).Value=dict['result'][url']
    #print(response_body)
    #print(response_body.decode('utf-8'))
else:
    print("Error Code:" + rescode)