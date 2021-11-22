# -*- coding: utf-8 -*-
"""
Created on Sat Oct 16 14:21:48 2021

@author: jubis
"""

from pynse import *
from datetime import datetime, timedelta

nse=Nse()
#nse.info('SBIN')
nse.get_quote('RELIANCE')
nse.get_hist('TATAMOTORS')

nse.get_hist('NIFTY 50', from_date=dt.date(2020,1,1),to_date=dt.date(2020,6,26))

duration = 10
stock_symbol = 'SBIN'
to_date = datetime.now()
from_date = datetime.today() - timedelta(days=duration)
nse.get_hist(stock_symbol, from_date=from_date,to_date=to_date)