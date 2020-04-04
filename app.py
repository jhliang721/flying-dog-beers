import sys
import requests
import pandas
import dash
import dash_core_components as dcc
import dash_html_components as html
import numpy
import plotly.graph_objs as go

from flask import Flask
    
app1 = Flask(__name__)

@app1.route('/')
def testweibocrawling():
    articles = []
    for i in range(1,15):
        res = requests.get('https://m.weibo.cn/api/container/getIndex?containerid=231522type%3D1%26q%3D%23%E9%A6%99%E5%A5%88%E5%84%BF%23&page_type=searchall&page={}'.format(i))
    jd = res.json()
    articles.extend( [rec['mblog'] for rec in jd['data']['cards'] if rec.get('mblog')] )
    df = pandas.DataFrame(articles)
    print(len(df))
    a=len(df)
    pandas.set_option('max_colwidth',500)
    pandas.DataFrame(df)
    print(df.loc[1:a, ['id','text']])
    df1=df.loc[1:a, ['id','text']]
    return '<div>' + df1.to_html(classes='tbstyle') + '</div>'

