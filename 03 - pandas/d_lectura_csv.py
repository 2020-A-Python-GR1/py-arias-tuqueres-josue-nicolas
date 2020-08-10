# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 19:42:19 2020

@author: Nicolas
"""
import pandas as pd
import numpy as np
import os

path = r"D:\Nicolas\7 SEMESTRE\Github\py-arias-tuqueres-josue-nicolas\03 - pandas\data\artwork_data.csv"

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
    #nrows=10,
    usecols = columnas,
    index_col = "id")


path_pickle = r"D:\Nicolas\7 SEMESTRE\Github\py-arias-tuqueres-josue-nicolas\03 - pandas\data\artwork_data.pickle"


df3.to_pickle(path_pickle)


df5 = pd.read_pickle(path_pickle)






mylist = list('abcedfghijklmnopqrstuvwxyz')
myarr = np.arange(26)
mydict = dict(zip(mylist, myarr))
ser = pd.Series(mydict) 
df1 = pd.DataFrame(ser)














