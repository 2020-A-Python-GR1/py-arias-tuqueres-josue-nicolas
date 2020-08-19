# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 19:14:04 2020

@author: Nicolas
"""


import pandas as pd

#LAPTOP
#path_pickle = r"D:\Nicolas\7 SEMESTRE\Github\py-arias-tuqueres-josue-nicolas\03 - pandas\data\artwork_data.pickle"

#PC DE ESCRITORIO
path_pickle = r"D:\NICOLAS\EPN\7 SEMESTRE\Github\py-arias-tuqueres-josue-nicolas\03 - pandas\data\artwork_data.pickle"


df = pd.read_pickle(path_pickle)


filtrado_filas = df.loc[1035] # SERIE
print(filtrado_filas)
print(filtrado_filas.index) # Indices columnas


filtrado_columnas = df["artist"]
print(filtrado_columnas)
print(filtrado_columnas.index) # Indices son los Indices

df_1035 = df[df.index == 1035] # FILTRAR POR ARREGLO VERDADERO Y FALSOS

segundo = df.loc[1035] # FILTRAR POR INDICE (1)

segundo = df.loc[[1035,1036]] # FILTRAR POR ARR INDICES

segundo = df.loc[3:5] #FILTRAR DESDE x INDICE HASTA y INDICE

segundo = df.loc[1035, "artist"] #1 indice

segundo = df.loc[1035, ["artist", "medium"]] #VARIOS INDICES

#print(df.loc[0]) #INDICE DENTRO DEL DATAFRAME

#print(df[0]) #INDICE DENTRO DEL DATAFRAME



tercero = df.iloc[1]

tercero = df.iloc[[0,1]]

tercero = df.iloc[0:10]

tercero = df.iloc[df.index == 1035]

tercero = df.iloc[0:10, 0:3] #Filtrado por indices, po rango de indices 0:4

###################################

datos = {
    "nota 1":{
        "pepito":7,
        "juanita":8,
        "maria":9
        },
    "nota 2":{
        "pepito":6,
        "juanita":10,
        "maria":6
        },
    "disciplina":{
        "pepito":4,
        "juanita":9,
        "maria":2
        }
    }

notas = pd.DataFrame(datos)


condicion_nota_1 = notas["nota 1"] <= 7

condicion_nota_2 = notas["nota 2"] <= 7

condicion_disc = notas["disciplina"] <= 7

mayores_siete = notas.loc[condicion_nota_1] #TODAS LAS COLUMNAS

mayores_siete = notas.loc[condicion_nota_1, ["nota 1"]] #SOLO COLUMNA NOTA 1

pasaron = notas.loc[condicion_nota_1][condicion_disc][condicion_nota_2]

notas.loc["maria","disciplina"] = 10

notas.loc[:,"disciplina"] = 10


######## PROMEDIO DE LAS # NOTAS (no1 + no2 + disc) / 3

promedio_notas = notas.sum(axis = 1) / 3










