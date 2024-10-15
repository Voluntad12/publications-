#Assembler deux datasets 
import numpy as np
import matplotlib.pyplot as plt 
import pandas as pd 
bitcoin=pd.read_csv('BTC-EUR.csv', index_col='Date', parse_dates=True)     
etherium=pd.read_csv('ETH-EUR.csv', index_col='Date', parse_dates=True) 
pd.merge(bitcoin,etherium,on='date',)