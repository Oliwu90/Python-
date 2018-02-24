#Python: Bitcoin Pricing With 10 Moving Average Days

import requests
res=requests.get('https://www.coingecko.com/zh-tw/%E5%8C%AF%E7%8E%87%E5%9C%96/%E6%AF%94%E7%89%B9%E5%B9%A3/usd')
#res to test 
from bs4 import BeautifulSoup as bs
soup = bs(res.text, 'html.parser')

type(soup.select('#coin_portfolio_price_chart_btc')[0])
# type as bs4.element.Tag

data_prices = soup.select('#coin_portfolio_price_chart_btc')[0].prettify('utf-8').decode('utf-8')
# covert to str

import re 
clean = re.search('div class="coin_portfolio_price_chart" data-prices="(.*?)"',data_prices)

import json
jd = json.loads(clean.group(1))
# jd were converted to dictionary

import pandas 
df = pandas.DataFrame(jd)

df.columns = ['DateTime', 'USD']
df.head()
df['DateTime']=pandas.to_datetime(df['DateTime'],unit='ms')
df.head()

df.index = df['DateTime']

get_ipython().magic('pylab inline')
df['USD'].plot(kind= 'line', figsize = [10,7])

df['Moving Average 10'] = df['USD'].rolling(window=10).mean()

df[['USD','Moving Average 10']].plot(kind = 'line', figsize=[10,7])

