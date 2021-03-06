from flask import Flask,render_template,request,flash,request,url_for,redirect,session
import pymysql
import sys,os,time
import json
import datetime
from slacker import Slacker

if getattr(sys, 'frozen', False):
    template_folder = os.path.join(sys._MEIPASS, 'templates')
    static_folder = os.path.join(sys._MEIPASS, 'static')
    app = Flask(__name__, template_folder=template_folder,static_folder=static_folder)
else:
    app = Flask(__name__)

##함수선언
def slack_data(ordermessage):
    token="xoxb-1017448255248-1176108620737-4kNkImbnfhiKOBKWLQNtZGG6"
    slack=Slacker(token)
    slack.chat.post_message('#pythonmessage',ordermessage)
    
def DB_connection(attr):
    data_list=[]
    for obj in attr:##DB출력
        data_dic={
            'date' : obj[0],
            'name' : obj[1],
            'checkin' : obj[2],
            'checkout' : obj[3],
            'worktime' : obj[4],
            'check_explain' : obj[5]
        }
        data_list.append(data_dic)
    return data_list
    
def worktime(attr):
    data_list=[]
    for obj in attr:
        data_dic={
            'name' : obj[0],
            'time' : obj[1],
            'count' : obj[2]
        }
        data_list.append(data_dic)
    return data_list

def checkname(attr):
    data_list=[]
    for obj in attr:
        data_dic={
            'name' : obj[0]
        }
        data_list.append(data_dic)
    return data_list

def connection():
    return pymysql.connect(host='localhost',port=3306,user='selling',passwd='122919',db='sys',charset='utf8')

