import yfinance as yf
import datetime 

tickers_list = {
    'AAPL': 'Apple',
    'MSFT': 'Microsoft',
    'AMZN': 'Amazon',
    'GOOGL': 'Google',
    'FB': 'Facebook',
    'TSLA': 'Tesla',
    'BABA': 'Alibaba',
    'TSM': 'Taiwan Semiconductor',
    'BRK.A': 'Berkshire Hathawa',
    'MA': '	Mastercard',
    'WMT': 'Walmart',
    'DIS': 'Disney',
    'NVDA': 'NVIDIA',
    'PYPL': 'PayPal',
    'NFLX': 'Netflix',
    'NKE': 'Nike',
    'ADBE': 'Adobe',
    'KO': 'Coca-Cola',
    'ORCL': 'Oracle',
    'PFE': 'Pfizer'
} 

end = datetime.datetime(2021,3,14) 
start = datetime.datetime(2013,1,30) 
Amazon = yf.Ticker("NKE") 
print(Amazon.history(start=start, end=end))
