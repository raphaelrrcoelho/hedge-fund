import numpy as np
import pandas as pd

def tickers(file='database.xlsx'):
	return pd.read_excel(file, sheet_name='Tickers').set_index('ticker')

def get_data(file='database.xlsx'):
	adj_close_prices = pd.read_excel(file, sheet_name='Adj Close Prices')
	close_prices = pd.read_excel(file, sheet_name='Close Prices')
	simple_returns = pd.read_excel(file, sheet_name='Simple Returns')
	cc_returns = pd.read_excel(file, sheet_name='CC Returns')
	
	return adj_close_prices, close_prices, simple_returns, cc_returns

def save_data(tickers, adj_close_prices, close_prices, simple_returns, cc_returns, file='database.xlsx'):
	writer = pd.ExcelWriter(file)
	
	tickers.to_excel(writer, 'Tickers')
	adj_close_prices.to_excel(writer, 'Adj Close Prices')
	close_prices.to_excel(writer, 'Close Prices')
	simple_returns.to_excel(writer, 'Simple Returns')
	cc_returns.to_excel(writer, 'CC Returns')
	
	writer.save()

def get_holidays(file='br_holidays.csv'):
	return pd.read_csv(file, header=None).values[0]
