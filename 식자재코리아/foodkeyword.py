import win32com.client

excel=win32com.client.Dispatch("Excel.Application")
excel.Visible=True
url=input("엑셀 파일 경로를 입력하세요. :")
wb=excel.workbooks.Open(url)
ws=wb.ActiveSheet

i=2
while True:
    if ws.Cells(i,1).Value is None:
        break
    for j in range(6,14):
        if ws.Cells(i,j).Value is not None:
            ws.Cells(i,4).Value+=str(" ")+ws.Cells(i,j).Value
            if ws.Cells(i,5).Value>50:
                ws.Cells(i,4).Value=ws.Cells(i,4).Value.replace(str(" ")+ws.Cells(i,j).Value,"")
        else:
            break
    i+=1
        
