from flask import Flask,render_template,request,flash,request,url_for,redirect,session
import pymysql
import sys,os,time
import json
import datetime
app=Flask(__name__)

def connection():
    return pymysql.connect(host='localhost',port=3306,user='selling',passwd='122919',db='sys',charset='utf8')

@app.route('/',methods=['POST', 'GET'])
def index():#메인홈페이지
    if request.method=='POST':
        id=request.form['id']
        password=request.form['password']
        conn=connection()##로그인값 DB로부터 가져오기
        curs=conn.cursor()
        sql="select name,id,password from useradmin where id=%s and password=%s"##쿼리
        curs.execute(sql,(id,password))#DB 가져오기
        rows=curs.fetchall()
        print(rows)
        ##근태관리 페이지 게시판 가져오기
        sql="select * from checkinout where name=%s"
        curs.execute(sql,(rows[0][0]))
        attends=curs.fetchall()
        data_list=[]
        for obj in attends:##게시판 DB가져오기
            data_dic={
                'date' : obj[0],
                'name' : obj[1],
                'checkin' : obj[2],
                'checkout' : obj[3],
                'check_explain' : obj[4]
            }
            data_list.append(data_dic)
        conn.close()
        print(data_list)
        for row in rows:##아이디 비밀번호 비교
            if id==row[1] and password==row[2]:
                session['name']=row[0]
                return render_template('atted.html',name=row[0],data_list=data_list)
                #return redirect(url_for('user',idname=row[0]))
            else:
                return render_template('fail.html')
        return render_template('fail.html')
    else:
        return render_template('login.html')

@app.route('/join',methods=['POST','GET'])    ##회원가입페이지
def join():
    if request.method=='POST':
        name=request.form['name']##form 가져오기
        id=request.form['id']
        password=request.form['password']
        conn=connection()
        curs=conn.cursor()
        sql="select id from useradmin where id=%s"
        curs.execute(sql,(id))
        rows=curs.fetchall()
        conn.close()
        for row in rows:
            if id==row[0]:##중복체크
                return render_template('join.html',id="No")
        if len(id)>0 and len(password)>0:##새로 가입  글자수로 제한
            print(id,password)
            conn=connection()
            curs=conn.cursor()
            sql="insert into useradmin (name,id,password) values (%s, %s,%s)"
            curs.execute(sql,(name,id,password))
            conn.commit()
            conn.close()
            return render_template('join.html',id='ok')
        else: ##아이디/비밀번호 제한
            return render_template('join.html',id='retry')
        
    return render_template('join.html',id='None')##처음 접속시

@app.route('/check',methods=['POST','GET'])  ##근태관리
def check(): ##출근페이지
    if request.method=="POST":
        name=session['name']
        if request.form['checkin']=='출근하기': ##출근도장 찍을때  
            check_explain=request.form['explain']
            try:
                conn=connection() ##출근도장 찍기
                curs=conn.cursor()
                sql="insert into checkinout (date,name,checkin,check_explain) values (%s,%s,%s,%s)"
                curs.execute(sql,(time.strftime('%y-%m-%d',time.localtime(time.time())),name,datetime.datetime.now(),check_explain))
                conn.commit()
                conn.close()
                conn=connection()
                curs=conn.cursor()
            except: ##출근확인 오류
                sql="select * from checkinout where name=%s"
                curs.execute(sql,(name))
                attends=curs.fetchall()
                data_list=[]
                for obj in attends:##DB출력
                    data_dic={
                        'date' : obj[0],
                        'name' : obj[1],
                        'checkin' : obj[2],
                        'checkout' : obj[3],
                        'check_explain' : obj[4]
                    }
                    data_list.append(data_dic)
                return render_template('atted.html',name=name,status_result='fail',data_list=data_list)
            sql="select * from checkinout where name=%s"
            curs.execute(sql,(name))
            attends=curs.fetchall()
            data_list=[]
            for obj in attends:##DB출력
                data_dic={
                    'date' : obj[0],
                    'name' : obj[1],
                    'checkin' : obj[2],
                    'checkout' : obj[3],
                    'check_explain' : obj[4]
                }
                data_list.append(data_dic)
            conn.close()
            return render_template('atted.html',status_result='success',name=name,data_list=data_list)
        elif request.form['checkin']=='퇴근하기':
            conn=connection()
            curs=conn.cursor()
            sql="update checkinout set checkout=%s where name=%s and date=%s"##퇴근시간 찍기
            curs.execute(sql,(datetime.datetime.now(),name,time.strftime('%y-%m-%d',time.localtime(time.time()))))
            conn.commit()
            conn.close()
            conn=connection()
            curs=conn.cursor()
            sql="select * from checkinout where name=%s"##DB출력
            curs.execute(sql,(name))
            attends=curs.fetchall()
            data_list=[]
            for obj in attends:##게시판 DB가져오기
                data_dic={
                    'date' : obj[0],
                    'name' : obj[1],
                    'checkin' : obj[2],
                    'checkout' : obj[3],
                    'check_explain' : obj[4]
                }
                data_list.append(data_dic)
            conn.close()
            return render_template('atted.html',name=name,data_list=data_list)
    else:
        return render_template('atted.html',name=name,status_result='fail')
    
