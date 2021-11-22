# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 23:21:36 2021

@author: Jubish
"""

from kiteconnect import KiteConnect
import pandas as pd
from datetime import datetime, timedelta
import dateutil.relativedelta

from pynse import *
nse=Nse()

cwd = os.chdir("D:\\softwares programming\\PythonProjects\\AlgorithmicTrading\\KiteTradingBot")



#generate trading session
access_token = open("access_token.txt",'r').read()
key_secret = open("my_det.txt",'r').read().split()
kite = KiteConnect(api_key=key_secret[0])
kite.set_access_token(access_token)

#get dump of all NSE instruments
instrument_dump = kite.instruments("NSE")
instrument_df = pd.DataFrame(instrument_dump)

def fetchohlc(stock_symbol,duration):
    to_date = datetime.now()
    from_date = datetime.today() - timedelta(days=duration)
    data = pd.DataFrame(nse.get_hist(stock_symbol, from_date=from_date,to_date=to_date))
    return data

def levels(ohlc_day):    
    """returns pivot point and support/resistance levels"""
    high = round(ohlc_day["high"][-1],2)
    low = round(ohlc_day["low"][-1],2)
    close = round(ohlc_day["close"][-1],2)
    pivot = round((high + low + close)/3,2)
    r1 = round((2*pivot - low),2)
    r2 = round((pivot + (high - low)),2)
    r3 = round((high + 2*(pivot - low)),2)
    s1 = round((2*pivot - high),2)
    s2 = round((pivot - (high - low)),2)
    s3 = round((low - 2*(high - pivot)),2)
    return (pivot,r1,r2,r3,s1,s2,s3)

n= 1
ohlc_day = fetchohlc("TATAMOTORS",100)
#ohlc_day.drop(ohlc_day.tail(n).index,inplace=True)
#print(ohlc_day)
pp_levels = levels(ohlc_day.iloc[:-1,:])
#pp_levels = levels(ohlc_day)
print(pp_levels)