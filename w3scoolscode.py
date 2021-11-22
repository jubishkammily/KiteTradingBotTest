# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 01:27:07 2021

@author: Jubish
"""

import pandas as pd

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

#load data into a DataFrame object:
df = pd.DataFrame(data)

print(df.iloc[1:2,0:2]) 
