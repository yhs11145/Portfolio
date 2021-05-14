import win32com.client
import sys,os,time

excel=win32com.client.Dispatch("Excel.Application")
excel.Visible=True
wb=excel.workbooks.Open(os.getcwd()+'\price.xlsx')
ws1=wb.Worksheets('가격비교')
ws2=wb.Worksheets('아싸컴')
ws3=wb.Worksheets('블루아이티')
ws4=wb.Worksheets('오마이피씨')
ws5=wb.Worksheets('컴집')
ws6=wb.Worksheets('왕가피씨')
ws7=wb.Worksheets('팝콘피씨')
ws8=wb.Worksheets('컴마왕')
i=2
origin=2 ## 가격비교 번호

##가격비교시트에서 CPU,VGA 등록
cpu=ws1.Cells(2,1).Value
vga=ws1.Cells(2,2).Value
test=ws2.Cells(i,5).Value
test2=ws2.Cells(i,8).Value

##비교
ws1.Cells(origin,3).Value='아싸컴'
origin+=1
while(1):
    if ws2.Cells(i,5).Value is None:
        break
    if cpu in ws2.Cells(i,5).Value and vga in ws2.Cells(i,8).Value:
        ws1.Cells(origin,3).value=ws2.Cells(i,1).Value #상품제목
        ws1.Cells(origin,4).value=ws2.Cells(i,3).Value ##가격
        ws1.Cells(origin,5).Value=ws2.Cells(i,5).Value ##cpu
        ws1.Cells(origin,8).Value=ws2.Cells(i,6).Value ## Ram
        ws1.Cells(origin,9).Value=ws2.Cells(i,7).Value ## SSD
        ws1.Cells(origin,11).Value=ws2.Cells(i,8).Value ## VGA
        origin+=1
    i+=1

i=2
ws1.Cells(origin,3).Value="블루아이티"
origin+=1
while(1):
    if ws3.Cells(i,3).Value is None:
        break
    if (cpu in ws3.Cells(i,3).Value and (vga in ws3.Cells(i,6).Value or vga in ws3.Cells(i,7).Value)):
        ws1.Cells(origin,3).Value=ws3.Cells(i,1).Value #상품제목
        ws1.Cells(origin,5).Value=ws3.Cells(i,3).Value ##CPU
        ws1.Cells(origin,4).Value=ws3.Cells(i,20).Value##가격
        for j in range(4,19):##나머지
            ws1.Cells(origin,j+3).Value=ws3.Cells(i,j).Value
        origin+=1
    i+=1

i=2
ws1.Cells(origin,3).Value="오마이피씨"
origin+=1
while(1):
    if ws4.Cells(i,4).Value is None:
        break
    if (cpu in ws4.Cells(i,4).Value or cpu in ws4.Cells(i,5).Value) and (vga in ws4.Cells(i,9).Value or vga in ws4.Cells(i,10).Value):
        ws1.Cells(origin,3).Value=ws4.Cells(i,1).Value##상품제목
        ws1.Cells(origin,4).Value=ws4.Cells(i,2).Value##가격
        for j in range(3,19):##나머지
            ws1.Cells(origin,j+2).Value=ws4.Cells(i,j).Value
        origin+=1
    i+=1

i=2
ws1.Cells(origin,3).Value="컴집"
origin+=1
while(1):
    if ws5.Cells(i,3).Value is None:
        break
    if cpu in ws5.Cells(i,3).Value and vga in ws5.Cells(i,9).Value:
        ws1.Cells(origin,3).Value=ws5.Cells(i,1).Value ##상품제목
        ws1.Cells(origin,3).Value=ws5.Cells(i,2).Value#가격
        ws1.Cells(origin,5).Value=ws5.Cells(i,3).Value ##CPU
        ws1.Cells(origin,6).value=ws5.Cells(i,4).Value ##쿨러
        ws1.Cells(origin,7).Value=ws5.Cells(i,5).Value ##메인보드
        ws1.Cells(origin,8).Value=ws5.Cells(i,6).Value ##RAM
        ws1.Cells(origin,9).Value=ws5.Cells(i,7).Value ##SSD
        ws1.Cells(origin,10).Value=ws5.Cells(i,8).Value ##HDD
        ws1.Cells(origin,11).Value=ws5.Cells(i,9).Value ##VGA
        ws1.Cells(origin,13).Value=ws5.Cells(i,13).Value ##케이스
        ws1.Cells(origin,12).Value=ws5.Cells(i,14).Value ##파워
        origin+=1
    i+=1

i=2
ws1.Cells(origin,3).Value="왕가피씨"
origin+=1
while(1):
    if ws6.Cells(i,4).Value is None:
        break
    if cpu in ws6.Cells(i,4).Value and vga in ws6.Cells(i,8).Value:
        ws1.Cells(origin,3).Value=ws6.Cells(i,1).Value ##상품제목
        ws1.Cells(origin,4).value=ws6.Cells(i,2).Value##가격
        ws1.Cells(origin,5).Value=ws6.Cells(i,4).Value##CPU
        ws1.Cells(origin,6).Value=ws6.Cells(i,5).Value ##쿨러
        ws1.Cells(origin,8).Value=ws6.Cells(i,6).Value #RAM
        ws1.Cells(origin,7).Value=ws6.Cells(i,7).Value ##메인보드
        ws1.Cells(origin,11).Value=ws6.Cells(i,8).Value ##VGA
        ws1.Cells(origin,9).Value=ws6.Cells(i,9).Value ##ssd
        ws1.Cells(origin,10).Value=ws6.Cells(i,10).Value ##HDD
        ws1.Cells(origin,12).Value=ws6.Cells(i,13).Value ##power
        ws1.Cells(origin,13).Value=ws6.Cells(i,14).Value ##케이스
        origin+=1
    i+=1

i=2
ws1.Cells(origin,3).Value="팝콘피씨"
origin+=1
while(1):
    if ws7.Cells(i,3).Value is None:
        break
    if (cpu in ws7.Cells(i,4).Value or cpu in ws7.Cells(i,5).Value) and (vga in ws7.Cells(i,8).Value or vga in ws7.Cells(i,9).Value):
        ws1.Cells(origin,3).Value=ws7.Cells(i,1).Value#상품이름
        ws1.Cells(origin,4).Value=ws7.Cells(i,2).Value#가격
        for j in range(4,21):##나머지
            ws1.Cells(origin,j+1).Value=ws7.Cells(i,j).Value
        origin+=1
    i+=1

i=2
ws1.cells(origin,3).Value="컴마왕"
origin+=1
while(1):
    if ws8.Cells(i,4).Value is None:
        break
    if (cpu in ws8.Cells(i,4).Value or cpu in ws8.Cells(i,5).value) and (vga in ws8.Cells(i,8).Value or vga in ws8.Cells(i,9).Value):
        ws1.Cells(origin,3).Value=ws8.Cells(i,1).Value ##상품이름
        ws1.Cells(origin,4).Value=ws8.Cells(i,2).Value##가격
        for j in range(4,15):##나머지
            ws1.Cells(origin,j+1).Value=ws8.Cells(i,j).Value
        origin+=1
    i+=1