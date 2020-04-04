import sys
import requests
import pandas
import numpy
import plotly.graph_objs as go

from flask import Flask
    
app = Flask(__name__)

@app.route('/')
def testweibocrawling():
# gary's weibo account
# https://m.weibo.cn/api/container/getIndex?uid=1764276651&luicode=10000011&lfid=100103type%3D1%26q%3Dkawaaaaaaaa&containerid=1076031764276651&since_id=4079234580721927
base_url='https://m.weibo.cn/api/container/getIndex?'
response=requests.get
