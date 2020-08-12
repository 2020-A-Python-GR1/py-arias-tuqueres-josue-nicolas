# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 19:14:04 2020

@author: Nicolas
"""


import pandas as pd

path_pickle = r"D:\Nicolas\7 SEMESTRE\Github\py-arias-tuqueres-josue-nicolas\03 - pandas\data\artwork_data.pickle"

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

tercero = df.iloc[0:10, 0:3]













