from flask import Flask,render_template,request,flash,request,url_for,redirect,session
import pymysql
import sys,os,time
import json
app=Flask(__name__)

def connection():
    return pymysql.connect(host='localhost',port=3306,user='selling',passwd='122919',db='sys',charset='utf8')

@app.route('/',methods=['POST', 'GET'])
def index():#메인홈페이지
    if request.method=='POST':
        id=request.form['id']
        password=request.form['password']
        conn=connection()
        curs=conn.cursor()
        sql="select id,password from useradmin where id=%s and password=%s"
        curs.execute(sql,(id,password))
        rows=curs.fetchall()
        print(rows)
        conn.close()
        for row in rows:
            if id==row[0] and password==row[1]:
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
        if id is not None:##새로 가입
            conn=connection()
            curs=conn.cursor()
            sql="insert into useradmin (name,id,password) values (%s, %s,%s)"
            curs.execute(sql,(name,id,password))
            conn.commit()
            conn.close()
            return render_template('join.html',id='ok')
    return render_template('join.html',id='None')##처음 접속시

    
if __name__=="__main__":
    app.secret_key='super secret key'
    app.config['SESSION-TYPE']='filesystem'
    app.run(host="0.0.0.0", port="5200")