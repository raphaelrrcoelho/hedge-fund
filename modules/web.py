import numpy as np
import pandas as pd
from pandas.tseries.offsets import CustomBusinessDay
import pandas_datareader.data as web
import quandl

def stocks(tickers, start, end, how='yahoo_first'):
	stock_data = {}
    
	for ticker in tickers.index.tolist():
		try:
			stock_data[ticker] = get_from_yahoo(ticker + '.SA', start, end)
		except:
			print(ticker)
	
	stock_data = pd.Panel.from_dict(stock_data)
	stock_data = stock_data.loc[ tickers.index.tolist() ]
	
	stock_data['ibov'] = get_from_yahoo('^BVSP', start, end)
	stock_data['ibrx'] = get_from_yahoo('^IBX50', start, end)
	return stock_data

def risk_free(start, end, date_index):
    # Get CDI Daily Rate
    risk_free = quandl.get("BCB/12", trim_start=start, trim_end=end)
    risk_free.name = 'risk_free'
    risk_free.rename(columns={'Value': 'cdi'}, inplace=True)

    return risk_free.ix[date_index, :].dropna() / 100

def get_from_yahoo(ticker, start, end):
    return web.DataReader(ticker, 'yahoo', start, end)

# def get_from_google(ticker, start, end):
#     data = web.DataReader(ticker, 'google', start, end)
#     data['Adj Close'] = data['Close']
# 
#     return data
