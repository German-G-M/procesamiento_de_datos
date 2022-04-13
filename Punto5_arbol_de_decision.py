# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 00:13:54 2022

@author: germa
"""

#punto5 ARBOL DE DECISION
#Para esto vamos a necesitar: “graphviz” y “pydotplus” 
#los instalamos con: conda install ....

import pandas as pd
import numpy as np


from sklearn.tree import export_graphviz
#from sklearn.externals.six import StringIO
#from IPython.display import image
#import pydotplusdot_data=StringIO()


import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree

print("mostrando datos desde el archivo Autism-Child-Data.arff ")
datos=pd.read_csv("Autism-Child-Data.csv",sep=",")
print(datos)

df=pd.DataFrame(datos["result"],columns=datos.feature_names)
df["result"]=datos.result

#dividiendo los datos en 75% para el "training" y 25% para el "test"

X_train,X_test,Y_train,Y_test=train_test_split(df[datos.features_names],df['target'],random_state=0)