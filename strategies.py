import pandas as pd
import ta  # Technical analysis library


# Moving Average Crossover
def moving_average_crossover(data, short_window=5, long_window=15):
    data['Short_MA'] = data['Close'].rolling(window=short_window).mean()
    data['Long_MA'] = data['Close'].rolling(window=long_window).mean()
    if data['Short_MA'].iloc[-1] > data['Long_MA'].iloc[-1]:
        return "BUY"
    else:
        return "SELL"


# Relative Strength Index (RSI)
def rsi_strategy(data, window=14, buy_threshold=35, sell_threshold=65):
    data['RSI'] = ta.momentum.RSIIndicator(data['Close'], window=window).rsi()
    if data['RSI'].iloc[-1] < buy_threshold:
        return "BUY"
    elif data['RSI'].iloc[-1] > sell_threshold:
        return "SELL"
    else:
        return "HOLD"


# Bollinger Bands
def bollinger_bands_strategy(data, window=20, num_std=2.5):
    indicator_bb = ta.volatility.BollingerBands(data['Close'], window=window, window_dev=num_std)
    data['Upper_Band'] = indicator_bb.bollinger_hband()
    data['Lower_Band'] = indicator_bb.bollinger_lband()
    if data['Close'].iloc[-1] < data['Lower_Band'].iloc[-1]:
        return "BUY"
    elif data['Close'].iloc[-1] > data['Upper_Band'].iloc[-1]:
        return "SELL"
    else:
        return "HOLD"


# MACD (Moving Average Convergence Divergence)
def macd_strategy(data, short_window=8, long_window=17, signal_window=9):
    data['MACD'] = ta.trend.MACD(data['Close'], window_slow=long_window, window_fast=short_window, window_sign=signal_window).macd()
    data['Signal_Line'] = ta.trend.MACD(data['Close'], window_slow=long_window, window_fast=short_window, window_sign=signal_window).macd_signal()
    if data['MACD'].iloc[-1] > data['Signal_Line'].iloc[-1]:
        return "BUY"
    else:
        return "SELL"


# Volume Weighted Average Price (VWAP)
def vwap_strategy(data):
    data['VWAP'] = ta.volume.VolumeWeightedAveragePrice(
        high=data['High'],
        low=data['Low'],
        close=data['Close'],
        volume=data['Volume'],
        window=14
    ).volume_weighted_average_price()
    if data['Close'].iloc[-1] > data['VWAP'].iloc[-1]:
        return "BUY"
    else:
        return "SELL"


# Stochastic Oscillator
def stochastic_oscillator_strategy(data, window=14, smooth_window=3, buy_threshold=25, sell_threshold=75):
    stoch = ta.momentum.StochasticOscillator(
        high=data['High'],
        low=data['Low'],
        close=data['Close'],
        window=window,
        smooth_window=smooth_window
    )
    data['Stoch_%K'] = stoch.stoch()
    data['Stoch_%D'] = stoch.stoch_signal()
    if data['Stoch_%K'].iloc[-1] < buy_threshold and data['Stoch_%D'].iloc[-1] < buy_threshold:
        return "BUY"
    elif data['Stoch_%K'].iloc[-1] > sell_threshold and data['Stoch_%D'].iloc[-1] > sell_threshold:
        return "SELL"
    else:
        return "HOLD"


# On-Balance Volume (OBV)
def obv_strategy(data):
    data['OBV'] = ta.volume.OnBalanceVolumeIndicator(close=data['Close'], volume=data['Volume']).on_balance_volume()
    if data['OBV'].iloc[-1] > data['OBV'].iloc[-2]:
        return "BUY"
    else:
        return "SELL"


# All Strategies
def apply_all_strategies(data):
    strategies = {
        "Moving Average Crossover": moving_average_crossover(data),
        "RSI": rsi_strategy(data),
        "Bollinger Bands": bollinger_bands_strategy(data),
        "MACD": macd_strategy(data),
        "VWAP": vwap_strategy(data),
        "Stochastic Oscillator": stochastic_oscillator_strategy(data),
        "OBV": obv_strategy(data)
    }
    return strategies
