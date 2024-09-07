import pandas as pd 
import tkinter as tk


prueba = tk.Tk()
prueba.geometry("700x600")
prueba.title("Prueba contenido")

pantalla = tk.Frame(prueba, background="light slate gray")
pantalla.place(x=0,y=0,width=700,height=600)

cuadrotexto=tk.Entry()
cuadrotexto.place(x=200,y=200)

boton = tk.Button(pantalla,text="Buscar",command= lambda: encontrar(cuadrotexto.get()))
boton.place(x=300,y=300)

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

prueba.mainloop()