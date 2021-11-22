# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 20:25:03 2021

@author: jubis
"""

from kiteconnect import KiteConnect
import logging
import os
import datetime as dt
import pandas as pd
 
#generate trading session
access_token = open("access_token.txt",'r').read()
key_secret = open("my_det.txt",'r').read().split()
kite = KiteConnect(api_key=key_secret[0])
kite.set_access_token(access_token)

#get dump of all NSE instruments
instrument_dump = kite.instruments("NSE")
instrument_df = pd.DataFrame(instrument_dump)
instrument_df.to_csv("NSE_Instruments_31122019.csv",index=False)