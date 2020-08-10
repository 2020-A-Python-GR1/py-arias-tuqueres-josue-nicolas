# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 17:10:41 2020

@author: Nicolas
"""

import pandas as pd
import numpy as np
import os
import sqlite3


path_pickle = r"D:\Nicolas\7 SEMESTRE\Github\py-arias-tuqueres-josue-nicolas\03 - pandas\data\artwork_data.pickle"

path = r"D:\Nicolas\7 SEMESTRE\Github\py-arias-tuqueres-josue-nicolas\03 - pandas\data\artwork_data.csv"

df = pd.read_pickle(path_pickle)

sub_df = df.iloc[49980:50519,:].copy()


# Excel #

path_excel = r"D:\Nicolas\7 SEMESTRE\Github\py-arias-tuqueres-josue-nicolas\03 - pandas\data\artwork_data.xlsx"

#Con indice
sub_df.to_excel(path_excel)

#Sin indice
sub_df.to_excel(path_excel, index = False)

#Columnas específicas
columnas = ["artist", "title", "year"]
sub_df.to_excel(path_excel,columns=columnas)

# Multiples hojas de trabajo #

path_excel_mt = r"D:\Nicolas\7 SEMESTRE\Github\py-arias-tuqueres-josue-nicolas\03 - pandas\data\artwork_data_mt.xlsx"

writer = pd.ExcelWriter(path_excel_mt, engine="xlsxwriter")

sub_df.to_excel(writer, sheet_name = "Primera")

sub_df.to_excel(writer, sheet_name = "Segunda")

sub_df.to_excel(writer, sheet_name = "Tercera")

writer.save()

# Formato condicional #

num_artistas = sub_df["artist"].value_counts()

path_excel_colores= r"D:\Nicolas\7 SEMESTRE\Github\py-arias-tuqueres-josue-nicolas\03 - pandas\data\artwork_data_colores.xlsx"

writer = pd.ExcelWriter(path_excel_colores, 
                            engine="xlsxwriter")

num_artistas.to_excel(writer, 
                      sheet_name="Artistas")

hoja_artistas = writer.sheets["Artistas"]

#rango_celdas = "B2:B{}".format(len(num_artistas.index) + 1)

ultimo_numero = len(num_artistas.index) + 1

rango_celdas = f"B2:B{ultimo_numero}"

formato_artistas = {
        "type" : "2_color_scale",
        "min_value" : "10",
        "min_type" : "percentile",
        "max_value" : "99",
        "max_type" : "percentile"}


hoja_artistas.conditional_format(rango_celdas, formato_artistas)



writer.save()





####### SQL ###########

with sqlite3.connect(r"D:\Nicolas\7 SEMESTRE\Github\py-arias-tuqueres-josue-nicolas\03 - pandas\bdd_artist.bdd") as conexion:
   sub_df.to_sql("py_artista", conexion)
    


####### JSON ##################

sub_df.to_json(r"D:\Nicolas\7 SEMESTRE\Github\py-arias-tuqueres-josue-nicolas\03 - pandas\artistas.json")

sub_df.to_json(r"D:\Nicolas\7 SEMESTRE\Github\py-arias-tuqueres-josue-nicolas\03 - pandas\artistas_tabla.json", orient="table")






















