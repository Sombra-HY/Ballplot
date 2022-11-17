from tkinter import *
import data as dt
from math import sqrt
from INTERFACE import *

def bot():
    x=y=0

    def querypg(x, y):
        print("...")
        if (x.isnumeric()==True) and (y.isnumeric()==True) and (0<=float(x)<=9 )  and (0<=float(y)<=6 ) :
            x = float(x)
            y = float(y)
            print(x, y)
        else:
            x = 0
            y = 0

    janela = Tk()
    janela.title("query tools")
    texto = Label(janela, text="insira seu código aqui")
    texto.grid(column=0, row=0)

    codigo = Entry(janela, width=100)
    codigo.grid(column=1, row=1)

    codigo2 = Entry(janela, width=100)
    codigo2.grid(column=2, row=1)

    botao = Button(janela, text="Rodar código", command=lambda: querypg(codigo.get(), codigo2.get()))

    botao.grid(column=0, row=2)
    janela.mainloop()

x=y=0

def querypg(x, y):
    print("...")
    if (x.isnumeric()==True) and (y.isnumeric()==True) and (0<=float(x)<=9 )  and (0<=float(y)<=6 ) :
        x = float(x)
        y = float(y)
        print(x, y)
    else:
        x = 0
        y = 0

janela = Tk()
janela.title("query tools")
texto = Label(janela, text="insira seu código aqui")
texto.grid(column=0, row=0)

codigo = Entry(janela, width=100)
codigo.grid(column=1, row=1)

codigo2 = Entry(janela, width=100)
codigo2.grid(column=2, row=1)

botao = Button(janela, text="Rodar código", command=lambda: querypg(codigo.get(), codigo2.get()))

botao.grid(column=0, row=2)
janela.mainloop()