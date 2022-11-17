import tkinter as tk
import data as dt
from plot import grafico_1, grafico_2, grafico_3, grafico_4,grafico_5
from math import sqrt

global x
x = 0
global y
y = 0

def arquivo():
    arquivo = dt.pega_arquivo()
    return arquivo

arquivo = arquivo()

def interceptacao():
    Ri = 0.11
    posix = x
    posiy = y

    distancia = [(sqrt(((Xbola - posix) ** 2) + ((Ybola - posiy) ** 2)) + Ri) for Xbola, Ybola in
                 zip(arquivo[1][0], arquivo[2][0])]

    tempoRoboPonto = [((-23 + sqrt(529 + 800 * d)) / 40) for d in distancia]
    difTempo = [(arquivo[0][0][i] - tempoRoboPonto[i]) for i in range((len(arquivo[0][0])))]
    lista = []

    for i in range(len(difTempo)):

        if (difTempo[i]) > 0:
            lista.append([arquivo[0][0][i], arquivo[1][0][i],
                          arquivo[2][0][i], distancia[i], tempoRoboPonto[i], difTempo[i]])
            break


    velocidadex = (lista[0][1] - posix) / lista[0][0]
    velocidadey = (lista[0][2] - posiy) / lista[0][0]
    h = lista[0][0]
    xroboideal = posix + (velocidadex * h)
    yroboideal = posiy + (velocidadey * h)

    return h, posix, velocidadex, posiy, velocidadey

def querypg(x, y):
    print("...")
    if (x.isnumeric()==True) and (y.isnumeric()==True) and (0<=float(x)<=9 )  and (0<=float(y)<=6 ) :
        x = float(x)
        y = float(y)
    else:
        x = 0
        y = 0
        print("Valores Inválidos!")


window = tk.Tk()
window.geometry("1280x720")


c = tk.Canvas(window, bg="#545454", height="720", width="300")
c.place(x=0, y=0)

def chamador(indice):
    valor = [grafico_1,grafico_2,grafico_3,grafico_4,grafico_5]
    valor[indice]


grafico1 = tk.Button(
    window,
    text="Gráfico 1",
    fg="black",
    bg="white",
    command=chamador(0)
)

grafico2 = tk.Button(
    window,
    text="Gráfico 2",
    fg="black",
    bg="white",
    command=chamador(1)
)

grafico3 = tk.Button(
    window,
    text="Gráfico 3",
    fg="black",
    bg="white",
    command=chamador(2)
)

grafico4 = tk.Button(
    window,
    text="Gráfico 4",
    fg="black",
    bg="white",
    command=chamador(3)
)

grafico5 = tk.Button(
    window,
    text="Gráfico 5",
    fg="black",
    bg="white",
    command=chamador(4)
)

inputix = tk.Entry(window)

inputiy = tk.Entry(window)

enviar = tk.Button(window, text="Enviar valores", command=lambda: querypg(inputix.get(), inputiy.get()))

grafico1.place(x=20, y=140, height=40, width=260)
grafico2.place(x=20, y=200, height=40, width=260)
grafico3.place(x=20, y=260, height=40, width=260)
grafico4.place(x=20, y=320, height=40, width=260)
grafico5.place(x=20, y=380, height=40, width=260)
inputix.place(x=20,y=480,height=40, width=260)
inputiy.place(x=20,y=540,height=40, width=260)
enviar.place(x=20, y=560,height=40, width=260)


window.mainloop()