import sys
import requests
import pandas
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    articles = []
    for i in range(1,2):
        res = requests.get('https://m.weibo.cn/api/container/getIndex?containerid=231522type%3D1%26q%3D%23%E9%A6%99%E5%A5%88%E5%84%BF%23&page_type=searchall&page={}'.format(i))
    jd = res.json()
    articles.extend( [rec['mblog'] for rec in jd['data']['cards'] if rec.get('mblog')] )
    df = pandas.DataFrame(articles)
    print(len(df))
    print(jd)
    return 'Hello, World!'


