# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 00:07:48 2021

@author: Jubish
"""

from kiteconnect import KiteConnect
import pandas as pd
from datetime import datetime, timedelta
import dateutil.relativedelta

#cwd = os.chdir("D:\\softwares programming\\PythonProjects\\AlgorithmicTrading\\KiteTradingBot")
#generate trading session
access_token = open("access_token.txt",'r').read()
key_secret = open("my_det.txt",'r').read().split()
kite = KiteConnect(api_key=key_secret[0])
kite.set_access_token(access_token)


def fetchohlc(stock_symbol,duration):
    
    to_date = datetime.now()
    from_date = datetime.today() - timedelta(days=duration)
    data = yf.download("TATAMOTORS.NS", start=from_date, end=to_date,interval="15m")
    #data = yf.download("TATAMOTORS.NS", period='1mo', interval="5m")
    #df2.set_index("Date",inplace=True)
    return data


def MACD(DF, a=12 ,b=26, c=9):
    """function to calculate MACD
       typical values a(fast moving average) = 12; 
                      b(slow moving average) =26; 
                      c(signal line ma window) =9"""
    df = DF.copy()
    df["ma_fast"] = df["Adj Close"].ewm(span=a, min_periods=a).mean()
    df["ma_slow"] = df["Adj Close"].ewm(span=b, min_periods=b).mean()
    df["macd"] = df["ma_fast"] - df["ma_slow"]
    df["signal"] = df["macd"].ewm(span=c, min_periods=c).mean()
    #return df.loc[:,["macd","signal"]]
    return df

data = fetchohlc("TATAMOTORS.NS",30)
df = MACD(data, a=12 ,b=26, c=9)
print(df)