import ta


def atr_strategy(data, window=14, atr_multiplier=2):
    data['ATR'] = ta.volatility.AverageTrueRange(
        high=data['High'],
        low=data['Low'],
        close=data['Close'],
        window=window
    ).average_true_range()
    data['Upper_Band'] = data['High'].shift(1) + (atr_multiplier * data['ATR'])
    data['Lower_Band'] = data['Low'].shift(1) - (atr_multiplier * data['ATR'])
    if data['Close'].iloc[-1] > data['Upper_Band'].iloc[-1]:
        return "BUY"
    elif data['Close'].iloc[-1] < data['Lower_Band'].iloc[-1]:
        return "SELL"
    else:
        return "HOLD"


def parabolic_sar_strategy(data):
    data['SAR'] = ta.trend.PSARIndicator(
        high=data['High'],
        low=data['Low'],
        close=data['Close']
    ).psar()
    if data['Close'].iloc[-1] > data['SAR'].iloc[-1]:
        return "BUY"
    else:
        return "SELL"


def ichimoku_cloud_strategy(data):
    ichimoku = ta.trend.IchimokuIndicator(
        high=data['High'],
        low=data['Low']
    )
    data['Tenkan_Sen'] = ichimoku.ichimoku_conversion_line()
    data['Kijun_Sen'] = ichimoku.ichimoku_base_line()
    data['Senkou_Span_A'] = ichimoku.ichimoku_a()
    data['Senkou_Span_B'] = ichimoku.ichimoku_b()
    if (data['Close'].iloc[-1] > data['Senkou_Span_A'].iloc[-1] and
        data['Close'].iloc[-1] > data['Senkou_Span_B'].iloc[-1] and
        data['Tenkan_Sen'].iloc[-1] > data['Kijun_Sen'].iloc[-1]):
        return "BUY"
    elif (data['Close'].iloc[-1] < data['Senkou_Span_A'].iloc[-1] and
          data['Close'].iloc[-1] < data['Senkou_Span_B'].iloc[-1] and
          data['Tenkan_Sen'].iloc[-1] < data['Kijun_Sen'].iloc[-1]):
        return "SELL"
    else:
        return "HOLD"


def fibonacci_retracement_strategy(data):
    high = data['High'].max()
    low = data['Low'].min()
    diff = high - low
    levels = {
        '61.8%': high - 0.618 * diff,
        '50%': high - 0.5 * diff,
        '38.2%': high - 0.382 * diff
    }
    current_price = data['Close'].iloc[-1]
    if current_price <= levels['61.8%']:
        return "BUY"
    elif current_price >= levels['38.2%']:
        return "SELL"
    else:
        return "HOLD"


def volume_profile_strategy(data, window=20):
    data['Volume_Profile'] = ta.volume.VolumeWeightedAveragePrice(
        high=data['High'],
        low=data['Low'],
        close=data['Close'],
        volume=data['Volume'],
        window=window
    ).volume_weighted_average_price()
    if data['Close'].iloc[-1] > data['Volume_Profile'].iloc[-1]:
        return "BUY"
    else:
        return "SELL"


def adx_strategy(data, window=14):
    adx = ta.trend.ADXIndicator(
        high=data['High'],
        low=data['Low'],
        close=data['Close'],
        window=window
    )
    data['ADX'] = adx.adx()
    data['+DI'] = adx.adx_pos()
    data['-DI'] = adx.adx_neg()
    if data['ADX'].iloc[-1] > 25 and data['+DI'].iloc[-1] > data['-DI'].iloc[-1]:
        return "BUY"
    elif data['ADX'].iloc[-1] > 25 and data['-DI'].iloc[-1] > data['+DI'].iloc[-1]:
        return "SELL"
    else:
        return "HOLD"


def mfi_strategy(data, window=14, buy_threshold=20, sell_threshold=80):
    data['MFI'] = ta.volume.MFIIndicator(
        high=data['High'],
        low=data['Low'],
        close=data['Close'],
        volume=data['Volume'],
        window=window
    ).money_flow_index()
    if data['MFI'].iloc[-1] < buy_threshold:
        return "BUY"
    elif data['MFI'].iloc[-1] > sell_threshold:
        return "SELL"
    else:
        return "HOLD"


def roc_strategy(data, window=14, buy_threshold=5, sell_threshold=-5):
    data['ROC'] = ta.momentum.ROCIndicator(data['Close'], window=window).roc()
    if data['ROC'].iloc[-1] > buy_threshold:
        return "BUY"
    elif data['ROC'].iloc[-1] < sell_threshold:
        return "SELL"
    else:
        return "HOLD"


def williams_r_strategy(data, window=14, buy_threshold=-80, sell_threshold=-20):
    data['Williams_%R'] = ta.momentum.WilliamsRIndicator(
        high=data['High'],
        low=data['Low'],
        close=data['Close'],
        window=window
    ).williams_r()
    if data['Williams_%R'].iloc[-1] < buy_threshold:
        return "BUY"
    elif data['Williams_%R'].iloc[-1] > sell_threshold:
        return "SELL"
    else:
        return "HOLD"


def cmf_strategy(data, window=20):
    data['CMF'] = ta.volume.ChaikinMoneyFlowIndicator(
        high=data['High'],
        low=data['Low'],
        close=data['Close'],
        volume=data['Volume'],
        window=window
    ).chaikin_money_flow()
    if data['CMF'].iloc[-1] > 0:
        return "BUY"
    else:
        return "SELL"
