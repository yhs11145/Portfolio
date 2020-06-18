import pymysql
 
# database에 접근
db= pymysql.connect(host='localhost',
                     port=3306,
                     user='root',
                     passwd='122919',
                     db='sys',
                     charset='utf8')
 
# database를 사용하기 위한 cursor를 세팅합니다.
cursor= db.cursor()
 
# SQL query 작성
sql= """CREATE TABLE user(
         id  varchar(80) NOT NULL  PRIMARY KEY,
         pw VARCHAR(256) NOT NULL
         );"""
 
# SQL query 실행
cursor.execute(sql)
 
# SQL query가 잘 실행됐는지 table을 살펴보도록 합니다.
# 이미 4번 라인에서 use database를 수행한 것과 다름 없으니 show tables라는 명령을 수행해도 문제가 없습니다.
cursor.execute("show tables")
 
# 데이터 변화 적용
# CREATE 혹은 DROP, DELETE, UPDATE, INSERT와 같이 Database 내부의 데이터에 영향을 주는 함수의 경우 commit()을 해주어야 합니다.
db.commit()
 
# Database 닫기
db.close()