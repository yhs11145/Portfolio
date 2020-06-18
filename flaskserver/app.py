from flask import Flask,render_template,request,flash,request,url_for,redirect,session
import pymysql
from bs4 import BeautifulSoup
from selenium import webdriver
from werkzeug.utils import secure_filename
from selenium.webdriver.common.keys import Keys
import sys,os,time
import json
import requests
from datetime import timedelta
import pandas as pd

app=Flask(__name__)

def connection():
    return pymysql.connect(host='localhost',port=3306,user='selling',passwd='122919',db='sys',charset='utf8')
#curs=conn.cursor()

@app.route('/',methods=['POST', 'GET'])
def index():
    if request.method=='POST':
        id=request.form['id']
        pw=request.form['pw']
        conn=connection()
        curs=conn.cursor()
        sql="select id,pw from user where id=%s and pw=%s"
        curs.execute(sql,(id,pw))
        rows=curs.fetchall()
        print(rows)
        conn.close()
        for row in rows:
            if id==row[0] and pw==row[1]:
                if 'test2'==row[0] and 'test2'==row[1]:
                    session['name']=row[0]
                    return redirect(url_for('admin'),code=307)
                session['name']=row[0]
                return redirect(url_for('user',idname=row[0]))
            else:
                return render_template('fail.html')
        return render_template('fail.html')
    else:
        return render_template('login.html')
    
@app.route('/logout')
def logout():
    session.pop('name',None)
    return render_template('logout.html')

@app.route('/oauth')
def oauth():
    code=str(request.args.get('code'))
    url="https://kauth.kakao.com/oauth/token"
    
    payload="grant_type=authorization_code&client_id=c1bc0da7c5efa08e9595f207e7b8cb08&redirect_uri=http://192.168.0.7:5000/oauth&code="+str(code)
    headers={
        'content-type':'application/x-www-form-urlencoded;charset=utf-8',
    }
    response=requests.request("POST",url,data=payload,headers=headers)
    access_token=json.loads(((response.text).encode('utf-8')))['access_token']
    testtext="이거는 ???"
    API_HOST="https://kapi.kakao.com/v2/api/talk/memo/default/send"
    headers.update({'Authorization':"Bearer "+str(access_token)})
    payloadDict = dict({
    "object_type": "text",
    "text": str(testtext),
    "link": {
        "web_url": "https://foooodleplus.com/contents/login/selectCenter.jsp"
    },
    "button_title":"바로확인",
    })
    payload = 'template_object=' + str(json.dumps(payloadDict))
    response=requests.request("POST",API_HOST,data=payload,headers=headers)
    return (response.text)

@app.route('/kakaosend',methods=['get','post'])
def kakaosend():
    
    return "ok"

@app.route('/user/<idname>', methods=['get', 'post'])
def user(idname):
    if 'name' in session:
        if session['name']!=idname:
            return render_template('fail.html')
        pass
    else:
        return render_template('fail.html')
    pd.set_option('colheader_justify','center')
    pd.options.display.float_format='{:,.0f}'.format
    df=pd.read_excel('upload/'+idname+'.xlsx')
    dateti=df['일자별']
    label1=df['매출금액-건별']
    label2=df['매출원가-건별']
    label3=df['영업이익-건별']
    df['영업이익률-건별']=df['영업이익률-건별'].map('{:.2%}'.format)
    df['매출금액-건별']=df['매출금액-건별'].map('{:,}'.format)
    dftable=df[['일자별','매출금액-건별','매출원가-건별','영업이익-건별','영업이익률-건별','리딩타임-건별']]
   #label4=df['영업이익률']
    #print(label4)

    return render_template('user.html',dateti=dateti,label1=label1,label2=label2,label3=label3,tables=[dftable.to_html(classes='mystyle')],idname=session['name'])

@app.route('/admin',methods=['get','post'])
def admin():
    if 'name' in session:
        if session['name']!='test2':
            return render_template('fail.html')
        pass
    else:
        return render_template('fail.html')
    id=request.form['id']
    pw=request.form['pw']
    if 'test2'==id and 'test2'==pw:
        return render_template('admin.html',id=id)
    else:
        return render_template('fail.html')
   
