#panda 
#Analyse des donnÃ©es du Titanic
import numpy as np
import matplotlib.pyplot as plt 
import pandas as pd 


data=pd.read_excel('titanic3.xls')
data=data.drop(['name', 'sibsp','parch','ticket','fare', 'cabin', 'embarked', 'boat','body','home.dest'],axis =1)


#On va éléminer les passagers qui ont un age différent 
data=data.dropna(axis=0)
#data['pclass'].value_counts()

figure=data['pclass'].value_counts()
plt.figure()
data['pclass'].value_counts().plot.bar()
plt.show()
#Moyenne suivant le sexe : 
moy_sex=data.groupby(['sex']).mean()
print(moy_sex)