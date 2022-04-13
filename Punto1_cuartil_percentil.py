# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 19:58:46 2022

@author: germa
"""

#PUNTO 1 
import pandas as pd
import numpy as np
print("mostrando datos desde el archivo Autism-Child-Data.arff ")
datos=pd.read_csv("Autism-Child-Data.csv",sep=",")
print(datos)

# inciso a) QUARTIL 1
'''
El quartil 1 (Q1) es el percentil 25 (P25). El 25% de los datos son menores o iguales a Q1
Formula del 1er cuartil:
(N+1)/4
Nuestro N=292
(N+1)/4 = (292+1)/4 = 293/4 = 73.25

Como es un número decimal el cuartil será un número entre: X73 y  X74
Q1 = X73 + 0.25 *(X74 –X73)

'''

# inciso a) PERCENTIL 50
'''
El quartil 2 (Q2) es el percentil 50 (P50) y es la mediana. El 50% de los datos son menores o iguales a Q2
La fórmula del percentil 50 o lo lo que es lo mismo del quartil 2 o la mediana es:
N/2 + 1
Nuestro N=292
N/2 +1 = 292/2 +1 = 147
Como es un número entero el percentil 50 será: X147 

'''
# inciso b) USANDO NUMPY Y PANDAS

print("calculos del 1 cuartil Q1 (que es lo mismo que el percentil 25)")

print(np.percentile(datos["A1_Score"],25))
print(np.percentile(datos["result"],25))
#print(np.percentile(datos["age"],25)) # manda error porque en los registros hay campos que no tienen edad


print("calculos del percentil 50")
print(np.percentile(datos["A1_Score"],50))
print(np.percentile(datos["result"],50))


# inciso c) GRAFICANDO LOS DATOS
import matplotlib.pyplot as plt 

print("graficando los datos")
valores_x=datos["result"].unique()
valores_y=datos["result"].value_counts().tolist()
print(valores_x,valores_y)
plt.bar(valores_x, valores_y)
#plt.show()

#para poner titulo a la grafica
plt.title("Columna 'result'")
ax=plt.subplot()
ax.set_xticks(valores_x)
ax.set_xticklabels(valores_y)
ax.set_ylabel("eje y") #nombre del eje y
ax.set_xlabel("eje x") #nombre del eje x
plt.show()
