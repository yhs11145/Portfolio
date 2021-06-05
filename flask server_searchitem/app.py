from flask import Flask,render_template,request,flash,request,url_for,redirect,session
from flask.wrappers import Response
import requests
import sys,os,time
from bs4 import BeautifulSoup


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('admin.html')
    
@app.route('/info')
def info():
    return 'Info'

@app.route('/search',methods=['POST', 'GET'])
def search():
    if request.method=='POST':
        search=request.form['search']
        values={
            'query': search
            }
        response=requests.get('https://shopping.naver.com/search/all?',params=values)##네이버
        print(response.url)
        soup=BeautifulSoup(response.text,"html.parser")
        for name in soup.select('.basicList_title__3P9Q7'):
            print(name.text.strip())
        for price in soup.select('.price_num__2WUXn'):
            print(price.text.strip())
        return response.text


if __name__=="__main__":
    app.run(host="0.0.0.0", port="5100")