##페이지 경로
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
        conn.close()
        print(rows)
        for row in rows:##아이디 비밀번호 비교
            if id==row[1] and password==row[2]:
                session['name']=row[0]
                conn=connection()
                curs=conn.cursor()
                sql="select * from checkinout where name=%s"##근태관리 페이지 게시판 가져오기
                curs.execute(sql,(row[0]))
                attends=curs.fetchall()
                data_list=DB_connection(attends)
                conn.close()
                print(data_list)
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
            sql="insert into useradmin (name,id,password) values (%s, %s,%s)"##사용자DB 등록
            curs.execute(sql,(name,id,password))
            sql="insert into worktime (name,time,count) values (%s,0,0)"##총업무시간DB 등록
            curs.execute(sql,(name))
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
                curs.execute(sql,(time.strftime('%Y-%m-%d',time.localtime(time.time())),name,datetime.datetime.now().strftime('%H:%M:%S'),check_explain))
                slack_data(name+'출근완료 업무내용: '+check_explain)
                conn.commit()
            except: ##출근확인 오류 ( 경고문 띄어주고 다시 리스트 출력)
                sql="select * from checkinout where name=%s"
                curs.execute(sql,(name))
                attends=curs.fetchall()
                data_list=DB_connection(attends)
                conn.close()
                return render_template('atted.html',name=name,status_result='fail',data_list=data_list)
            sql="select * from checkinout where name=%s"
            curs.execute(sql,(name))
            attends=curs.fetchall()
            data_list=DB_connection(attends)
            conn.close()
            return render_template('atted.html',status_result='success',name=name,data_list=data_list)
        elif request.form['checkin']=='퇴근하기':
            conn=connection()
            curs=conn.cursor()
            sql="update checkinout set checkout=%s where name=%s and date=%s"##퇴근시간 찍기
            curs.execute(sql,(datetime.datetime.now().strftime('%H:%M:%S'),name,time.strftime('%Y-%m-%d',time.localtime(time.time()))))
            conn.commit()
            sql='select checkin,checkout from checkinout where name=%s and date=%s'##출근시간 퇴근시간 가져오기##업무시간 계산하기
            curs.execute(sql,(name,time.strftime('%Y-%m-%d',time.localtime(time.time()))))
            rows=curs.fetchall()
            for row in rows:##퇴근시간-출근시간
                worktime=row[1]-row[0]
            sql='update checkinout set worktime=%s where name=%s and date=%s'##업무시간 업데이트
            curs.execute(sql,(worktime,name,time.strftime('%Y-%m-%d',time.localtime(time.time()))))
            conn.commit()
            slack_data(name+'퇴근완료')##슬랙연동
            sql='select worktime from checkinout where name=%s'
            curs.execute(sql,(name))
            sumtimes=curs.fetchall()
            timeset=datetime.timedelta(0,0,0)##총 업무시간 더하기
            for sumtime in sumtimes:
                timeset+=sumtime[0]
            sql="update worktime set time=%s where name=%s"
            curs.execute(sql,(timeset,name))
            conn.commit()
            sql="select * from checkinout where name=%s"##DB출력
            curs.execute(sql,(name))
            attends=curs.fetchall()
            data_list=DB_connection(attends)
            sql="select COUNT(name) from checkinout where name=%s" ##업무일수 DB 넣어주기
            curs.execute(sql,(name))
            count=curs.fetchall()
            sql="update worktime set count=%s where name=%s"
            curs.execute(sql,(count,name))
            conn.commit()
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
        sql="select * from checkinout"##전체 리스트
        curs.execute(sql)
        check=curs.fetchall()
        data_list=DB_connection(check)
        sql='select * from worktime' ##업무일수 및 시간
        curs.execute(sql)
        timedata=curs.fetchall()
        data_list2=worktime(timedata)
        sql="select name from worktime"##이름 가져오기
        curs.execute(sql)
        selectname=curs.fetchall()
        selectname=checkname(selectname)
        conn.close()
        for row in rows:##아이디 비밀번호 비교
            if id==row[0] and password==row[1]:
                session['name']=row[0]
                return render_template('admin.html',name=row[0],data_list=data_list,data_list2=data_list2,selectnames=selectname)
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
        conn=connection()##이름 가져오기
        curs=conn.cursor()
        sql="select name from worktime"
        curs.execute(sql)
        selectname=curs.fetchall()
        selectname=checkname(selectname)
        sql='select * from worktime' ##업무일수 및 시간
        curs.execute(sql)
        timedata=curs.fetchall()
        data_list2=worktime(timedata)
        conn.close()
        if request.form['submit']=='기록삭제':##해당 사용자 행 삭제
            conn=connection()
            curs=conn.cursor()
            sql="delete from checkinout where name=%s and date=%s"
            curs.execute(sql,(dataname,date))
            conn.commit()
            sql="select * from checkinout"
            curs.execute(sql)
            check=curs.fetchall()
            data_list=DB_connection(check)
            conn.close()
            return render_template('admin.html',name=name,data_list=data_list,data_list2=data_list2,selectnames=selectname)
        elif request.form['submit']=='출근시간 수정': ##출근시간 수정
            checkin=request.form['checkin'] ##수정할 시간 가져오기
            conn=connection()
            curs=conn.cursor()
            sql="update checkinout set checkin=%s where name=%s and date=%s" ##업데이트
            curs.execute(sql,(checkin,dataname,date))
            conn.commit()
            sql="select * from checkinout"
            curs.execute(sql)
            check=curs.fetchall()
            data_list=DB_connection(check)
            conn.close()
            return render_template('admin.html',name=name,data_list=data_list,data_list2=data_list2,selectnames=selectname)
        elif request.form['submit']=='퇴근시간 초기화': ##퇴근시간 초기화 (인정안할경우
            conn=connection()
            curs=conn.cursor()
            sql="update checkinout set checkout=NULL where name=%s and date=%s"
            curs.execute(sql,(dataname,date))
            conn.commit()
            sql="select * from checkinout"
            curs.execute(sql)
            check=curs.fetchall()
            data_list=DB_connection(check)
            conn.close()
            return render_template('admin.html',name=name,data_list=data_list,data_list2=data_list2,selectnames=selectname)
        elif request.form['submit']=='조회하기':##조회하기 기능
            conn=connection()
            curs=conn.cursor()
            sql="select * from checkinout where date=%s and name=%s"
            curs.execute(sql,(date,dataname))
            search=curs.fetchall()
            data_list=DB_connection(search)
            conn.close()
            return render_template('admin.html',name=name,data_list=data_list,data_list2=data_list2,selectnames=selectname)

@app.route('/reply',methods=["GET",'POST'])
def reply():
    name=session['name']##문의내용 보내기
    if request.method=="POST":
        replyanswer=request.form['replyanswer']
        slack_data('문의자 : '+name+' 문의내용 :'+replyanswer)
        return redirect(url_for('index')) ##홈페이지로
    return render_template('reply.html',name=name)  ##문의하기 게시판이동

##실행    
if __name__=="__main__":
    from waitress import serve
    app.secret_key='super secret key'
    app.config['SESSION-TYPE']='filesystem'
    #app.run(host="0.0.0.0", port="5200")
    serve(app, host="0.0.0.0", port=5200)