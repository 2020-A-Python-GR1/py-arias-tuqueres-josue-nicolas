# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 08:46:56 2020

@author: Nicolas
"""
import numpy as np
import pandas as pd


arr_pand = np.random.randint(0,10,6).reshape(2,3)

df1 = pd.DataFrame(arr_pand)


s1 = df1[0]

s2 = df1[1]

s3 = df1[2]

df1[3] = s1

df1[4] = s1 * s2

datos_fisicos_uno = pd.DataFrame(
    arr_pand,
    columns = [
        'Estatura(cm)',
        'Peso (kg)',
        'Edad (anios)'
    ],
    index =[
        'Josue',
        'Nicolas'
        ])

serie_peso = datos_fisicos_uno['Peso (kg)']

datos_josue = serie_peso['Josue']

print(serie_peso)
print(datos_josue)


df1.index = ['Arias', 'Tuqueres']

df1.columns = ['A', 'B', 'C', 'D', 'E']
















