import pandas as pd #Analisis y limpieza de datos
import numpy as nu
import matplotlib.pyplot as mt

data = pd.read_csv("dataset_transacc_tdc_tdd_20230309.csv")


f_edad = (data["edad_cliente"]>12) & (data["edad_cliente"]<100)
data = data[(data["edad_cliente"]>12) & (data["edad_cliente"]<100)]

frecuencia_giro= data['giro_nombre'].value_counts()
frecuencia_giro.plot.bar(rot=90, title="")