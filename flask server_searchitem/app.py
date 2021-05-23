from flask import Flask,render_template
from flask.wrappers import Response
import requests
from bs4 import BeautifulSoup


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('admin.html')
    
@app.route('/info')
def info():
    return 'Info'

@app.route('/search')
def search():
    search="마스크"
    values={
          'query': search
          }
    response=requests.get('https://shopping.naver.com/search/all?',params=values)##네이버
    print(response.url)
    soup=BeautifulSoup(response.text,"html.parser")
    return soup.text


if __name__=="__main__":
    app.run(host="0.0.0.0", port="5100")