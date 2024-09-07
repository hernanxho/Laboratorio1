import tkinter as tk
from tkinter import ttk

class startFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(self,parent)

        parent.indicate(parent.startLb)
        lb = tk.Label(self, text="Main Title", font=("Helvetica", 67, "bold"), bg="#0BB6E0")
        lb.pack()
        startFrame.pack(pady=20)

class showFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(self, parent)

        parent.indicate(parent.showLb)
        lb = tk.Label(self, text="Mostrar", font=("Helvetica", 67, "bold"), bg="#0BB6E0")
        lb.pack()
        showFrame.pack(pady=20)

class insertFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(self, parent)

        parent.indicate(parent.insertLb)
        lb = tk.Label(self, text="Insertar", font=("Helvetica", 67, "bold"), bg="#0BB6E0")
        lb.pack()
        insertFrame.pack(pady=20)

class deleteFrame(tk.Frame):
    def __init__(self, parent ):
        super().__init__(self, parent)

        parent.indicate(parent.deleteLb)
        lb = tk.Label(self, text = "Eliminar", font = ("Helvetica",67, "bold"), bg = "#0BB6E0")
        lb.pack()
        deleteFrame.pack(pady=20)

class searchFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(self,parent)

        lb = tk.Label(self, text="Buscar", font=("Helvetica", 100, "bold"), bg="#0BB6E0")
        lb.pack(fill="both", pady=60)

        textBox = tk.Text(self, font=("Arial", 20), height=3, insertbackground="#0BB6E0", wrap=tk.WORD)
        textBox.pack(pady=80)

        rdVar = tk.IntVar
        rdBut1 = tk.Radiobutton(self, variable=rdVar, text="Buscar en el árbol", font=("Times New Roman", 25),
                                borderwidth=20, value=0, command=self.showMessage)
        rdBut2 = tk.Radiobutton(self, variable=rdVar, text="Buscar en cartelera", font=("Times New Roman", 25),
                                borderwidth=20, value=1, command=lambda: self.showMessage(textBox.get()))
        rdBut1.pack(pady=10)
        rdBut2.pack(pady=10)
        button = tk.Button(self, text="Buscar Película", relief="raised", font=("Times New Roman", 40))
        button.pack(pady=30)

    def showMessage(self, p):
        print (p)
        pass

class infoFrame(tk.Frame):
    def __init__(self,parent):
        super().__init__(self,parent)

        parent.indicate(parent.startLb, self)
        lb = tk.Label(self, text = "¡Conócenos!", font = ("Helvetica",67, "bold"), bg = "#0BB6E0")
        lb.pack()
        infoFrame.pack(pady=20)



class MainGUI:
    def __init__(self):


        gui = tk.Tk()
        gui.geometry("1500x1000")
        gui.title("EN PROCESO")

        optionFrame = tk.Frame(gui, bg="#0772D6")
        optionFrame.pack(side=tk.LEFT)
        optionFrame.pack_propagate(False)
        optionFrame.configure(width=200, height=1000)

        mainFrame = tk.Frame(gui, bg="#0BB6E0", highlightbackground="black", highlightthickness=2)
        mainFrame.pack(fill=tk.BOTH, expand=True)

        self.frameList = [searchFrame(mainFrame), infoFrame(mainFrame)]
        self.frameList[1].forget()

        startBt = tk.Button(optionFrame, text = "Inicio", font = ("Bold", 20), fg = "black", bd = 0, bg = "#0772D6", command = self.startFrame)
        startBt.place(x = 45 , y = 40)
        startLb = tk.Label(optionFrame, text = "", bg = "#DEE9F3")
        startLb.place(x = 8, y = 35, width = 5, height = 65)

        showBt = tk.Button(optionFrame, text = "Mostrar", font = ("Bold", 20), fg = "black", bd = 0, bg = "#0772D6", command = self.showFrame)
        showBt.place(x = 45 , y = 180)
        showLb = tk.Label(optionFrame, text = "", bg = "#0772D6")
        showLb.place(x = 8, y = 175, width = 5, height = 65)

        insertBt = tk.Button(optionFrame, text="Insertar", font=("Bold", 20), fg="black", bd=0, bg="#0772D6", command = self.insertFrame)
        insertBt.place(x=45, y=320)
        insertLb = tk.Label(optionFrame, text = "", bg = "#0772D6")
        insertLb.place(x = 8, y = 315, width = 5, height = 65)


        deleteBt = tk.Button(optionFrame, text="Eliminar", font=("Bold", 20), fg="black", bd=0, bg="#0772D6", command = self.deleteFrame)
        deleteBt.place(x=45, y=460)
        deleteLb = tk.Label(optionFrame, text = "", bg = "#0772D6")
        deleteLb.place(x = 8, y = 455, width = 5, height = 65)

        searchBt = tk.Button(optionFrame, text="Buscar", font=("Bold", 20), fg="black", bd=0, bg="#0772D6", command = self.searchFrame)
        searchBt.place(x=45, y=600)
        searchLb = tk.Label(optionFrame, text = "", bg = "#0772D6")
        searchLb.place(x = 8, y = 595, width = 5, height = 65)

        infoBt = tk.Button(optionFrame, text="¡Conócenos!", font=("Bold", 20), fg="black", bd=0, bg="#0772D6", command = self.infoFrame)
        infoBt.place(x=20, y=740)
        infoLb = tk.Label(optionFrame, text = "", bg = "#0772D6")
        infoLb.place(x = 8, y = 735, width = 5, height = 65)

        closeBt = tk.Button(optionFrame, text="Cerrar", font=("Bold", 20), fg="black", bd=0, bg="#0772D6", command = self.close )
        closeBt.place(x=45, y=880)
        closeLb = tk.Label(optionFrame, text = "", bg = "#0772D6")
        closeLb.place(x = 8, y = 875, width = 5, height = 65)

        self.startFrame()
        gui.mainloop()

    def close(self):
        self.indicate(self.closeLb)
        self.gui.destroy()

    def hideIndicate(self):
        startLb.config(bg="#0772D6")
        showLb.config(bg="#0772D6")
        insertLb.config(bg="#0772D6")
        deleteLb.config(bg="#0772D6")
        searchLb.config(bg="#0772D6")
        infoLb.config(bg = "#0772D6")
        closeLb.config(bg="#0772D6")

    def indicate(self, lb, frame):
        self.hideIndicate()
        lb.config(bg = "#DEE9F3")
        frame.tkraise()


    def searchFrame(self):
        pass


    def startFrame(self):
        pass

    def showFrame(self):
        pass

    def insertFrame(self):
        pass

    def deleteFrame(self):
        pass

    def infoFrame(self):
        pass



MainGUI()