# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 17:29:42 2019

@author: DELL
"""

import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt
import pandas_datareader as pdr
df = pdr.get_data_yahoo('AAPL', 
                          start=datetime.datetime(2006, 1, 1), 
                          end=datetime.datetime(2019, 10, 1))
df = df['Close']
sma_mean = df.rolling(window=20).mean()
plt.figure(figsize=(12,6))
plt.title('   AAPL Plot      ')
plt.plot(df, label='AAPL', color='orange')
plt.show()
plt.figure(figsize=(12,6))
plt.title('   SMA Plot      ')
plt.plot(sma_mean, label='AAPL 20 Day SMA', color='black')
plt.show()
plt.figure(figsize=(12,6))
plt.title('AAPL and SMA Plot')
plt.plot(df, label='AAPL')
plt.plot(sma_mean, label='AAPL 20 Day SMA', color='magenta')
plt.legend(loc='upper left')
plt.show()
