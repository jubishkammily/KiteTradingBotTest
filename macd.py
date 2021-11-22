# -*- coding: utf-8 -*-
"""
Created on Sat Oct 16 12:36:15 2021

@author: jubis
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
    #data.set_index("date",inplace=True)
    #data.to_csv('file1.csv')
    #df2 = pd.read_csv("file1.csv")
    #df2.set_index("Date",inplace=True)
    return data


def MACD(DF,a,b,c):
    df = DF.copy()
    #df["MA_Fast"]=df["close"].rolling(a).mean()
    #df["MA_Slow"]=df["close"].rolling(b).mean()
    #df["MACD"]=df["MA_Fast"] - df["MA_Slow"]
    #df["Signal"]=df["MACD"].rolling(c).mean()
    df["MA_Fast"]=df["close"].ewm(span=a,min_periods=a).mean()
    df["MA_Slow"]=df["close"].ewm(span=b,min_periods=b).mean()
    df["MACD"]=df["MA_Fast"]-df["MA_Slow"]
    df["Signal"]=df["MACD"].ewm(span=c,min_periods=c).mean()
    df.dropna(inplace=True)
    return df

df = fetchohlc("TATAMOTORS",100)
print(df)
df3 = MACD(df,12,26,9)
print(df3)



    

