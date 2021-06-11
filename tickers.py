import numpy, requests
from datetime import datetime

baseURL = 'https://api.binance.com/api/v3/klines?'

def tickers(symbol, interval, limit):
    response = requests.get(f'{baseURL}symbol={symbol}&interval={interval}&limit={limit + 100}')
    candles = response.json()  

    open_time_list = []
    for item in candles:        
	    open_time_list.append(datetime.utcfromtimestamp(item[0] / 1000).isoformat()+'.000000Z')
	    open_time = numpy.array(open_time_list) 

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
    
    volume_list = []
    for item in candles:
	    volume_list.append(float(item[5]))
	    volume = numpy.array(volume_list) 
    
    close_time_list = []
    for item in candles:
	    close_time_list.append(datetime.utcfromtimestamp(item[6] / 1000).isoformat()+'Z')
	    close_time = numpy.array(close_time_list) 
   
    return {'open_time': open_time, 'open': open, 'high': high, 'low': low, 'close': close, 'close_time': close_time, 'volume': volume}