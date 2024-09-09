import Lectura as le
import tkinter as tk
from tkinter import ttk
import BinaryTree as bt
import Node
import AvlTree as lqs
from PIL import ImageTk, Image
from tkinter import PhotoImage

#CLASE PRINCIPAL CONTROLADORA DE INTERFAZ
class MainGUI:
    #CREACION DE INTERFAZ INTERACTIVA, BOTONES Y SU RESPECTIVA PROGRAMACION
    def __init__(self):

        self.gui = tk.Tk()
        self.gui.geometry("1500x1000")
        self.gui.title("AVL SIMULATOR")

        self.optionFrame = tk.Frame(self.gui, bg="#0772D6")
        self.optionFrame.pack(side=tk.LEFT)
        self.optionFrame.pack_propagate(False)
        self.optionFrame.configure(width=200, height=1000)

        self.mainFrame = tk.Frame(self.gui, bg="#0BB6E0", highlightbackground="black", highlightthickness=2)
        self.mainFrame.pack(fill=tk.BOTH, expand=True)
        #BOTON DE PAGINA INICIAL
        self.startBt = tk.Button(self.optionFrame, text = "Inicio", font = ("Bold", 20), fg = "black", bd = 0, bg = "#0772D6", command = self.startFrame)
        self.startBt.place(x = 45 , y = 40)
        self.startLb = tk.Label(self.optionFrame, text = "", bg = "#DEE9F3")
        self.startLb.place(x = 8, y = 35, width = 5, height = 65)
        #BOTON PARA MOSTRAR EL ARBOL AVL
        self.showBt = tk.Button(self.optionFrame, text = "Mostrar", font = ("Bold", 20), fg = "black", bd = 0, bg = "#0772D6", command = lambda: lqs.avl_tree.draw_tree(lqs.avl_tree.root))
        self.showBt.place(x = 45 , y = 180)
        self.showLb = tk.Label(self.optionFrame, text = "", bg = "#0772D6")
        self.showLb.place(x = 8, y = 175, width = 5, height = 65)
        #BOTON DE INSERCION
        self.insertBt = tk.Button(self.optionFrame, text="Insertar", font=("Bold", 20), fg="black", bd=0, bg="#0772D6", command = self.insertFrame)
        self.insertBt.place(x=45, y=320)
        self.insertLb = tk.Label(self.optionFrame, text = "", bg = "#0772D6")
        self.insertLb.place(x = 8, y = 315, width = 5, height = 65)

        #BOTON DE ELIMINACION
        self.deleteBt = tk.Button(self.optionFrame, text="Eliminar", font=("Bold", 20), fg="black", bd=0, bg="#0772D6", command = self.deleteFrame)
        self.deleteBt.place(x=45, y=460)
        self.deleteLb = tk.Label(self.optionFrame, text = "", bg = "#0772D6")
        self.deleteLb.place(x = 8, y = 455, width = 5, height = 65)
        #BOTON DE BUSQUEDA
        self.searchBt = tk.Button(self.optionFrame, text="Buscar", font=("Bold", 20), fg="black", bd=0, bg="#0772D6", command = self.searchFrame)
        self.searchBt.place(x=45, y=600)
        self.searchLb = tk.Label(self.optionFrame, text = "", bg = "#0772D6")
        self.searchLb.place(x = 8, y = 595, width = 5, height = 65)
        #BOTON DE CIERRE
        self.closeBt = tk.Button(self.optionFrame, text="Cerrar", font=("Bold", 20), fg="black", bd=0, bg="#0772D6", command = self.close )
        self.closeBt.place(x=40, y=740)
        self.closeLb = tk.Label(self.optionFrame, text = "", bg = "#0772D6")
        self.closeLb.place(x = 8, y = 735, width = 5, height = 65)

        self.startFrame()
        self.gui.mainloop()

    def close(self):
        self.indicate(self.closeLb)
        self.gui.destroy()

    def hideIndicate(self):
        self.startLb.config(bg="#0772D6")
        self.showLb.config(bg="#0772D6")
        self.insertLb.config(bg="#0772D6")
        self.deleteLb.config(bg="#0772D6")
        self.searchLb.config(bg="#0772D6")
        self.closeLb.config(bg="#0772D6")
        

    def indicate(self, lb):
        self.hideIndicate()
        lb.config(bg = "#DEE9F3")

    def deleteFrames(self):
        for frame in self.mainFrame.winfo_children():
            frame.destroy()


    #PAGINA PRINCIPAL DE LA INTERFAZ DE USUARIO
    def startFrame(self):
        self.deleteFrames()
        self.indicate(self.startLb)
        startFrame = tk.Frame(self.mainFrame,bg = "#0BB6E0")
        startFrame.pack(pady=20)
        lb = tk.Label(startFrame, text = "AVL Makers/Haters",font = ("Impact",67, "bold"), bg = "#0BB6E0")
        lb.pack()
        photo = Image.open("data\pixlr-image-generator-8841b930-4fee-4623-9239-bf284689f7d5.png") 
        imagen = ImageTk.PhotoImage(photo) 
        imagenlbl = tk.Label(startFrame, image=imagen)
        imagenlbl.image = imagen
        imagenlbl.pack()

    #FUNCION PARA LA ELIMINACION
    def deleteFrame(self):
        self.deleteFrames()
        self.indicate(self.deleteLb)
        deleteFrame = tk.Frame(self.mainFrame,bg = "#0BB6E0")
        deleteFrame.pack()
        lb = tk.Label(deleteFrame, text = "Eliminar", font = ("Helvetica",67, "bold"), bg = "#0BB6E0")
        lb.pack(pady=60)

        texteliminar = tk.Entry(deleteFrame,width=30,font=("Arial",40))
        texteliminar.pack(pady=80)

        eliminar = tk.Button(deleteFrame, text="Eliminar", font = ("Times New Roman", 25), borderwidth= 20, command= lambda: lqs.avl_tree.delete(texteliminar.get()))
        eliminar.pack(pady=10)
        

    #FUNCION PARA INSERTAR DATOS DEL DATASET (PELICULAS)
    def insertFrame(self):
        self.deleteFrames()
        self.indicate(self.insertLb)
        insertFrame = tk.Frame(self.mainFrame,bg = "#0BB6E0")
        insertFrame.pack()

        lb = tk.Label( insertFrame, text = "Insertar", font = ("Helvetica",60, "bold"), bg = "#0BB6E0")
        lb.pack(fill="both", pady = 60)

        text = tk.Entry(insertFrame,width=30,font=("Arial",40))
        text.pack(pady=80)

        insert = tk.Button(insertFrame,  text = "Insertar", font = ("Times New Roman", 25), borderwidth= 20, command= lambda: lqs.avl_tree.insert(le.encontrar(text.get().strip())))
        insert.pack(pady=10)

    #FUNCION PARA BUSCAR DATOS (PELICULAS) UNA VEZ HAN SIDO INGRESADOS EN EL ARBOL AVL
    def searchFrame(self):
        self.deleteFrames()
        self.indicate(self.searchLb)
        searchFrame = tk.Frame(self.mainFrame, bg = "#0BB6E0")
        searchFrame.pack()

        lb = tk.Label(searchFrame, text = "Buscar", font = ("Helvetica",100, "bold"), bg = "#0BB6E0")
        lb.pack(fill="both", pady = 60)

        textBox = tk.Entry(searchFrame,width=30,font=("Arial",40))
        textBox.pack(pady = 80)

        rdBut1 = tk.Button(searchFrame,  text = "Buscar en el Árbol", font = ("Times New Roman", 25), borderwidth= 20,command= lambda: lqs.avl_tree.familiar(textBox.get()))
        rdBut2 = tk.Button(searchFrame,  text="Buscar por Parámetros", font=("Times New Roman", 25), borderwidth= 20, command= self.searchParameter)
        rdBut3 = tk.Button(searchFrame,  text = "Recorrido por Niveles", font = ("Times New Roman", 25), borderwidth= 20,command= lambda: lqs.avl_tree.mostrarNiveles(lqs.avl_tree.root))
        rdBut1.pack(pady=10)
        rdBut2.pack(pady=10)
        rdBut3.pack(pady=10)

    #FUNCION PARA BUSCAR LOS NODOS QUE CUMPLAN LOS CRITERIOS ANTERIORMENTE ESTABLECIDOS EN LA DOCUMENTACION (PUNTO 4)
    def searchParameter(self):
        self.deleteFrames()
        self.indicate(self.searchLb)
        searchIndicate = tk.Frame(self.mainFrame, bg="#0BB6E0")
        searchIndicate.pack()

        lb = tk.Label(searchIndicate, text = "Buscar por Parámetros", font = ("Helvetica",70, "bold"), bg = "#0BB6E0")
        lb.pack(pady=80)

        año = tk.Label(searchIndicate, text = "Año", font = ("Helvetica",25, "bold"), bg = "#0BB6E0")

        text1 = tk.Entry(searchIndicate,width=30,font=("Arial",40))
        text2 = tk.Entry(searchIndicate,width=30, font=("Arial",40))
        text1.pack()
        año.pack(pady=30)
        ingreso = tk.Label(searchIndicate, text = "Ingreso internacionales", font = ("Helvetica",25, "bold"), bg = "#0BB6E0")
        text2.pack(padx=20)
        ingreso.pack(pady=30)
        

        buttonserach = tk.Button(searchIndicate, text="Buscar", font=("Times New Roman", 25), borderwidth= 20, command= lambda: le.mostrar(text1.get(),text2.get(),lqs.avl_tree.root,le.myList) )
        buttonserach.pack(pady=20)   







MainGUI()