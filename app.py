import sys
import requests
import pandas
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

# res = requests.get('https://m.weibo.cn/api/container/getIndex?containerid=231522type%3D1%26q%3D%23%E9%A6%99%E5%A5%88%E5%84%BF%23&page_type=searchall&page=3')
# jd = res.json()
# articles = [rec['mblog'] for rec in jd['data']['cards'] if rec.get('mblog')]
# df = pandas.DataFrame(articles)
# df['text']

articles = []
for i in range(1,2):
    res = requests.get('https://m.weibo.cn/api/container/getIndex?containerid=231522type%3D1%26q%3D%23%E9%A6%99%E5%A5%88%E5%84%BF%23&page_type=searchall&page={}'.format(i))
    jd = res.json()
    articles.extend( [rec['mblog'] for rec in jd['data']['cards'] if rec.get('mblog')] )
df = pandas.DataFrame(articles)
print(len(df))
# df['text']
#df.to_csv(r'caroltest.csv',index=False)

# ########### Define your variables
# beers=['Chesapeake Stout', 'Snake Dog IPA', 'Imperial Porter', 'Double Dog IPA']
# ibu_values=[35, 60, 85, 75]
# abv_values=[5.4, 7.1, 9.2, 4.3]
# color1='lightblue'
# color2='darkgreen'
# mytitle='Beer Comparison'
# tabtitle='beer!'
# myheading='Flying Dog Beers'
# label1='IBU'
# label2='ABV'
# githublink='https://github.com/austinlasseter/flying-dog-beers'
# sourceurl='https://www.flyingdog.com/beers/'

# ########### Set up the chart
# bitterness = go.Bar(
#     x=beers,
#     y=ibu_values,
#     name=label1,
#     marker={'color':color1}
# )
# alcohol = go.Bar(
#     x=beers,
#     y=abv_values,
#     name=label2,
#     marker={'color':color2}
# )

# beer_data = [bitterness, alcohol]
# beer_layout = go.Layout(
#     barmode='group',
#     title = mytitle
# )

# beer_fig = go.Figure(data=beer_data, layout=beer_layout)


########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title=tabtitle

########### Set up the layout
# app.layout = html.Div(children=[
#     html.H1(myheading),
#     dcc.Graph(
#         id='flyingdog',
#         figure=beer_fig
    ),
#     html.A('Code on Github', href=githublink),
#     html.Br(),
#     html.A('Data Source', href=sourceurl),
    ]
)

app.layout = html.Div([
    html.H1('Hello Carol'),
    html.Div([
        html.P(df.to_string()),
        html.P('You are the best!!')
    ])
])

if __name__ == '__main__':
    app.run_server()


