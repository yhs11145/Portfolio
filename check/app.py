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
                'name' : obj[0],
                'checkin' : obj[1],
                'checkout' : obj[2],
                'check_explain' : obj[3]
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

@app.route('/checkin',methods=['POST','GET'])  ##근태관리
def checkin(): ##출근페이지
    if request.method=="POST":
        name=session['name']
        check_explain=request.form['explain']
        print(name,check_explain)
        conn=connection() ##출근도장 찍기
        curs=conn.cursor()
        sql="insert into checkinout (name,checkin,check_explain) values (%s,%s,%s)"
        curs.execute(sql,(name,datetime.datetime.now(),check_explain))
        conn.commit()
        conn.close()
        conn=connection()
        curs=conn.cursor()
        sql="select * from checkinout where name=%s"
        curs.execute(sql,(name))
        attends=curs.fetchall()
        data_list=[]
        for obj in attends:##DB출력
            data_dic={
                'name' : obj[0],
                'checkin' : obj[1],
                'checkout' : obj[2],
                'check_explain' : obj[3]
            }
            data_list.append(data_dic)
        conn.close()
        return render_template('atted.html',status_result='success',name=name,data_list=data_list)
    else:
        return render_template('atted.html',status_result='fail')
    
@app.route('/checkout',methods=['POST','GET'])
def checkout(): ##퇴근페이지
    if request.method=="POST":
        name=session['name']
        conn=connection()
        curs=conn.cursor()
        sql="update checkinout set checkout=%s where name=%s"##퇴근시간 찍기
        curs.execute(sql,(datetime.datetime.now(),name))
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
                'name' : obj[0],
                'checkin' : obj[1],
                'checkout' : obj[2],
                'check_explain' : obj[3]
            }
            data_list.append(data_dic)
        conn.close()
        return render_template('atted.html',name=name,data_list=data_list)
    
if __name__=="__main__":
    app.secret_key='super secret key'
    app.config['SESSION-TYPE']='filesystem'
    app.run(host="0.0.0.0", port="5200")