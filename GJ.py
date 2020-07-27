import win32com.client

excel=win32com.client.Dispatch("Excel.Application")
excel.Visible=True
url=input("경로를 입력하세요")
wb=excel.workbooks.Open(url)
ws=wb.ActiveSheet
i=2
while(1):
    name=str(ws.Cells(i,1).Value)
    if ws.Cells(i,1).value is None:
        break
    a=name.split(',')
    while(1):
        for j in range(len(a)):
            if '품절' in a[j]:
                if ws.Cells(i,2).Value is None:
                    ws.Cells(i,2).Value=str("0")
                else:
                    ws.Cells(i,2).Value=str(ws.Cells(i,2).Value)+str(",0")
            elif '단종' in a[j]:
                if ws.Cells(i,2).Value is None:
                    ws.Cells(i,2).Value=str("0")
                else:
                    ws.Cells(i,2).Value=str(ws.Cells(i,2).Value)+str(",0")     
            else:
                if ws.Cells(i,2).Value is None:
                    ws.Cells(i,2).Value=str("9999")
                else:
                    ws.Cells(i,2).Value=str(ws.Cells(i,2).Value)+str(",9999")
        break
    i+=1