@app.route('/refund',methods=['get','post'])
def refund():
    if 'name' in session:
        pass
    else:
        return render_template('fail.html')
    conn=connection()
    curs=conn.cursor()
    sql="TRUNCATE refund"
    curs.execute(sql)
    conn.commit()
    conn.close()

    if getattr(sys, 'frozen', False):
        Chrome_path = os.path.join(sys._MEIPASS, "ChromeDriver.exe")
        driver = webdriver.Chrome(Chrome_path)
    else:
        driver=webdriver.Chrome()

    id="dorothy385"
    pw="zlqhem12"
    driver.get("https://www.dometopia.com/member/login")
    driver.find_element_by_name("userid").send_keys(id)
    driver.find_element_by_name("password").send_keys(pw)
    driver.find_element_by_xpath('//*[@id="doto_login"]/div[3]/div[1]/form/div/input[3]').click()
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="dometopia_header"]/div[1]/div[2]/ul/li[6]/a').click()
    driver.switch_to.window(driver.window_handles[1])
    driver.get("http://dometopia.com/selleradmin/point/emoney_list?member_seq=&keyword=%ED%99%98%EB%B6%88&sdate=&edate=")
    html=driver.page_source
    soup=BeautifulSoup(html,'html.parser')
    for number in range(1,51):
        for j in soup.select('#layout-body > table.list-table-style > tbody > tr:nth-child('+str(number)+') > td:nth-child(3)'):
            pass
        for k in soup.select('#layout-body > table.list-table-style > tbody > tr:nth-child('+str(number)+') > td:nth-child(4)'):
            pass
        for i in soup.select('#layout-body > table.list-table-style > tbody > tr:nth-child('+str(number)+') > td:nth-child(6)'):
            sql="insert into refund(name,numb,price) values (%s, %s, %s);"
            conn=connection()
            curs=conn.cursor()
            curs.execute(sql,(j.text,i.text,k.text))
            conn.commit()
            conn.close()


    driver.close()
    driver.switch_to.window(driver.window_handles[0])
            
 
    return "ok"

@app.route('/refundpage',methods=['get','post'])
def refundpage():
    if 'name' in session:
        if session['name']!='test2':
            return render_template('fail.html')
        pass
    else:
        return render_template('fail.html')
    conn=connection()
    curs=conn.cursor()
    sql="select * from refund"
    curs.execute(sql)
    rows=curs.fetchall()
    data_list=[]
    for obj in rows:
        data_dic={
            'name' : obj[0],
            'numb' : obj[1],
            'price' : obj[2]
        }
        data_list.append(data_dic)
    conn.close()
    return render_template('refund.html',datalist=data_list)

@app.route('/qapage',methods=['get','post'])
def qapage():
    if 'name' in session:
        if session['name']!='test2':
            return render_template('fail.html')
        pass
    else:
        return render_template('fail.html')
    if request.method=="POST":
        idname=request.form['id']
        conn=connection()
        curs=conn.cursor()
        sql="select name,reply,datet,checkdata,customer,reply2 from qa where id=%s order by datet desc"
        curs.execute(sql,(idname))
        rows=curs.fetchall()
        data_list=[]
        for obj in rows:
            data_dic={
                'name' : obj[0],
                'reply' : obj[1],
                'datet' : obj[2],
                'checkdata' : obj[3],
                'customer' : obj[4],
                'reply2' : obj[5]
            }
            data_list.append(data_dic)
        conn.close()
        return render_template('qa.html',datalist=data_list)

    else:
        print("pass")
        return render_template('qa.html')

@app.route('/qacheck',methods=['get','post'])
def qacheck():
    name=request.form['cb']
    checkd="처리완료"
    print(id)
    print(name)
    sql="update qa set checkdata=%s where name=%s"
    conn=connection()
    curs=conn.cursor()
    curs.execute(sql,(checkd,name))
    conn.commit()
    conn.close()

    return redirect(request.referrer)

@app.route('/qadelete', methods=['get','post'])
def qadelete():
    ordername=request.form['dele']
    conn=connection()
    curs=conn.cursor()
    sql="delete from qa where name=%s"
    curs.execute(sql,(ordername))
    conn.commit()
    conn.close()

    return render_template('qa.html')

@app.route('/upload',methods=['get','post'])
def upload():
    if 'name' in session:
        pass
    else:
        return render_template('fail.html')
    if request.method=="POST":
        f=request.files['file']
        f.save(f'upload/{secure_filename(f.filename)}')
        return 'uplaod good'
    else:
        return render_template("upload.html")
    

