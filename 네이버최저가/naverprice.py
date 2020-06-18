import sys,os,time
from bs4 import BeautifulSoup
import urllib.parse
import urllib.request
import smtplib
from email.mime.text import MIMEText

if __name__ == "__main__":
    id=input("메일을 입력해주세요.")
    pw=input("네이버 비밀번호를 입력해주세요")
    url=input("url을 입력해주세요")
    price=int(input("가격을 설정해주세요"))
    sec=float(input("주기적으로 불러올 시간을 입력해주세요"))
    number=int(input("조건을 입력하세요"))
    while True:
        # 세션 생성
        s = smtplib.SMTP('smtp.naver.com', 587)
        # TLS 보안 시작
        s.starttls()
        senderAddr = id
        recipientAddr = id
        s.login(senderAddr, pw)
        text="설정된 가격으로 되었습니다."
        msg=MIMEText(text)
        msg['Subject']="가격설정알람"
        msg['From']=senderAddr
        msg['To']=recipientAddr
        try:
            res=urllib.request.urlopen(url)
            soup=BeautifulSoup(res,"html.parser")
            for j in soup.select('#section_price > div.sort_group > div.condition_group > ul > li:nth-child('+str(number)+') > label > em'):
                print(j.text)
                j=j.text.split('원')[0]
                j=j.replace(',','')
                if int(j)<=price:
                    print("완료")
                    s.sendmail(senderAddr, [recipientAddr], msg.as_string())
                    time.sleep(sec)
                    break
                else:
                    time.sleep(sec)
                    continue
        except:
            print("서버접속실패-재실행중")
            time.sleep(10)
            continue
    s.quit()