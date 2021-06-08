import talib
from flask import Flask, request, jsonify
from tickers import tickers
app = Flask(__name__)

@app.route('/indicators', methods=['POST'])
def indicators():
    data = request.get_json()
    symbol, interval, isClosed = data['symbol'], data['interval'], data['isClosed']

    candles_data = tickers(symbol, interval, isClosed)
    open = candles_data['open']
    close = candles_data['close']
    high = candles_data['high']
    low = candles_data['low']
    volume = candles_data['volume']

    # Volume Indicator
    ad = talib.AD(high, low, close, volume)
    adosc = talib.ADOSC(high, low, close, volume, fastperiod=3, slowperiod=10)
    obv = talib.OBV(close, volume)

    # Volatility Indicator
    atr = talib.ATR(high, low, close, timeperiod=14)
    natr = talib.NATR(high, low, close, timeperiod=14)
    trange = talib.TRANGE(high, low, close)

    # Price Transform
    avgprice = talib.AVGPRICE(open, high, low, close)
    medprice = talib.MEDPRICE(high, low)
    typprice = talib.TYPPRICE(high, low, close)
    wclprice = talib.WCLPRICE(high, low, close)

    # Cycle Indicator
    ht_dcperiod = talib.HT_DCPERIOD(close)
    ht_dcphase = talib.HT_DCPHASE(close)
    inphase, quadrature = talib.HT_PHASOR(close)
    sine, leadsine = talib.HT_SINE(close)
    ht_trendmode = talib.HT_TRENDMODE(close)

    # Statistic
    beta = talib.BETA(high, low, timeperiod=5)
    correl = talib.CORREL(high, low, timeperiod=30)
    linearreg = talib.LINEARREG(close, timeperiod=14)
    linearreg_angle = talib.LINEARREG_ANGLE(close, timeperiod=14)
    linearreg_intercept = talib.LINEARREG_INTERCEPT(close, timeperiod=14)
    linearreg_slope = talib.LINEARREG_SLOPE(close, timeperiod=14)
    stddev = talib.STDDEV(close, timeperiod=5, nbdev=1)
    tsf = talib.TSF(close, timeperiod=14)
    tsf = talib.VAR(close, timeperiod=5, nbdev=1)

    # Math Transform
    atan = talib.ATAN(close)
    ceil = talib.CEIL(close)
    cos = talib.COS(close)
    floor = talib.FLOOR(close)
    ln = talib.LN(close)
    log10 = talib.LOG10(close)
    sin = talib.SIN(close)
    sqrt = talib.SQRT(close)
    tan = talib.TAN(close)
    tanh = talib.TANH(close)

    # Math Operator
    add = talib.ADD(high, low)
    div = talib.DIV(high, low)
    max = talib.MAX(close, timeperiod=30)
    maxindex = talib.MAXINDEX(close, timeperiod=30)
    min = talib.MIN(close, timeperiod=30)
    minindex = talib.MININDEX(close, timeperiod=30)
    mult = talib.MULT(high, low)
    sub = talib.SUB(high, low)
    sum = talib.SUM(close, timeperiod=30)

    # Overlap Studies
    upperband, middleband, lowerband = talib.BBANDS(close, timeperiod=20, nbdevup=2, nbdevdn=2, matype=0)
    dema = talib.DEMA(close, timeperiod=30)
    ema = talib.EMA(close, timeperiod=30)
    h_trendline = talib.HT_TRENDLINE(close)
    kama = talib.KAMA(close, timeperiod=30)
    ma = talib.MA(close, timeperiod=30, matype=0)
    mama, fama  = talib.MAMA(close, fastlimit=0.25, slowlimit=0.05)
    midpoint = talib.MIDPOINT(close, timeperiod=14)
    midprice = talib.MIDPRICE(high, low, timeperiod=14)
    sar = talib.SAR(high, low, acceleration=0.2, maximum=0.2)
    sma = talib.SMA(close, timeperiod=30)
    t3 = talib.T3(close, timeperiod=5, vfactor=0.7)
    tema = talib.TEMA(close, timeperiod=30)
    trima = talib.TRIMA(close, timeperiod=30)
    wma = talib.WMA(close, timeperiod=30)

    # Momentum Indicator Functions
    adx = talib.ADX(high, low, close, timeperiod=14)
    adxr = talib.ADXR(high, low, close, timeperiod=14)
    apo = talib.APO(close, fastperiod=12, slowperiod=26, matype=0)
    aroondown, aroonup = talib.AROON(high, low, timeperiod=14)
    aroonosc = talib.AROONOSC(high, low, timeperiod=14)
    bop = talib.BOP(open, high, low, close)
    cci = talib.CCI(high, low, close, timeperiod=14)
    cmo = talib.CMO(close, timeperiod=14)
    dx = talib.DX(high, low, close, timeperiod=14)
    macd, macdsignal, macdhist = talib.MACD(
        close, fastperiod=12, slowperiod=26, signalperiod=9)
    mfi = talib.MFI(high, low, close, volume, timeperiod=14)
    minus_di = talib.MINUS_DI(high, low, close, timeperiod=14)
    minus_dm = talib.MINUS_DM(high, low, timeperiod=14)
    mom = talib.MOM(close, timeperiod=10)
    plus_di = talib.PLUS_DI(high, low, close, timeperiod=14)
    plus_dm = talib.PLUS_DM(high, low, timeperiod=14)
    ppo = talib.PPO(close, fastperiod=12, slowperiod=26, matype=0)
    roc = talib.ROC(close, timeperiod=10)
    rocp = talib.ROCP(close, timeperiod=10)
    rocr = talib.ROCR(close, timeperiod=10)
    rsi = talib.RSI(close, timeperiod=14)
    slowk, slowd = talib.STOCH(high, low, close, fastk_period=5,
                               slowk_period=3, slowk_matype=0, slowd_period=3, slowd_matype=0)
    fastk, fastd = talib.STOCHF(
        high, low, close, fastk_period=5, fastd_period=3, fastd_matype=0)
    fastk_rsi, fastd_rsi = talib.STOCHRSI(
        close, timeperiod=14, fastk_period=5, fastd_period=3, fastd_matype=0)
    trix = talib.TRIX(close, timeperiod=30)
    ultosc = talib.ULTOSC(high, low, close, timeperiod1=7,
                          timeperiod2=14, timeperiod3=28)
    willr = talib.WILLR(high, low, close, timeperiod=14)

    # Pattern Recognition
    cdl2crows = talib.CDL2CROWS(open, high, low, close)
    cdl3blackcrows = talib.CDL3BLACKCROWS(open, high, low, close)
    cdl3inside = talib.CDL3INSIDE(open, high, low, close)
    cdl3linestrike = talib.CDL3LINESTRIKE(open, high, low, close)
    cdl3outside = talib.CDL3OUTSIDE(open, high, low, close)
    cdl3starsinsouth = talib.CDL3STARSINSOUTH(open, high, low, close)
    cdl3whitesoldiers = talib.CDL3WHITESOLDIERS(open, high, low, close)
    cdlabandonedbaby = talib.CDLABANDONEDBABY(
        open, high, low, close, penetration=0)
    cdladvanceblock = talib.CDLADVANCEBLOCK(open, high, low, close)
    cdlbelthold = talib.CDLBELTHOLD(open, high, low, close)
    cdlbreakaway = talib.CDLBREAKAWAY(open, high, low, close)
    cdlclosingmarubozu = talib.CDLCLOSINGMARUBOZU(open, high, low, close)
    cdlconcealbabyswall = talib.CDLCONCEALBABYSWALL(open, high, low, close)
    cdlcounterattack = talib.CDLCOUNTERATTACK(open, high, low, close)
    cdldarkcloudcover = talib.CDLDARKCLOUDCOVER(
        open, high, low, close, penetration=0)
    cdldoji = talib.CDLDOJI(open, high, low, close)
    cdldojistar = talib.CDLDOJISTAR(open, high, low, close)
    cdldragonflydoji = talib.CDLDRAGONFLYDOJI(open, high, low, close)
    cdlengulfing = talib.CDLENGULFING(open, high, low, close)
    cdleveningdojistar = talib.CDLEVENINGDOJISTAR(
        open, high, low, close, penetration=0)
    cdleveningstar = talib.CDLEVENINGSTAR(
        open, high, low, close, penetration=0)
    cdlgapsidesidewhite = talib.CDLGAPSIDESIDEWHITE(open, high, low, close)
    cdlgravestonedoji = talib.CDLGRAVESTONEDOJI(open, high, low, close)
    cdlhammer = talib.CDLHAMMER(open, high, low, close)
    cdlhangingman = talib.CDLHANGINGMAN(open, high, low, close)
    cdlharami = talib.CDLHARAMI(open, high, low, close)
    cdlharamicross = talib.CDLHARAMICROSS(open, high, low, close)
    cdlhighwave = talib.CDLHIGHWAVE(open, high, low, close)
    cdlhikkake = talib.CDLHIKKAKE(open, high, low, close)
    cdlhikkakemod = talib.CDLHIKKAKEMOD(open, high, low, close)
    cdlhomingpigeon = talib.CDLHOMINGPIGEON(open, high, low, close)
    cdlidentical3crows = talib.CDLIDENTICAL3CROWS(open, high, low, close)
    cdlinneck = talib.CDLINNECK(open, high, low, close)
    cdlinvertedhammer = talib.CDLINVERTEDHAMMER(open, high, low, close)
    cdlkicking = talib.CDLKICKING(open, high, low, close)
    cdlkickingbylength = talib.CDLKICKINGBYLENGTH(open, high, low, close)
    cdlladderbottom = talib.CDLLADDERBOTTOM(open, high, low, close)
    cdllongleggeddoji = talib.CDLLONGLEGGEDDOJI(open, high, low, close)
    cdllongline = talib.CDLLONGLINE(open, high, low, close)
    cdlmarubozu = talib.CDLMARUBOZU(open, high, low, close)
    cdlmatchinglow = talib.CDLMATCHINGLOW(open, high, low, close)
    cdlmathold = talib.CDLMATHOLD(open, high, low, close, penetration=0)
    cdlmorningdojistar = talib.CDLMORNINGDOJISTAR(
        open, high, low, close, penetration=0)
    cdlmorningstar = talib.CDLMORNINGSTAR(
        open, high, low, close, penetration=0)
    cdlonneck = talib.CDLONNECK(open, high, low, close)
    cdlpiercing = talib.CDLPIERCING(open, high, low, close)
    cdlrickshawman = talib.CDLRICKSHAWMAN(open, high, low, close)
    cdlrisefall3methods = talib.CDLRISEFALL3METHODS(open, high, low, close)
    cdlseparatinglines = talib.CDLSEPARATINGLINES(open, high, low, close)
    cdlshootingstar = talib.CDLSHOOTINGSTAR(open, high, low, close)
    cdlshortline = talib.CDLSHORTLINE(open, high, low, close)
    cdlspinningtop = talib.CDLSPINNINGTOP(open, high, low, close)
    cdlstalledpattern = talib.CDLSTALLEDPATTERN(open, high, low, close)
    cdlsticksandwich = talib.CDLSTICKSANDWICH(open, high, low, close)
    cdltakuri = talib.CDLTAKURI(open, high, low, close)
    cdltasukigap = talib.CDLTASUKIGAP(open, high, low, close)
    cdlthrusting = talib.CDLTHRUSTING(open, high, low, close)
    cdltristar = talib.CDLTRISTAR(open, high, low, close)
    cdltristar = talib.CDLUNIQUE3RIVER(open, high, low, close)
    cdlupsidegap2crows = talib.CDLUPSIDEGAP2CROWS(open, high, low, close)
    cdlxsidegap3methods = talib.CDLXSIDEGAP3METHODS(open, high, low, close)

    return jsonify({
        'candle': {
            'open': open[99],
            'low': low[99],
            'high': high[99],
            'close': close[99],
            'volume': volume[99]
        },
        'volume': {
            'ad': ad[99],
            'adosc': adosc[99],
            'obv': obv[99]
        },
        'volatility': {
            'atr': atr[99],
            'natr': natr[99],
            'trange': trange[99]
        },
        'price_transform': {
            'avgprice': avgprice[99],
            'medprice': medprice[99],
            'typprice': typprice[99],
            'wclprice': wclprice[99]
        },
        'statistic': {
            'beta': beta[99],
            'correl': correl[99],
            'linearreg': linearreg[99],
            'linearreg_angle': linearreg_angle[99],
            'linearreg_intercept': linearreg_intercept[99],
            'linearreg_slope': linearreg_slope[99],
            'stddev': stddev[99],
            'tsf': tsf[99],
            'tsf': tsf[99]
        },
        'cycle': {
            'ht_dcperiod': ht_dcperiod[99],
            'ht_dcphase': ht_dcphase[99],
            'ht_phasor ': {'inphase': inphase[99], 'quadrature': quadrature[99]},
            'ht_sine': {'sine': sine[99], 'leadsine': leadsine[99]},
            'ht_trendmode': bool(ht_trendmode[99])
        },
        'math_transform': {
            'atan': atan[99],
            'ceil': ceil[99],
            'cos': cos[99],
            'floor': floor[99],
            'ln': ln[99],
            'log10': log10[99],
            'sin': sin[99],
            'sqrt': sqrt[99],
            'tan': tan[99],
            'tanh': tanh[99]
        },
        'math_operator': {
            'add': add[99],
            'div': div[99],
            'max': max[99],
            'maxindex': float(maxindex[99]),
            'min': min[99],
            'minindex': float(minindex[99]),
            'mult': float(mult[99]),
            'sub': sub[99],
            'sum': sum[99]
        },
        'overlap_studies': {
            'bbands': {'upperband': upperband[99],'middleband': middleband[99], 'lowerband': lowerband[99] },
            'dema': dema[99],
            'ema': ema[99],
            'h_trendline': h_trendline[99],
            'kama': kama[99],
            'ma': ma[99],
            'mesa': {'mama': mama[99], 'fama': fama[99]},
            'midpoint': midpoint[99],
            'midprice': midprice[99],
            'sar': sar[99],
            'sma': sma[99],
            't3': t3[99],
            'tema': tema[99],
            'trima': trima[99],
            'wma': wma[99]
        },
        'momentum': {
            'rsi': rsi[99],
            'adx': adx[99],
            'adxr': adxr[99],
            'apo': apo[99],
            'aroon': {'aroondown': aroondown[99], 'aroonup': aroonup[99]},
            'aroonosc': aroonosc[99],
            'bop': bop[99],
            'cci': cci[99],
            'cmo': cmo[99],
            'dx': dx[99],
            'macd': {'macd': macd[99], 'macdsignal': macdsignal[99], 'macdhist': macdhist[99]},
            'mfi': mfi[99],
            'minus_di': minus_di[99],
            'minus_dm': minus_dm[99],
            'mom': mom[99],
            'plus_di': plus_di[99],
            'plus_dm': plus_dm[99],
            'ppo': ppo[99],
            'roc': roc[99],
            'rocp': rocp[99],
            'rocr': rocr[99],
            'stoch': {'slowk': slowk[99], 'slowd': slowd[99]},
            'stochfast': {'fastk': fastk[99], 'fastd': fastd[99]},
            'stochrsi': {'fastkrsi': fastk_rsi[99], 'fastdrsi': fastd_rsi[99]},
            'trix': trix[99],
            'ultosc': ultosc[99],
            'willr': willr[99]
        },
        'pattern': {
            'cdl2crows': bool(cdl2crows[99]),
            'cdl3blackcrows': bool(cdl3blackcrows[99]),
            'cdl3inside': bool(cdl3inside[99]),
            'cdl3linestrike': bool(cdl3linestrike[99]),
            'cdl3outside': bool(cdl3outside[99]),
            'cdl3starsinsouth': bool(cdl3starsinsouth[99]),
            'cdl3whitesoldiers': bool(cdl3whitesoldiers[99]),
            'cdlabandonedbaby': bool(cdlabandonedbaby[99]),
            'cdladvanceblock': bool(cdladvanceblock[99]),
            'cdlbelthold': bool(cdlbelthold[99]),
            'cdlbreakaway': bool(cdlbreakaway[99]),
            'cdlclosingmarubozu': bool(cdlclosingmarubozu[99]),
            'cdlconcealbabyswall': bool(cdlconcealbabyswall[99]),
            'cdlcounterattack': bool(cdlcounterattack[99]),
            'cdldarkcloudcover': bool(cdldarkcloudcover[99]),
            'cdldoji': bool(cdldoji[99]),
            'cdldojistar': bool(cdldojistar[99]),
            'cdldragonflydoji': bool(cdldragonflydoji[99]),
            'cdlengulfing': bool(cdlengulfing[99]),
            'cdleveningdojistar': bool(cdleveningdojistar[99]),
            'cdleveningstar': bool(cdleveningstar[99]),
            'cdlgapsidesidewhite': bool(cdlgapsidesidewhite[99]),
            'cdlgravestonedoji': bool(cdlgravestonedoji[99]),
            'cdlhammer': bool(cdlhammer[99]),
            'cdlhangingman': bool(cdlhangingman[99]),
            'cdlharami': bool(cdlharami[99]),
            'cdlharamicross': bool(cdlharamicross[99]),
            'cdlhighwave': bool(cdlhighwave[99]),
            'cdlhikkake': bool(cdlhikkake[99]),
            'cdlhikkakemod': bool(cdlhikkakemod[99]),
            'cdlhomingpigeon': bool(cdlhomingpigeon[99]),
            'cdlidentical3crows': bool(cdlidentical3crows[99]),
            'cdlinneck': bool(cdlinneck[99]),
            'cdlinvertedhammer': bool(cdlinvertedhammer[99]),
            'cdlkicking': bool(cdlkicking[99]),
            'cdlkickingbylength': bool(cdlkickingbylength[99]),
            'cdlladderbottom': bool(cdlladderbottom[99]),
            'cdllongleggeddoji': bool(cdllongleggeddoji[99]),
            'cdllongline': bool(cdllongline[99]),
            'cdlmarubozu': bool(cdlmarubozu[99]),
            'cdlmatchinglow': bool(cdlmatchinglow[99]),
            'cdlmathold': bool(cdlmathold[99]),
            'cdlmorningdojistar': bool(cdlmorningdojistar[99]),
            'cdlmorningstar': bool(cdlmorningstar[99]),
            'cdlonneck': bool(cdlonneck[99]),
            'cdlpiercing': bool(cdlpiercing[99]),
            'cdlrickshawman': bool(cdlrickshawman[99]),
            'cdlrisefall3methods': bool(cdlrisefall3methods[99]),
            'cdlseparatinglines': bool(cdlseparatinglines[99]),
            'cdlshootingstar': bool(cdlshootingstar[99]),
            'cdlshortline': bool(cdlshortline[99]),
            'cdlspinningtop': bool(cdlspinningtop[99]),
            'cdlstalledpattern': bool(cdlstalledpattern[99]),
            'cdlsticksandwich': bool(cdlsticksandwich[99]),
            'cdltakuri': bool(cdltakuri[99]),
            'cdltasukigap': bool(cdltasukigap[99]),
            'cdlthrusting': bool(cdlthrusting[99]),
            'cdltristar': bool(cdltristar[99]),
            'cdltristar': bool(cdltristar[99]),
            'cdlupsidegap2crows': bool(cdlupsidegap2crows[99]),
            'cdlxsidegap3methods': bool(cdlxsidegap3methods[99])
        }
    })
