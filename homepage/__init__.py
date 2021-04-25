from flask import Flask, request, jsonify
from flask import render_template
from selectDB import select, delete, select_count, select_page
import math


app = Flask(__name__)

@app.route('/')
def home():
    return "welcome"

@app.route('/list')
def list_all():
    list = select()
    return render_template('temp/list.html', list=list)

@app.route('/list/<int:page>')
def list_pages(page):
    list_num = 5
    list_count = select_count()
    # page_count = int(list_count / list_num)
    page_count = math.ceil(list_count/list_num)
    list = select_page(list_num, page)
    return render_template('temp/list_paging.html', list=list, page_count=page_count)

@app.route('/delete')
def renew():
    list = delete()
    return render_template('temp/list.html', list=list)

if __name__ == "__main__":
    app.run(host="localhost")