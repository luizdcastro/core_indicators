from binance.client import Client
import numpy, talib, websocket

socket = "wss://stream.binance.com:9443/ws/ethusdt@kline_1m"

eth_tickers = []    

def on_message(ws, message):
    json_message = json.loads(message)

    candle = json_message['k']
    is_candle_closed = candle['x']

    if is_candle_closed:
        eth_candle = {'symbol':candle['s'],'open':float(candle['o']),'close':float(candle['c']),'high':float(candle['h']),'low':float(candle['l']),'volume':float(candle['v'])}
        eth_tickers.append(eth_candle)
        rsi() 

        if len(eth_tickers) > 15:
            eth_tickers.pop(1) 
    
ws = websocket.WebSocketApp(socket, on_message=on_message)
ws.run_forever()

import numpy, talib, os, requests
from threading import Timer
from flask import Flask, request
from dotenv import load_dotenv
load_dotenv()
app = Flask(__name__)

baseURL = 'https://api.binance.com/api/v3/klines?'

@app.route('/rsi', methods=['GET'])
def rsi():
    # Reciving the parameters for getting the candles data
    symbol = request.args['symbol']
    interval = request.args['interval']
    limit = request.args['limit']
    close = request.args['close']

    # Making the request to get the marked data based on the parameters
    candles = requests.get(f'{baseURL}symbol={symbol}&interval={interval}&limit={limit}')

    # Getting the response response data and fetchin the close values to an array
    array = []
    for item in candles:
        array.append(float(item[4]))
    close = numpy.array(array)
    print(len(close))

    # Calculate the RSI and return the result
    rsi = talib.RSI(close, 14)      
    return {'rsi': rsi[14]}


    {
  "rsi": 62.169665401953836
}




