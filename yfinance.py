# -*- coding: utf-8 -*-
"""
Created on Fri Oct 15 15:20:10 2021

@author: jubis
"""

# Import yfinance package
import yfinance as yf

# Set the start and end date
start_date = '1990-01-01'
end_date = '2021-07-12'

# Set the ticker
ticker = 'AMZN'

# Get the data
data = yf.download(ticker, start_date, end_date)

# Print 5 rows
data.tail()