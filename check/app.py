from flask import Flask,render_template,request,flash,request,url_for,redirect,session
import pymysql
import sys,os,time
import json
app=Flask(__name__)

@app.route('/',methods=['POST', 'GET'])
def index():
    return 'test'
    
if __name__=="__main__":
    app.secret_key='super secret key'
    app.config['SESSION-TYPE']='filesystem'
    app.run(host="0.0.0.0", port="5200")