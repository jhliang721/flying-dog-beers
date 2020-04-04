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
    #根据页面获取数据
    def get_page(page):
        weiboaccount = {
            "containerid":"1076031764276651",
            "page_type":"03",
            "page":page
        }
        response=requests.get(base_url + urlencode(weiboaccount))
#         print(urlencode(weiboaccount))
#         print(response.json())
        return response.json()
    
    #解析数据
    def print_data(res_json):  
        print(res_json)
    
    def main():
        #从1-10页，执行请求，获取数据，解析、打印数据
        for page in range (1,5):
            res_json=get_page(page)
            print_data(res_json)
    if __name__=='__main__':
        main()
    
    return 'Finish！'
