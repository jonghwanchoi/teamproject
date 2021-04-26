from flask import Flask, request, jsonify
from flask import render_template
from selectDB import select_DB #송이씨 코드보고 클래스화
import math

tabledic = {"1":"tempTable", "2":"testTable"}
htmlList =['temp/home.html', 'temp/list.html', 'temp/list_paging.html','test.html']

arduinoDB = select_DB("./arduinoDB.db", tabledic["1"]) # select_DB 클래스를 이용해 arduinoDB라는 객체 생성
testDB = select_DB("./testDB.db", tabledic["2"])

app = Flask(__name__)

@app.route('/')
def home():
    return render_template(htmlList[0])

@app.route('/test')
def testpage():
    list = testDB.select()
    return render_template(htmlList[3], list = list)

@app.route('/list')
def list_all():
    list = arduinoDB.select()
    return render_template(htmlList[1], list=list)

@app.route('/list/<int:page>')
def list_pages(page):
    list_num = 5
    list_count = testDB.select_count("idx")
    # page_count = int(list_count / list_num)
    page_count = math.ceil(list_count/list_num)
    list = testDB.select_page(list_num, page, "idx")
    return render_template(htmlList[2], list=list, page_count=page_count)

@app.route('/delete')
def renew():
    list = testDB.delete()
    return render_template(htmlList[3], list=list)

if __name__ == "__main__":
    app.run(host="localhost")