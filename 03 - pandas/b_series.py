# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 07:57:38 2020

@author: Nicolas
"""

import numpy as np
import pandas as pd

lista_numeros = [1,2,3,4]
tupla_numeros = [1,2,3,4]
np_numeros = np.array([1,2,3,4])

series_a = pd.Series(lista_numeros)
series_b = pd.Series(tupla_numeros)
series_c = pd.Series(np_numeros)

series_d = pd.Series([
    True,
    False,
    12,
    12.2,
    "Nicolas",
    None,
    (1),
    [2],
    {"Nombre":"Nicolas"}])

print(series_d[8]["Nombre"])
print(type(series_d))


lista_ciudades = [
    "Ambato",
    "Cuenca",
    "Loja",
    "Quito"]

serie_cuidad = pd.Series(
    lista_ciudades,
    index = [
        "A",
        "C",
        "L",
        "Q"])

print(serie_cuidad[3])
print(serie_cuidad["Q"])

valores_ciudad = {
    "Ibarra":9500,
    "Guayaquil":10000,
    "Cuenca":7000,
    "Quito":8000,
    "Loja":3000}

serie_valor_ciudad = pd.Series(valores_ciudad)

print(valores_ciudad["Quito"])

ciudades_menor_5k = serie_valor_ciudad < 5000

print(ciudades_menor_5k)

print(type(ciudades_menor_5k))

s5 = serie_valor_ciudad[ciudades_menor_5k]

serie_valor_ciudad *= 1.1

serie_valor_ciudad["Quito"] -= 50

print("Lima" in serie_valor_ciudad)


for x in serie_valor_ciudad:
    print(x)