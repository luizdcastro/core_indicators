import talib
from flask import Flask, request, jsonify
from getData import candles
app = Flask(__name__)

@app.route('/rsi', methods=['POST'])
def rsi():
    data = request.get_json()
    symbol, interval, isClosed = data['symbol'], data['interval'], data['isClosed']

    candles_data = candles(symbol, interval, isClosed)
    close = candles_data['close']

    rsi = talib.RSI(close, timeperiod=14)  
    return jsonify({'rsi': rsi[99]})

@app.route('/macd', methods=['POST'])
def macd():
    data = request.get_json()
    symbol, interval, isClosed = data['symbol'], data['interval'], data['isClosed']

    candles_data = candles(symbol, interval, isClosed)
    close = candles_data['close']

    macd, macdsignal, macdhist = talib.MACD(close, fastperiod=12, slowperiod=26, signalperiod=9)  
    return jsonify({'macd': macd[99], 'macdsignal': macdsignal[99], 'macdhist': macdhist[99]})

port = 5000
app.run(port=5000 or port)