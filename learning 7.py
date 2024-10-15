#Bitcoin et time series 
import numpy as np
import matplotlib.pyplot as plt 
import pandas as pd 

bitcoin=pd.read_csv('BTC-EUR.csv', index_col='Date', parse_dates=True)     

#bitcoin['Close'].plot(figsize=(9,6))
#si on veut juste 2019, on peut faire : 
#bitcoin['2023']['Close'].plot(figsize=(9,6))
#bitcoin['2023-02']['Close'].plot(figsize=(9,6))
#bitcoin['2023-02':'2023-04']['Close'].plot(figsize=(9,6))
#bitcoin.loc['2023-02':'2023-04','Close'].plot(figsize=(9,6))

#On peut ajouter des dates : 
#bitcoin.loc['2022','Close'].resample('M').std().plot()

# le std est utilisé pour voir à quel niveau le truc est volatille


# si on  veut faire une analyse de l'année 2022
#plt.figure(figsize=(12,8))
#bitcoin.loc['2022','Close'].plot()
#bitcoin.loc['2022','Close'].resample('M').mean().plot(label='Moyenne par mois',lw=3, ls=':',alpha=0.8)                                                                    
#bitcoin.loc['2022','Close'].resample('W').mean().plot(label='Moyenne par semaine',lw=3, ls='--',alpha=0.8)                             
#plt.legend()
#plt.show()

#var_stat=bitcoin['Close'].resample('W').agg(['mean','std','min','max'])
plt.figure(figsize=(12,8))
#var_stat['mean'].plot(label='moyenne par semaine')
#plt.fill_between(var_stat.index, var_stat['max'],var_stat['min'], alpha=0.2, label='min-max par semaine')

#Moving Average
bitcoin.loc['2022-09','Close'].plot()
bitcoin.loc['2022-09','Close'].rolling(window=7).mean().plot(label='moving average',lw=3,ls=':',alpha=0.8)
for i in np.arange(0.2,1,0.2):
   bitcoin.loc['2022-09','Close'].ewm(alpha=i).mean().plot(label=f'ewm{i}',lw=3,ls=':',alpha=0.8)
   

#Moyenne mobile exponentielle
#alpha facteur de lissage 


plt.legend()
plt.show()



