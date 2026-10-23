import pandas as pd
import numpy as np 
# Cristopher Lopez Nc 1374
n_filas = 5 
n_columnas = 5
tag_columna = tuple('ABCDE') # etiqueta para las columnas de una tuplas
print(tag_columna)
matriz = np.random.randint(1,7, size=(n_filas, n_columnas))
print("Genera matriz de 5 filas por 5 columnas")
print("Con numeros comprendidos entre 1 y 10")
print(matriz) 
# la variable df es DataFrame 
df = pd.DataFrame(matriz,columns=tag_columna)
print("---La tabla o dataframe-----Nc 1374")
print(df)
print(" Cristopher Lopez Nc 1374")