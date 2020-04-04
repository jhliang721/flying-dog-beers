#-*- coding:utf-8 -*-
import sys
import requests
import pandas
import numpy
import plotly.graph_objs as go
import pprint
import json
from urllib.parse import urlencode
from flask import Flask
from pyquery import PyQuery
    
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
    def crawl_data(res_json):
        if res_json.get["data"]:
            for weibo_content in res_json["data"]["cards"]:
                item=dict()
                item["id"] = item["mblog"]["id"]
                item["user_name] = weibo_content["mblog"]["user"]["screen_name"]
                item["text]=PyQuery(weibo_content["mblog"]["text"]).text()
                item["comments_count] = weibo_content["mblog"]["comments_count"]
                item["reposts_count] = weibo_content["mblog"]["reposts_count"]
                item["attitudes_count] = weibo_content["mblog"]["attitudes_count"]
                print(item)
    #             write into json or csv etc
    #             with open(file="WeiboResult.json",mode = "a+", encoding="utf-8") as f:
    #                  f.write(json.dumps(item))
    
    def main():
        #从1-4页，执行请求，获取数据，解析、打印数据
        for page in range (1,5):
            res_json = get_page(page)
            crawl_data(res_json)
            
    if __name__=='__main__':
        result = main()
    
    return '<div>' + result.to_html(classes='tbstyle') + '</div>'
