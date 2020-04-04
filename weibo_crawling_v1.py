import sys
import requests
import pandas
import numpy
import plotly.graph_objs as go
import pprint
from urllib.parse import urlencode
from flask import Flask
    
app = Flask(__name__)

@app.route('/')
def weibo_api_crawling():
    # gary's weibo account
    # https://m.weibo.cn/api/container/getIndex?uid=1764276651&luicode=10000011&lfid=100103type%3D1%26q%3Dkawaaaaaaaa&containerid=1076031764276651&since_id=4079234580721927
    base_url='https://m.weibo.cn/api/container/getIndex?'
    
    #请求的方法
    def get_page(page):
        weiboaccount = {
            "containerid":"1076031764276651",
            "page_type":"03",
            "page":page
        }
        response=requests.get(base_url + urlencode(weiboaccount))
        print(urlencode(weiboaccount))
        print(response.json())
        pprint.pprint(response.json())
    get_page(4)
    return 'Finish'
