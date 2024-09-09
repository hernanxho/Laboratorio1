import pandas as pd 
from BinaryTree import *
from Node import *
from tkinter import messagebox

df = pd.read_csv("./data/dataset_movies.csv")



def encontrar(pelicula):
 encontrado = False
 for index, row in df.iterrows():
    title = row['Title']
    if(pelicula.lower()==title.lower()):
     print("Pelicula Encontrada " + title)
     encontrado = True
     return title
 if(encontrado== False):
   print("Pelicula no encontrada")
   return ""
myList=[] 
def busqueda(año,valor,node,myList):
  if node is not None: 
   for index,row in df.iterrows():
     title = row['Title']
     year = row['Year']
     ingresoInternacional = row['Foreign Earnings']
     domesticP = row['Domestic Percent Earnings']
     internationalP= row['Foreign Percent Earnings']
     valor = int(valor)
     año=int(año)
     if((node.data.lower()==title.lower()) and (año == year) and (domesticP < internationalP) and (ingresoInternacional>=valor)):
       myList.append(title)
   busqueda(año,valor,node.left,myList)
   busqueda(año,valor,node.right,myList)

 
   
def mostrar(año,valor,node,myList):
 busqueda(año,valor,node,myList)
 message=""
 for i in myList:
   message= message+i+"\n"
 messagebox.showinfo("Peliculas","Lista peliculas:\n " +message)
 myList.clear()
