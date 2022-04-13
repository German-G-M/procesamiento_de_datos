# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 23:17:24 2022

@author: germa
"""

#PUNTO 3
#3 algoritmos de preprocesamiento
import pandas as pd
import numpy as np
print("mostrando datos desde el archivo Autism-Child-Data.arff ")
datos=pd.read_csv("Autism-Child-Data.csv",sep=",")
print(datos)



#1 primer algoritmo de pre procesamiento: ReplaceMissingValues
print("reemplazando valores vacíos usando SimpleImputer ")
from sklearn.impute import SimpleImputer #importamos la clase simpleImputer
prepro=SimpleImputer(missing_values='?',strategy="mean") #llenamos números
prepro2=SimpleImputer(missing_values='?',strategy="moda") #llenamos caractéres
x1=np.array(datos["age"])
print(x1)
#x2=prepro.fit_transform(x1)
#print (x2)


#2 segundo algoritmo de pre procesamiento: Discretizer
print("Dividimos los datos en grupos con KBinsDiscretizer ")
from sklearn.preprocessing import KBinsDiscretizer
x1=np.array(datos["age"])
print(x1)

preproD=KBinsDiscretizer(n_bins=5,encode="ordinal", strategy='uniform')
#x2=preproD.fit_transform(x1)
#print (x2)



#2 tercer algoritmo de pre procesamiento: MinMaxScaler:normalizado a [0,1]
print("Normalizando a [0,1] con MinMaxScaler ")
from sklearn import preprocessing
x1=np.array(datos["age"])
print(x1)
min_max_scaler=preprocessing.MinMaxScaler()
x_minmax=min_max_scaler.fit_transform(x1)
print(x_minmax)

