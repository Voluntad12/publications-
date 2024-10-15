#panda 
#Analyse des donnÃ©es du Titanic
import numpy as np
import matplotlib.pyplot as plt 
import pandas as pd 


data=pd.read_excel('titanic3.xls')
#data=data.dropna(axis=0)
#on veut indexer la data par nom 
data=data.drop(['name', 'sibsp','parch','ticket','fare', 'cabin', 'embarked', 'boat','body','home.dest'],axis =1)
#on peut assembler les séries s'ils contiennt l=meme

#data[['age','pclass']]


# on veut obtenir des ages indéxés par des noms
data=data.dropna(axis=0)
#data=data[data['age']<18]
#on a gardé ceux dont l'age est inférieur à 18
almer=data[data['age']<18]['pclass'].value_counts()
print(almer)
#almer nous donnne le nombre des enfants dont l'age est inf à 18 selon leur classe
# Et si on veut toujours avoir la moyenne selon le sexe et la classe des survivants 
surviv_class_sex= data[data['age']<18].groupby(['sex','pclass']).mean()
#iloc= index localisation et loc
#iloc c'est pour les colonnes 
#data.loc[0:2,['age','sex']]





