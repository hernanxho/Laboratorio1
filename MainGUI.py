import Lectura as le
import tkinter as tk
from tkinter import ttk
import BinaryTree as bt
import PruebaArbol as pb


class MainGUI:
    def __init__(self):

        self.gui = tk.Tk()
        self.gui.geometry("1500x1000")
        self.gui.title("EN PROCESO")

        self.optionFrame = tk.Frame(self.gui, bg="#0772D6")
        self.optionFrame.pack(side=tk.LEFT)
        self.optionFrame.pack_propagate(False)
        self.optionFrame.configure(width=200, height=1000)

        self.mainFrame = tk.Frame(self.gui, bg="#0BB6E0", highlightbackground="black", highlightthickness=2)
        self.mainFrame.pack(fill=tk.BOTH, expand=True)

        self.startBt = tk.Button(self.optionFrame, text = "Inicio", font = ("Bold", 20), fg = "black", bd = 0, bg = "#0772D6", command = self.startFrame)
        self.startBt.place(x = 45 , y = 40)
        self.startLb = tk.Label(self.optionFrame, text = "", bg = "#DEE9F3")
        self.startLb.place(x = 8, y = 35, width = 5, height = 65)

        self.showBt = tk.Button(self.optionFrame, text = "Mostrar", font = ("Bold", 20), fg = "black", bd = 0, bg = "#0772D6", command = self.showFrame)
        self.showBt.place(x = 45 , y = 180)
        self.showLb = tk.Label(self.optionFrame, text = "", bg = "#0772D6")
        self.showLb.place(x = 8, y = 175, width = 5, height = 65)

        self.insertBt = tk.Button(self.optionFrame, text="Insertar", font=("Bold", 20), fg="black", bd=0, bg="#0772D6", command = self.insertFrame)
        self.insertBt.place(x=45, y=320)
        self.insertLb = tk.Label(self.optionFrame, text = "", bg = "#0772D6")
        self.insertLb.place(x = 8, y = 315, width = 5, height = 65)


        self.deleteBt = tk.Button(self.optionFrame, text="Eliminar", font=("Bold", 20), fg="black", bd=0, bg="#0772D6", command = self.deleteFrame)
        self.deleteBt.place(x=45, y=460)
        self.deleteLb = tk.Label(self.optionFrame, text = "", bg = "#0772D6")
        self.deleteLb.place(x = 8, y = 455, width = 5, height = 65)

        self.searchBt = tk.Button(self.optionFrame, text="Buscar", font=("Bold", 20), fg="black", bd=0, bg="#0772D6", command = self.searchFrame)
        self.searchBt.place(x=45, y=600)
        self.searchLb = tk.Label(self.optionFrame, text = "", bg = "#0772D6")
        self.searchLb.place(x = 8, y = 595, width = 5, height = 65)

        self.infoBt = tk.Button(self.optionFrame, text="¡Conócenos!", font=("Bold", 20), fg="black", bd=0, bg="#0772D6", command = self.infoFrame)
        self.infoBt.place(x=20, y=740)
        self.infoLb = tk.Label(self.optionFrame, text = "", bg = "#0772D6")
        self.infoLb.place(x = 8, y = 735, width = 5, height = 65)

        self.closeBt = tk.Button(self.optionFrame, text="Cerrar", font=("Bold", 20), fg="black", bd=0, bg="#0772D6", command = self.close )
        self.closeBt.place(x=45, y=880)
        self.closeLb = tk.Label(self.optionFrame, text = "", bg = "#0772D6")
        self.closeLb.place(x = 8, y = 875, width = 5, height = 65)

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
        self.infoLb.config(bg = "#0772D6")
        self.closeLb.config(bg="#0772D6")
        

    def indicate(self, lb):
        self.hideIndicate()
        lb.config(bg = "#DEE9F3")

    def deleteFrames(self):
        for frame in self.mainFrame.winfo_children():
            frame.destroy()



    def startFrame(self):
        self.deleteFrames()
        self.indicate(self.startLb)
        startFrame = tk.Frame(self.mainFrame,bg = "#0BB6E0")
        lb = tk.Label(startFrame, text = "Main Title",font = ("Helvetica",67, "bold"), bg = "#0BB6E0")
        lb.pack()
        startFrame.pack(pady=20)

    def showFrame(self):
        self.deleteFrames()
        self.indicate(self.showLb)
        showFrame = tk.Frame(self.mainFrame,bg = "#0BB6E0")
        lb = tk.Label(showFrame, text = "Mostrar", font = ("Helvetica",67, "bold"), bg = "#0BB6E0")
        lb.pack()
        showFrame.pack(pady=20)
    
    def deleteFrame(self):
        self.deleteFrames()
        self.indicate(self.deleteLb)
        deleteFrame = tk.Frame(self.mainFrame,bg = "#0BB6E0")
        lb = tk.Label(deleteFrame, text = "Eliminar", font = ("Helvetica",67, "bold"), bg = "#0BB6E0")
        lb.pack()
        deleteFrame.pack(pady=20)


    def insertFrame(self):
        self.deleteFrames()
        self.indicate(self.insertLb)
        insertFrame = tk.Frame(self.mainFrame,bg = "#0BB6E0")
        insertFrame.pack()

        lb = tk.Label( insertFrame, text = "Insertar", font = ("Helvetica",60, "bold"), bg = "#0BB6E0")
        lb.pack(fill="both", pady = 60)

        text = tk.Entry(insertFrame,width=30,font=("Arial",40))
        text.pack(pady=80)

        insert = tk.Button(insertFrame,  text = "Insertar", font = ("Times New Roman", 25), borderwidth= 20, command= lambda: pb.tree.insert(text.get()) and pb.printRoot(pb.tree.root))
        insert.pack(pady=10)


    def searchFrame(self):
        self.deleteFrames()
        self.indicate(self.searchLb)
        searchFrame = tk.Frame(self.mainFrame, bg = "#0BB6E0")
        searchFrame.pack()

        lb = tk.Label(searchFrame, text = "Buscar", font = ("Helvetica",100, "bold"), bg = "#0BB6E0")
        lb.pack(fill="both", pady = 60)

        textBox = tk.Entry(searchFrame,width=30,font=("Arial",40))
        textBox.pack(pady = 80)

        rdBut1 = tk.Button(searchFrame,  text = "Buscar en el árbol", font = ("Times New Roman", 25), borderwidth= 20)
        rdBut2 = tk.Button(searchFrame,  text="Buscar en cartelera", font=("Times New Roman", 25), borderwidth= 20,command= lambda: le.encontrar(textBox.get()))
        rdBut1.pack(pady = 10)
        rdBut2.pack(pady=10)



    def infoFrame(self):
        self.deleteFrames()
        self.indicate(self.infoLb)
        infoFrame = tk.Frame(self.mainFrame,bg = "#0BB6E0")
        lb = tk.Label(self.mainFrame, text = "¡Conócenos!", font = ("Helvetica",67, "bold"), bg = "#0BB6E0")
        lb.pack()
        infoFrame.pack(pady=20)





MainGUI()