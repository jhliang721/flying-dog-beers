import sys

import requests
import pandas

res = requests.get('https://m.weibo.cn/api/container/getIndex?containerid=231522type%3D1%26q%3D%23%E9%A6%99%E5%A5%88%E5%84%BF%23&page_type=searchall&page=3')
jd = res.json()
articles = [rec['mblog'] for rec in jd['data']['cards'] if rec.get('mblog')]
df = pandas.DataFrame(articles)
df['text']

articles = []
for i in range(1,10):
    res = requests.get('https://m.weibo.cn/api/container/getIndex?containerid=231522type%3D1%26q%3D%23%E9%A6%99%E5%A5%88%E5%84%BF%23&page_type=searchall&page={}'.format(i))
    jd = res.json()
    articles.extend( [rec['mblog'] for rec in jd['data']['cards'] if rec.get('mblog')] )
df = pandas.DataFrame(articles)
print(len(df))
df.to_excel(r'caroltest.xlsx',index=False)
print("done for the carol testing!!!!")
