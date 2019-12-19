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
#importing data 
data = pdr.get_data_yahoo('AAPL', 
                          start=datetime.datetime(2006, 1, 1), 
                          end=datetime.datetime(2019, 10, 1))
data = data['Close']
#Finding the mean
sma_mean = data.rolling(window=20).mean()
#Plotting the data
plt.figure(figsize=(12,6))
plt.title('   AAPL Plot      ')
plt.plot(data, label='AAPL', color='orange')
plt.show()
#Plotting the mean
plt.figure(figsize=(12,6))
plt.title('   SMA Plot      ')
plt.plot(sma_mean, label='AAPL 20 Day SMA', color='black')
plt.show()
#Plotting the data and mean together
plt.figure(figsize=(12,6))
plt.title('AAPL and SMA Plot')
plt.plot(data, label='AAPL')
plt.plot(sma_mean, label='AAPL 20 Day SMA', color='magenta')
plt.legend(loc='upper left')
plt.show()