@app.route('/admin',methods=['POST','GET']) ##관리자페이지 접속 및 관리
def admin():
    if request.method=="POST":##관리자페이지 로그인
        id=request.form['id']
        password=request.form['password']
        conn=connection()##로그인값 DB로부터 가져오기
        curs=conn.cursor()
        sql="select id,pw from admin where id=%s and pw=%s"##쿼리
        curs.execute(sql,(id,password))#DB 가져오기
        rows=curs.fetchall()
        print(rows)
        conn=connection()
        curs=conn.cursor()
        sql="select * from checkinout"
        curs.execute(sql)
        check=curs.fetchall()
        data_list=[]
        for obj in check:##게시판 DB가져오기
            data_dic={
                'date' : obj[0],
                'name' : obj[1],
                'checkin' : obj[2],
                'checkout' : obj[3],
                'check_explain' : obj[4]
            }
            data_list.append(data_dic)
        conn.close()
        for row in rows:##아이디 비밀번호 비교
            if id==row[0] and password==row[1]:
                session['name']=row[0]
                return render_template('admin.html',name=row[0],data_list=data_list)
                #return redirect(url_for('user',idname=row[0]))
            else:
                return render_template('fail.html')
        return render_template('fail.html')
    
    return render_template('adminlogin.html',id='None')##처음 접속시

@app.route('/admincontrol',methods=['GET','POST'])
def admincontrol():
    if request.method=="POST":##관리자가 초기화할 대상 선정.
        name=session['name']
        date=request.form['date']
        dataname=request.form['name']
        if request.form['submit']=='출근시간 초기화':
            conn=connection()
            curs=conn.cursor()
            sql="update checkinout set checkin=NULL where name=%s and date=%s"
            curs.execute(sql,(dataname,date))
            conn.commit()
            conn.close()
            conn=connection()
            curs=conn.cursor()
            sql="select * from checkinout"
            curs.execute(sql)
            check=curs.fetchall()
            data_list=[]
            for obj in check:##게시판 DB가져오기
                data_dic={
                    'date' : obj[0],
                    'name' : obj[1],
                    'checkin' : obj[2],
                    'checkout' : obj[3],
                    'check_explain' : obj[4]
                }
                data_list.append(data_dic)
            conn.close()
            return render_template('admin.html',name=name,data_list=data_list)
        elif request.form['submit']=='퇴근시간 초기화':
            conn=connection()
            curs=conn.cursor()
            sql="update checkinout set checkout=NULL where name='%s' and date='%s'"
            curs.execute(sql,(name,date))
            conn.commit()
            conn.close()
            conn=connection()
            curs=conn.cursor()
            sql="select * from checkinout"
            curs.execute(sql)
            check=curs.fetchall()
            data_list=[]
            for obj in check:##게시판 DB가져오기
                data_dic={
                    'date' : obj[0],
                    'name' : obj[1],
                    'checkin' : obj[2],
                    'checkout' : obj[3],
                    'check_explain' : obj[4]
                }
                data_list.append(data_dic)
            conn.close()
            return render_template('admin.html',name=name,data_list=data_list)
    
if __name__=="__main__":
    app.secret_key='super secret key'
    app.config['SESSION-TYPE']='filesystem'
    app.run(host="0.0.0.0", port="5200")