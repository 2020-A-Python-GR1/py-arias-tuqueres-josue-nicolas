# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 18:58:04 2020

@author: Nicolas
"""


import pandas as pd

path_pickle = r"D:\Nicolas\7 SEMESTRE\Github\py-arias-tuqueres-josue-nicolas\03 - pandas\data\artwork_data.pickle"


df = pd.read_pickle(path_pickle)


serie_artistas_duplicados = df["artist"]


# SELECCIONAR OBJETOS SIN REPETIR
artistas = pd.unique(serie_artistas_duplicados)

print(type(artistas))

print(artistas.size)


# FILTRAR POR OBJETO
blake = df["artist"] == "Blake, William"

print(blake.value_counts())

df_blake = df[blake]