import tkinter
from tkinter import *

class Busca:
    def __init__(self, master = None):
        self.fontep = ("arial", "10", "bold")
        self.titulo1 = Label()
        self.titulo1["text"] = "Iforme os dados:"
        self.titulo1["font"] = ("times new roman", "13", "bold")
        self.titulo1.pack()

        self.cont2 = Frame(master)
        self.cont2["padx"] = 30
        self.cont2.pack()
        self.idusu = Label(self.cont2, text="IDusuario:", font=self.fontep)
        self.idinfo = Entry(self.cont2)
        self.idinfo["width"] = 10
        self.b1 = Button(self.cont2, text="Buscar", font=self.fontep)
        self.b1["width"] = 6
        self.idusu.pack(side=LEFT)
        self.idinfo.pack(side=LEFT)
        self.b1.pack(side=RIGHT)

        self.cont3 = Frame(master)
        self.cont3["padx"] = 30
        self.cont3.pack()
        self.Nome = Label(self.cont3, text="Nome:", font=self.fontep, padx= -20)
        self.idnome = Entry(self.cont3)
        self.idnome["width"] = 27
        self.Nome.pack(side=LEFT)
        self.idnome.pack(side=LEFT)

        self.cont4 = Frame(master)
        self.cont4["padx"] = 30
        self.cont4.pack()
        self.tel = Label(self.cont4, text="telefone:", font=self.fontep, padx=-20)
        self.idtel = Entry(self.cont4)
        self.idtel["width"] = 24
        self.tel.pack(side=LEFT)
        self.idtel.pack(side=LEFT)

        self.cont5 = Frame(master)
        self.cont5["padx"] = 30
        self.cont5.pack()
        self.email = Label(self.cont5, text="E-mail:", font=self.fontep, padx= -20)
        self.idema = Entry(self.cont5)
        self.idema["width"] = 26
        self.email.pack(side=LEFT)
        self.idema.pack(side=LEFT)

        self.cont6 = Frame(master)
        self.cont6["padx"] = 30
        self.cont6.pack()
        self.usuario = Label(self.cont6, text="usuario:", font=self.fontep, padx= -20)
        self.idusa = Entry(self.cont6)
        self.idusa["width"] = 25
        self.usuario.pack(side=LEFT)
        self.idusa.pack(side=LEFT)

        self.cont7 = Frame(master)
        self.cont7["padx"] = 30
        self.cont7.pack()
        self.senha = Label(self.cont7, text="Senha:", font=self.fontep, padx=-20)
        self.idsen = Entry(self.cont7)
        self.idsen["show"] = "*"
        self.idsen["width"] = 26
        self.senha.pack(side=LEFT)
        self.idsen.pack(side=LEFT)

        self.cont8 = Frame(master)
        self.cont8["padx"] = 30
        self.cont8.pack()
        self.bot2 = Button(self.cont8, text="Inserir", font=self.fontep)
        self.bot3 = Button(self.cont8, text="Alterar", font=self.fontep)
        self.bot4 = Button(self.cont8, text="Excluir", font=self.fontep)
        self.bot2["width"] = 7
        self.bot3["width"] = 7
        self.bot4["width"] = 7
        self.bot2.pack(side=LEFT)
        self.bot3.pack(side=LEFT)
        self.bot4.pack(side=LEFT)

root = Tk()
Busca(root)
root.mainloop()