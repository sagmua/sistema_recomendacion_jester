# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 18:41:31 2019

@author: samuel
"""

# Importamos las librerías necesarias
import pandas as pd
import numpy as np



#nuevo dataset para guardar el número de valoraciones, la valoración, la película, y los usuarios.
#def asignaValoraciones(usuario):
    

#funcion para transformar el dataframe

if (__name__ == "__main__"):
    
    # Leemos el archivo mediante Pandas:
    jokes = pd.read_csv("jester_ratings.dat", sep = '\t\t', header = None)
    jokes.columns = ['users', 'jokes', 'rate']
    jokes = jokes[jokes['jokes']<=100]
    jokes = jokes.iloc[1:67176,:]
    
    
    #Obtenemos los usurios y los almacenamos en un dataframe vacío:
    index = pd.unique(jokes.iloc[:,0])
    column_names = list(map(str, range(1,101)))
    column_names = ["users"]+ column_names
    valoraciones = pd.DataFrame(index = index, columns = column_names)
    valoraciones['users'] = index
    
    for x in range(1,len(index)):
        jok_rated = jokes.loc[jokes['users']==x, 'jokes']
        rates = jokes.loc[jokes['users']==x, 'rate']
        valoraciones.iloc[x-1,jok_rated] = rates.values.tolist()
        
    count_nan = pd.DataFrame(data = valoraciones.isnull().sum(axis= 1), columns = ['count_NAN'])
    valoraciones = pd.concat([valoraciones, count_nan], axis=1)
    
    #Solo aceptamos valoraciones de usuarios que hayan valorado al menos 
    #el 10% de los chistes:
    
    valoraciones_10 = valoraciones[valoraciones.count_NAN <=90]
    usuarios_index = [x-1 for x in valoraciones_10.users.tolist()]
    
    #eliminamos la columna con el num. de NAN:
    valoraciones = valoraciones.drop('count_NAN', axis = 1)
    valoraciones_10 = valoraciones_10.drop('count_NAN', axis = 1)
    
    #Pasamos a formato CSV para tratarlo con R:
    valoraciones_10.to_csv("valoraciones_10.csv")

