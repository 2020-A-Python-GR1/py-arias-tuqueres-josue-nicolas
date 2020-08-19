# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 19:30:24 2020

@author: Nicolas
"""


import pandas as pd
import math
import numpy as np

#LAPTOP
#path_pickle = r"D:\Nicolas\7 SEMESTRE\Github\py-arias-tuqueres-josue-nicolas\03 - pandas\data\artwork_data.pickle"

#PC DE ESCRITORIO
path_pickle = r"D:\NICOLAS\EPN\7 SEMESTRE\Github\py-arias-tuqueres-josue-nicolas\03 - pandas\data\artwork_data.pickle"


df = pd.read_pickle(path_pickle)

seccion_df = df.iloc[49980:50019,:].copy()

df_agrupar_artista = seccion_df.groupby("artist")

for columna, df_agrupado in df_agrupar_artista:
    print(type(columna))
    print(columna)
    print(type(df_agrupado))
    print(df_agrupado)
    
#Hacer calculos en columnas del df

a = seccion_df["units"].value_counts() #38 (mm) y 1 nan

#VERIFICAR SI LA COLUMNA ESTA VACÍA 
print(seccion_df["units"].empty)
print(a.empty)
    
print(seccion_df["units"].value_counts().argmax())
print(seccion_df["units"].mode().iloc[0])


def llenar_valores_vacios(series, tipo):
    lista_valores = series.value_counts()
    
    if(lista_valores.empty == True):
        return series
    else:
        if(tipo == "promedio"):
            suma = 0
            numero_valores = 0
            for valor_serie in series:
                if(isinstance(valor_serie,str)):
                    valor = int(valor_serie)
                    numero_valores = numero_valores + 1
                    suma = suma + valor
                else:
                    pass
            promedio = suma / numero_valores
            series_valores_llenos = series.fillna(promedio)
            return series_valores_llenos
        if(tipo == "mas_repetido"):
            valor_mas_repetido = series.mode().iloc[0]
            series_valores_llenos = series.fillna(valor_mas_repetido)
            return series_valores_llenos

    
def transformar_df(df):
    df_artist = df.groupby("artist")
    lista_df = []
    for artista, df in df_artist:
        copia_df = df.copy()
        serie_w = copia_df["width"]
        serie_h = copia_df["height"]
        serie_u = copia_df["units"]
        serie_t = copia_df["title"]
        copia_df.loc[:,"width"] = llenar_valores_vacios(
            serie_w, 
            "promedio")
        
        copia_df.loc[:,"height"] = llenar_valores_vacios(
            serie_h, 
            "promedio")
        
        copia_df.loc[:,"units"] = llenar_valores_vacios(
            serie_u, 
            "mas_repetido")
        
        copia_df.loc[:,"title"] = llenar_valores_vacios(
            serie_t, 
            "mas_repetido")
        lista_df.append(copia_df)
    df_completo = pd.concat(lista_df)
    return df_completo


df_lleno = transformar_df(seccion_df)
    
    
    
    
    
    
    
    
    
    
    
    
    



