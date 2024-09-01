import tkinter as tk
from tkinter.ttk import Button

import SearchGUI as SG
from idlelib.undo import Command


class MainGUI:
    def __init__(self):
        self.gui = tk.Tk()
        self.gui.geometry("1500x1000")
        self.gui.title("EN PROCESO")

        self.optionFrame = tk.Frame(self.gui, bg = "#0772D6")
        self.optionFrame.pack(side = tk.LEFT)
        self.optionFrame.pack_propagate(False)
        self.optionFrame.configure(width = 200, height = 1000)


        self.mainFrame = tk.Frame(self.gui,bg ="#0BB6E0", highlightbackground = "black", highlightthickness =2 )
        self.mainFrame.pack(fill = tk.BOTH, expand = True)

        self.startBt = tk.Button(self.optionFrame, text = "Inicio", font = ("Bold", 20), fg = "black", bd = 0, bg = "#0772D6", command = self.start)
        self.startBt.place(x = 45 , y = 40)
        self.startLb = tk.Label(self.optionFrame, text = "", bg = "#DEE9F3")
        self.startLb.place(x = 8, y = 35, width = 5, height = 65)

        self.showBt = tk.Button(self.optionFrame, text = "Mostrar", font = ("Bold", 20), fg = "black", bd = 0, bg = "#0772D6", command = self.showFrame)
        self.showBt.place(x = 45 , y = 180)
        self.showLb = tk.Label(self.optionFrame, text = "", bg = "#0772D6")
        self.showLb.place(x = 8, y = 175, width = 5, height = 65)

        self.insertBt = tk.Button(self.optionFrame, text="Insertar", font=("Bold", 20), fg="black", bd=0, bg="#0772D6", command = self.insert)
        self.insertBt.place(x=45, y=320)
        self.insertLb = tk.Label(self.optionFrame, text = "", bg = "#0772D6")
        self.insertLb.place(x = 8, y = 315, width = 5, height = 65)


        self.deleteBt = tk.Button(self.optionFrame, text="Eliminar", font=("Bold", 20), fg="black", bd=0, bg="#0772D6", command = self.delete)
        self.deleteBt.place(x=45, y=460)
        self.deleteLb = tk.Label(self.optionFrame, text = "", bg = "#0772D6")
        self.deleteLb.place(x = 8, y = 455, width = 5, height = 65)

        self.searchBt = tk.Button(self.optionFrame, text="Buscar", font=("Bold", 20), fg="black", bd=0, bg="#0772D6", command = self.search)
        self.searchBt.place(x=45, y=600)
        self.searchLb = tk.Label(self.optionFrame, text = "", bg = "#0772D6")
        self.searchLb.place(x = 8, y = 595, width = 5, height = 65)

        self.infoBt = tk.Button(self.optionFrame, text="¡Conócenos!", font=("Bold", 20), fg="black", bd=0, bg="#0772D6", command = self.info)
        self.infoBt.place(x=20, y=740)
        self.infoLb = tk.Label(self.optionFrame, text = "", bg = "#0772D6")
        self.infoLb.place(x = 8, y = 735, width = 5, height = 65)

        self.closeBt = tk.Button(self.optionFrame, text="Cerrar", font=("Bold", 20), fg="black", bd=0, bg="#0772D6", command = self.close )
        self.closeBt.place(x=45, y=880)
        self.closeLb = tk.Label(self.optionFrame, text = "", bg = "#0772D6")
        self.closeLb.place(x = 8, y = 875, width = 5, height = 65)


        self.mainTitle = tk.Label(self.mainFrame, text = "Main Title",font = ("Helvetica",67, "bold"), bg = "#0BB6E0")
        self.mainTitle.pack()


        self.infoGUI=tk.Frame(self.mainFrame)
        self.infoGUITitle = tk.Label(self.infoGUI, text="INFO", font = ("Times New Roman", 50, "bold"))
        self.infoGUITitle.pack()

        self.gui.mainloop()


    def start(self):
        self.gui.destroy()
        MainGUI()

    def show(self):
        self.indicate(self.showLb)

    def search(self):
        self.indicate(self.searchLb)

    def insert(self):
        self.indicate(self.insertLb)

    def delete(self):
        self.indicate(self.deleteLb)

    def info(self):
        self.indicate(self.infoLb)

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



    def showFrame(self):
        self.deleteFrames()
        self.show()
        showFrame = tk.Frame(self.mainFrame)
        lb = tk.Label(self.mainFrame, text = "Show Title", font = ("Helvetica",67, "bold"), bg = "#0BB6E0")
        lb.pack()
        showFrame.pack(pady=20)

    def deleteFrames(self):
        for frame in self.mainFrame.winfo_children():
            frame.destroy()





MainGUI()