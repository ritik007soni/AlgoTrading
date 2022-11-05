import  numpy as np
import  pandas as pd
import requests
import math
import xlsxwriter
from secret import  IEX_CLOUD_API_TOKEN

#Reading stocks data
stocks = pd.read_csv("sp_500_stocks.csv")
#print(stocks)

'''Making our first call to the api
   we need following info from the api
   1. Market capitalization for each stock
   2. Price of each stock'''
symbol = 'AAPL'
apiUrl = f'https://sandbox.iexapis.com/stable/stock/{symbol}/quote/?token={IEX_CLOUD_API_TOKEN}'
'''
#print(apiUrl)
data = requests.get(apiUrl)
print(type(data))
print(data.status_code)
'''
#The data in the above code is not usefull, so we need to convert it into a json file to be able to read the info retrived by api object i.e data
data = requests.get(apiUrl).json()
print(data)


'''Parsing our api
    The api call we made in the above code conatians all the information.
    We need to parse it to properly formate it'''
price = data['latestPrice']
marketCap = data['marketCap']
#print(price,marketCap)


'''Adding our data to pandas dataframe'''
myCol = ["Ticker","Stock Prize","Market Capitalization","Number of shares to buy"]
finalDataFrame = pd.DataFrame(columns=myCol)

finalDataFrame.append(
    pd.Series([
        symbol,
        price,
        marketCap,
        'N/A'
    ],
        index=myCol
    ),
        ignore_index=True
)
print(finalDataFrame)