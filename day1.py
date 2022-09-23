# -*- coding: utf-8 -*-
import requests

url = "https://searchapi.eastmoney.com/api/HotKeyword/GetBatch"
params = {
    # "cb": "jQuery351011081548002204444_1656903750005",
    "count": "20",
    "stockCount": "30",
    "token": "D43BF722C8E33BDC906FB84D85E326E8",
    "_": "1656903750011"
}
headers = {
    "Mozilla/5.0": "(Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                   "(KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
}

response = requests.get(url, params=params, headers=headers)
stock_list = response.json().get('Data').get('Stock')
print(stock_list)
for stock in stock_list[:10]:
    stock_code = stock.get('Code', '')
    print(stock_code)


""" 测试"""

