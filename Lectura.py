import pandas as pd 
import tkinter as tk


df = pd.read_csv("./data/dataset_movies.csv")


def encontrar(pelicula):
 encontrado = False
 for index, row in df.iterrows():
    title = row['Title']
    if(pelicula.lower()==title.lower()):
     print("Pelicula Encontrada " + title)
     encontrado = True
 if(encontrado== False):
   print("Pelicula no encontrada")