@app.route('/qa',methods=['get','post'])
def qa():
    a=[]
    x=""
    b=""

    if getattr(sys, 'frozen', False):
        Chrome_path = os.path.join(sys._MEIPASS, "ChromeDriver.exe")
        driver = webdriver.Chrome(Chrome_path)
    else:
        driver=webdriver.Chrome()
    
    id="dorothy385"
    pw="zlqhem12"
    driver.get("https://www.dometopia.com/member/login")
    driver.find_element_by_name("userid").send_keys(id)
    driver.find_element_by_name("password").send_keys(pw)
    driver.find_element_by_xpath('//*[@id="doto_login"]/div[3]/div[1]/form/div/input[3]').click()
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="dometopia_header"]/div[1]/div[2]/ul/li[6]/a').click()
    driver.switch_to.window(driver.window_handles[1])
    driver.get('http://dometopia.com/selleradmin/board/board?id=mbqna')
    time.sleep(5)
    html=driver.page_source
    soup=BeautifulSoup(html,'html.parser')
    j=1
    for i in soup.select('#ajaxTable > tr > td:nth-child(6) > span'):
        for m in soup.select('#ajaxTable > tr:nth-child('+str(j)+') > td.date'):
            pass
        driver.find_element_by_xpath('//*[@id="ajaxTable"]/tr['+str(j)+']/td[6]/span').click()
        time.sleep(2)
        html=driver.page_source
        soup=BeautifulSoup(html,'html.parser')
        for xy in soup.select('#form1 > div.content > div:nth-child(4)'):
            x=xy.text
        for k in soup.select('.ml10'):
            a.append(k.text)
        for ka in soup.select('#form1 > div.content > p'):
            a.append(ka.text)
        for xyz in soup.select('.reply'):
            b=xyz.text
        #for ik in range(5,20):
            #for xyz in soup.select('#form1 > div.content > div:nth-child('+str(ik)+')'):
                #a.append(xyz.text)
            
        s=" ".join(a)
        conn=connection()
        curs=conn.cursor()
        sql="insert into qa(name,id,reply,datet,customer,reply2) select %s, %s, %s, %s, %s, %s from dual where NOT EXISTS(select * from qa where datet=%s)"
        curs.execute(sql,(i.text,id,s,m.text,x,b,m.text))
        conn.commit()
        conn.close()
        conn=connection()
        curs=conn.cursor()
        sql2="update qa set reply2=%s where name=%s and datet=%s and reply2 !=%s"
        curs.execute(sql2,(b,i.text,m.text,b))
        conn.commit()
        conn.close()
        a.clear()
        x=""
        driver.find_element_by_xpath('/html/body/div[12]/div[1]/a').click()
        j+=1
    driver.close()
    driver.switch_to.window(driver.window_handles[0])

    return "ok"

@app.route('/answer',methods=['get','post'])
def answer():
    id=request.form['id']
    title=request.form['title']
    content=request.form['content']
    kind=request.form['kind']
    ordertitle=request.form['ordertitle']
    f=request.files['file']
    f.save(f'upload/{secure_file(f.filename)}')

    if 'selling'==id:
        pw='tpfqudtls123!'
        if getattr(sys, 'frozen', False):
            Chrome_path = os.path.join(sys._MEIPASS, "ChromeDriver.exe")
            driver = webdriver.Chrome(Chrome_path)
        else:
            driver=webdriver.Chrome()

        driver.get("https://www.dometopia.com/member/login")
        driver.find_element_by_name("userid").send_keys(id)
        driver.find_element_by_name("password").send_keys(pw)
        driver.find_element_by_xpath('//*[@id="doto_login"]/div[3]/div[1]/form/div/input[3]').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="dometopia_header"]/div[1]/div[2]/ul/li[6]/a').click()
        driver.switch_to.window(driver.window_handles[1])
        driver.get('http://dometopia.com/selleradmin/board/board?id=mbqna')
        time.sleep(5)
        driver.find_element_by_xpath('//*[@id="boad_write_btn"]').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="issueOrdersButton"]').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="selectformdisplayOrdersSelect"]/div[1]/table/tbody/tr/td[1]/input').send_keys(ordertitle)
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="selectSearchButton"]').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="select_displayOrdersSelect"]').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="subject"]').send_keys(title)
        driver.find_element_by_xpath('//*[@id="tx_switchertoggle1"]/a').click()
        time.sleep(5)
        driver.find_element_by_xpath('//*[@id="tx_canvas_source1"]').send_keys(content)
        driver.find_element_by_xpath('//*[@id="tx_switchertoggle1"]/a').click()
        driver.find_element_by_xpath('//*[@id="addcategory"]/option['+str(kind)+']').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="data_save_btn"]').click()

        return "ok"
    else:
        return "ok"

if __name__=="__main__":
    app.secret_key='super secret key'
    app.config['SESSION-TYPE']='filesystem'
    app.run(host="0.0.0.0", port="5100")