from flask import Flask, request, jsonify
from flask import render_template
from selectDB import select_DB #송이씨 코드보고 클래스화
import math

db = select_DB("./arduinoDB.db", "./testDB.db")

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('temp/home.html')

@app.route('/test')
def testpage():
    list = db.selectTest()
    return render_template('test.html', list = list)

@app.route('/list')
def list_all():
    list = db.select()
    return render_template('temp/list.html', list=list)

@app.route('/list/<int:page>')
def list_pages(page):
    list_num = 5
    list_count = db.select_count()
    # page_count = int(list_count / list_num)
    page_count = math.ceil(list_count/list_num)
    list = db.select_page(list_num, page)
    return render_template('temp/list_paging.html', list=list, page_count=page_count)

@app.route('/delete')
def renew():
    list = db.delete()
    return render_template('temp/list.html', list=list)

if __name__ == "__main__":
    app.run(host="localhost")