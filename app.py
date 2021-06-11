import talib
from flask import Flask, request, jsonify
from tickers import tickers
from datetime import datetime
app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

@app.route('/indicators', methods=['POST'])
def indicators():
    data = request.get_json()
    symbol, interval, limit = data['symbol'], data['interval'], data['limit']

    candles_data = tickers(symbol, interval, limit)
    open_time = candles_data['open_time']
    open = candles_data['open']
    close = candles_data['close']
    close_time = candles_data['close_time']
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
    cdlupsidegap2crows = talib.CDLUPSIDEGAP2CROWS(open, high, low, close)
    cdlxsidegap3methods = talib.CDLXSIDEGAP3METHODS(open, high, low, close)

    list = []
    for open_time,open,low,high,close,close_time,volume,ad,adosc,obv,atr,natr,trange,avgprice,medprice,typprice,wclprice,beta,correl,linearreg,linearreg_angle,linearreg_intercept,linearreg_slope,stddev,tsf,tsf,ht_dcperiod,ht_dcphase,inphase,quadrature,sine,leadsine,ht_trendmode,atan,ceil,cos,floor,ln,log10,sin,sqrt,tan,tanh,add,div,max,maxindex,min,minindex,mult,sub,sum,upperband,middleband,lowerband,dema,ema,h_trendline,kama,ma,mama,fama,midpoint,midprice,sar,sma,t3,tema,trima,wma,rsi,adx,adxr,apo,aroondown,aroonup,aroonosc,bop,cci,cmo,dx,macd,macdsignal,macdhist,mfi,minus_di,minus_dm,mom,plus_di,plus_dm,ppo,roc,rocp,rocr,slowk,slowd,fastk,fastd,fastk_rsi,fastd_rsi,trix,ultosc,willr,cdl2crows,cdl3blackcrows,cdl3inside,cdl3linestrike,cdl3outside,cdl3starsinsouth,cdl3whitesoldiers,cdlabandonedbaby,cdladvanceblock,cdlbelthold,cdlbreakaway,cdlclosingmarubozu,cdlconcealbabyswall,cdlcounterattack,cdldarkcloudcover,cdldoji,cdldojistar,cdldragonflydoji,cdlengulfing,cdleveningdojistar,cdleveningstar,cdlgapsidesidewhite,cdlgravestonedoji,cdlhammer,cdlhangingman,cdlharami,cdlharamicross,cdlhighwave,cdlhikkake,cdlhikkakemod,cdlhomingpigeon,cdlidentical3crows,cdlinneck,cdlinvertedhammer,cdlkicking,cdlkickingbylength,cdlladderbottom,cdllongleggeddoji,cdllongline,cdlmarubozu,cdlmatchinglow,cdlmathold,cdlmorningdojistar,cdlmorningstar,cdlonneck,cdlpiercing,cdlrickshawman,cdlrisefall3methods,cdlseparatinglines,cdlshootingstar,cdlshortline,cdlspinningtop,cdlstalledpattern,cdlsticksandwich,cdltakuri,cdltasukigap,cdlthrusting,cdltristar,cdlupsidegap2crows,cdlxsidegap3methods in zip(open_time,open,low,high,close,close_time,volume,ad,adosc,obv,atr,natr,trange,avgprice,medprice,typprice,wclprice,beta,correl,linearreg,linearreg_angle,linearreg_intercept,linearreg_slope,stddev,tsf,tsf,ht_dcperiod,ht_dcphase,inphase,quadrature,sine,leadsine,ht_trendmode,atan,ceil,cos,floor,ln,log10,sin,sqrt,tan,tanh,add,div,max,maxindex,min,minindex,mult,sub,sum,upperband,middleband,lowerband,dema,ema,h_trendline,kama,ma,mama,fama,midpoint,midprice,sar,sma,t3,tema,trima,wma,rsi,adx,adxr,apo,aroondown,aroonup,aroonosc,bop,cci,cmo,dx,macd,macdsignal,macdhist,mfi,minus_di,minus_dm,mom,plus_di,plus_dm,ppo,roc,rocp,rocr,slowk,slowd,fastk,fastd,fastk_rsi,fastd_rsi,trix,ultosc,willr,cdl2crows,cdl3blackcrows,cdl3inside,cdl3linestrike,cdl3outside,cdl3starsinsouth,cdl3whitesoldiers,cdlabandonedbaby,cdladvanceblock,cdlbelthold,cdlbreakaway,cdlclosingmarubozu,cdlconcealbabyswall,cdlcounterattack,cdldarkcloudcover,cdldoji,cdldojistar,cdldragonflydoji,cdlengulfing,cdleveningdojistar,cdleveningstar,cdlgapsidesidewhite,cdlgravestonedoji,cdlhammer,cdlhangingman,cdlharami,cdlharamicross,cdlhighwave,cdlhikkake,cdlhikkakemod,cdlhomingpigeon,cdlidentical3crows,cdlinneck,cdlinvertedhammer,cdlkicking,cdlkickingbylength,cdlladderbottom,cdllongleggeddoji,cdllongline,cdlmarubozu,cdlmatchinglow,cdlmathold,cdlmorningdojistar,cdlmorningstar,cdlonneck,cdlpiercing,cdlrickshawman,cdlrisefall3methods,cdlseparatinglines,cdlshootingstar,cdlshortline,cdlspinningtop,cdlstalledpattern,cdlsticksandwich,cdltakuri,cdltasukigap,cdlthrusting,cdltristar,cdlupsidegap2crows,cdlxsidegap3methods):
        candle =  {      
         'kline': {
            'time_open': open_time,
            'open': open,
            'low': low,
            'high': high,
            'close': close,
            'time_close': close_time,
            'volume': volume
        },
        'volume_indicators': {
            'ad': ad,
            'adosc': adosc,
            'obv': obv
        },
        'volatility_indicators': {
            'atr': atr,
            'natr': natr,
            'trange': trange
        },        
        'momentum_indicators': {
            'rsi': rsi,
            'adx': adx,
            'adxr': adxr,
            'apo': apo,
            'aroon': {'aroondown': aroondown, 'aroonup': aroonup},
            'aroonosc': aroonosc,
            'bop': bop,
            'cci': cci,
            'cmo': cmo,
            'dx': dx,
            'macd': {'macd': macd, 'macdsignal': macdsignal, 'macdhist': macdhist},
            'mfi': mfi,
            'minus_di': minus_di,
            'minus_dm': minus_dm,
            'mom': mom,
            'plus_di': plus_di,
            'plus_dm': plus_dm,
            'ppo': ppo,
            'roc': roc,
            'rocp': rocp,
            'rocr': rocr,
            'stoch': {'slowk': slowk, 'slowd': slowd},
            'stochfast': {'fastk': fastk, 'fastd': fastd},
            'stochrsi': {'fastkrsi': fastk_rsi, 'fastdrsi': fastd_rsi},
            'trix': trix,
            'ultosc': ultosc,
            'willr': willr
        },
         'overlap_studies': {
            'bbands': {'upperband': upperband,'middleband': middleband, 'lowerband': lowerband },
            'dema': dema,
            'ema': ema,
            'h_trendline': h_trendline,
            'kama': kama,
            'ma': ma,
            'mesa': {'mama': mama, 'fama': fama},
            'midpoint': midpoint,
            'midprice': midprice,
            'sar': sar,
            'sma': sma,
            't3': t3,
            'tema': tema,
            'trima': trima,
            'wma': wma
        },
        'price_transform': {
            'avgprice': avgprice,
            'medprice': medprice,
            'typprice': typprice,
            'wclprice': wclprice
        },
        'statistic_functions': {
            'beta': beta,
            'correl': correl,
            'linearreg': linearreg,
            'linearreg_angle': linearreg_angle,
            'linearreg_intercept': linearreg_intercept,
            'linearreg_slope': linearreg_slope,
            'stddev': stddev,
            'tsf': tsf,
            'tsf': tsf
        },
        'cycle_indicators': {
            'ht_dcperiod': ht_dcperiod,
            'ht_dcphase': ht_dcphase,
            'ht_phasor ': {'inphase': inphase, 'quadrature': quadrature},
            'ht_sine': {'sine': sine, 'leadsine': leadsine},
            'ht_trendmode': bool(ht_trendmode)
        },
        'math_transform': {
            'atan': atan,
            'ceil': ceil,
            'cos': cos,
            'floor': floor,
            'ln': ln,
            'log10': log10,
            'sin': sin,
            'sqrt': sqrt,
            'tan': tan,
            'tanh': tanh
        },
        'math_operator': {
            'add': add,
            'div': div,
            'max': max,
            'maxindex': float(maxindex),
            'min': min,
            'minindex': float(minindex),
            'mult': float(mult),
            'sub': sub,
            'sum': sum
        },       
        'pattern_recognition': {
            'cdl2crows': bool(cdl2crows),
            'cdl3blackcrows': bool(cdl3blackcrows),
            'cdl3inside': bool(cdl3inside),
            'cdl3linestrike': bool(cdl3linestrike),
            'cdl3outside': bool(cdl3outside),
            'cdl3starsinsouth': bool(cdl3starsinsouth),
            'cdl3whitesoldiers': bool(cdl3whitesoldiers),
            'cdlabandonedbaby': bool(cdlabandonedbaby),
            'cdladvanceblock': bool(cdladvanceblock),
            'cdlbelthold': bool(cdlbelthold),
            'cdlbreakaway': bool(cdlbreakaway),
            'cdlclosingmarubozu': bool(cdlclosingmarubozu),
            'cdlconcealbabyswall': bool(cdlconcealbabyswall),
            'cdlcounterattack': bool(cdlcounterattack),
            'cdldarkcloudcover': bool(cdldarkcloudcover),
            'cdldoji': bool(cdldoji),
            'cdldojistar': bool(cdldojistar),
            'cdldragonflydoji': bool(cdldragonflydoji),
            'cdlengulfing': bool(cdlengulfing),
            'cdleveningdojistar': bool(cdleveningdojistar),
            'cdleveningstar': bool(cdleveningstar),
            'cdlgapsidesidewhite': bool(cdlgapsidesidewhite),
            'cdlgravestonedoji': bool(cdlgravestonedoji),
            'cdlhammer': bool(cdlhammer),
            'cdlhangingman': bool(cdlhangingman),
            'cdlharami': bool(cdlharami),
            'cdlharamicross': bool(cdlharamicross),
            'cdlhighwave': bool(cdlhighwave),
            'cdlhikkake': bool(cdlhikkake),
            'cdlhikkakemod': bool(cdlhikkakemod),
            'cdlhomingpigeon': bool(cdlhomingpigeon),
            'cdlidentical3crows': bool(cdlidentical3crows),
            'cdlinneck': bool(cdlinneck),
            'cdlinvertedhammer': bool(cdlinvertedhammer),
            'cdlkicking': bool(cdlkicking),
            'cdlkickingbylength': bool(cdlkickingbylength),
            'cdlladderbottom': bool(cdlladderbottom),
            'cdllongleggeddoji': bool(cdllongleggeddoji),
            'cdllongline': bool(cdllongline),
            'cdlmarubozu': bool(cdlmarubozu),
            'cdlmatchinglow': bool(cdlmatchinglow),
            'cdlmathold': bool(cdlmathold),
            'cdlmorningdojistar': bool(cdlmorningdojistar),
            'cdlmorningstar': bool(cdlmorningstar),
            'cdlonneck': bool(cdlonneck),
            'cdlpiercing': bool(cdlpiercing),
            'cdlrickshawman': bool(cdlrickshawman),
            'cdlrisefall3methods': bool(cdlrisefall3methods),
            'cdlseparatinglines': bool(cdlseparatinglines),
            'cdlshootingstar': bool(cdlshootingstar),
            'cdlshortline': bool(cdlshortline),
            'cdlspinningtop': bool(cdlspinningtop),
            'cdlstalledpattern': bool(cdlstalledpattern),
            'cdlsticksandwich': bool(cdlsticksandwich),
            'cdltakuri': bool(cdltakuri),
            'cdltasukigap': bool(cdltasukigap),
            'cdlthrusting': bool(cdlthrusting),
            'cdltristar': bool(cdltristar),
            'cdlupsidegap2crows': bool(cdlupsidegap2crows),
            'cdlxsidegap3methods': bool(cdlxsidegap3methods)
        }
    } 
        list.append(candle)              

    return jsonify(list[100:])
