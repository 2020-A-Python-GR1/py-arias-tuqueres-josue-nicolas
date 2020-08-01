# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 19:42:19 2020

@author: Nicolas
"""
import pandas as pd
import os

path = "./data/artwork_data.csv"

df1 = pd.read_csv(
    path,
    nrows=10)

columnas = ["id", "artist", "title", "medium", "year", 
            "acquisitionYear", "height", "width", "units"]

df2 = pd.read_csv(
    path,
    nrows=10,
    usecols = columnas)

df3 = pd.read_csv(
    path,
    nrows=10,
    usecols = columnas,
    index_col = "id")


pathGuardado = "./data/artwork_data.pickle"


df3.to_pickle(pathGuardado)


df5 = pd.read_pickle(pathGuardado)





















