import numpy, requests

baseURL = 'https://api.binance.com/api/v3/klines?'

def candles(symbol, interval, isClosed):
    limit = 101 if isClosed else 100  
    response = requests.get(f'{baseURL}symbol={symbol}&interval={interval}&limit={limit}')
    candles = response.json()  

    open_list = []
    for item in candles:
	    open_list.append(float(item[1]))
	    open = numpy.array(open_list) 

    high_list = []
    for item in candles:
	    high_list.append(float(item[2]))
	    high = numpy.array(high_list)

    low_list = []
    for item in candles:
	    low_list.append(float(item[3]))
	    low = numpy.array(low_list)

    close_list = []
    for item in candles:
	    close_list.append(float(item[4]))
	    close = numpy.array(close_list) 
   
    return {'open': open, 'high': high, 'low': low, 'close': close}