# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 17:04:04 2022

@author: germa
"""
#PREGUNTA 4 DEL EXAMEN
#construya la dependencia de Abuelos, tios, padres, primos e hijos de su familia.
'''
abuelos: Francisco, Vicente
tios: Martha, Guido
padres: Marco, Rosa
hijos: German, Vanesa
primos: Hector, Luis
'''

from kanren import run, var, eq, Relation, facts
#run-->asignacion
#var ---> variable
#eq ---> igualdad
a=var()
b=var()

print("Relacion de padre")
padre=Relation()
facts(padre, 
      ("Marco","German"),
      ("Marco","Vanesa"),
      ("Francisco","Marco"),
      ("Francisco","Martha"),
      ("Vicente","Guido"),
      ("Vicente","Rosa"),
      ("Guido","Luis"),
      ("Martha","Hector"))
print(padre.facts)

m=var()
n=var()
print("¿quienes es el hermano de German?")
#hermanos=run(10,(m,n),padre(a,m),padre(a,n) m is not n)
hermanos=run(10,m,padre(a,m),padre(a,"German"))
print(hermanos)

print("*******************************consulta de padres e hijos**********************")

#quiero descubrir quienes padre de cierta persona
print("Realizamos algunas consultas")

print("¿Quien es el papa de German?")
print(run(1,a,padre(a,"German")))

print("quienes son los hijos de Marco?")
print(run(2,b,padre("Marco",b)))

c=var()
d=var()
e=var()

print("¿quienes son hijos?")
print(run(8,c,padre(d,c)))

print("¿quienes son padres?")
print(run(8,d,padre(d,c)))


print("***********************************consulta Abuelos***************************")
print("¿quienes son abuelos?")
print(run(8,c,padre(c,d),padre(d,e)))


print("************************************consulta de tios******************************")
print("¿quienes son tios de GERMAN?")
print(run(8,d,padre(a,"German"),padre(b,a),padre(b,d)))


print("************************************consulta de primos****************************")
print("Quienes son primos de GERMAN?")
print(run(8,c,padre(a,"German"),padre(b,c),padre(d,a),padre(d,b)))
