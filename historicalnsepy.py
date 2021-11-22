# -*- coding: utf-8 -*-
"""
Created on Fri Oct 15 13:45:37 2021

@author: jubis
"""

from datetime import date
from nsepy import get_history
sbin = get_history(symbol='SBIN',
                   start=date(2021,10,1),
                   end=date(2021,10,10))

print(sbin)


to_date = datetime.now()
to_date = datetime.strftime(to_date,'%Y,%m,%d')
from_date=to_date-dateutil.relativedelta.relativedelta(days=30)
print(to_date)
to_date = datetime.now()
print(to_date)
hist_data = get_history(symbol=stock_symbol,
                   start=to_date,
                   end=from_date)
print(hist_data)
