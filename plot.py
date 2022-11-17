# importando arquivos e bibliotecas utilizadas no projeto
import data as dt
import numpy as np
import matplotlib.pyplot as plt
from math import sqrt
import tkinter as tk
from PIL import Image, ImageTk


# definindo arquivo que contém a trajetória da bola
def arquivo():
    arquivo = dt.pega_arquivo()
    return arquivo


arquivo = arquivo()

# coordenadas x e y em um vetor
coord = [0, 0]


# função que verifica se as variáveis são válidas
def querypg(x, y):
    if (x.isnumeric() == True) and (y.isnumeric() == True) and (0 <= float(x) <= 9) and (0 <= float(y) <= 6):
        global coord

        x = float(x)
        y = float(y)

        coord[0] = float(x)
        coord[1] = float(y)
        print("Novas coordenadas: ", coord)
    else:
        x = 0
        y = 0
        print("Valores Inválidos!")


# declarando a janela através do TkInter
window = tk.Tk()
window.geometry("300x720")
window.title("Gráficos")
window.configure(bg="#050a30")

# declarando campo de texto para envio das posições x e y iniciais do robô
inputix = tk.Entry(window)
inputiy = tk.Entry(window)

# declarando botão de envio chamando a função que altera os valores de x e y iniciais do robô
enviar = tk.Button(window,
                   text="Enviar!",
                   command=lambda: querypg(inputix.get(), inputiy.get()),
                   relief="raised",
                   bg="#A0DBFF",
                   font=('Arial', 12, "bold")
                   )

# declaração de outras variáveis
t = 1
Xbola = (-0.007 * (t ** 3)) - (0.17 * (t ** 2) + (2.5 * t) + 1)  # posição x da bola no instante t
Ybola = ((0.2 * (t ** 2) + (1.8 * t) + 0.7))  # posição y da bola no instante t
Ri = 0.11


# cálculo de variáveis baseadas nas posições iniciais do robô
def interceptacao(posix, posiy):
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


# cálculo da posição final do robõ baseadas nas variáveis obtidas em "interceptação()"
def contas(lista, u):
    # a trajetoria do robo ate a bola em x e y em funcao do tempo
    posix = [(lista[1] + lista[2] * t) for t in np.arange(0, lista[0], 0.02)]
    posiy = [(lista[3] + lista[4] * t) for t in np.arange(0, lista[0], 0.02)]
    tfinal = [arquivo[0][0][x] for x in range(0, len(posix))]

    def grafico_1():
        # Trajetoria do robo,bola no mapa XY
        plt.clf()
        plt.title("Trajetoria da bola")
        plt.scatter([arquivo[1][0][x] for x in range(0, len(posix) + 1)],
                    [arquivo[2][0][x] for x in range(0, len(posix) + 1)], s=10, label="Bola")
        plt.scatter(posix, posiy, s=10, label="Robo")

        plt.xlabel(" posicao X(m)")
        plt.ylabel(" posicao Y(m)")

        plt.grid()
        plt.legend()
        plt.show()

    def grafico_2():
        # posicoes do robo e da bola em funcao do tempo
        plt.clf()
        plt.title("Posições da bola e do robo")
        plt.scatter(tfinal, [arquivo[1][0][x] for x in range(0, len(tfinal))], s=10, label="Bola em X")
        plt.scatter(tfinal, [arquivo[2][0][x] for x in range(0, len(tfinal))], s=10, label="Bola em Y")

        plt.scatter(tfinal, posix, s=10, label="Robo em X")
        plt.scatter(tfinal, posiy, s=10, label="Robo em Y")

        plt.xlabel("Tempo (segundos)")
        plt.ylabel("Coordenadas (metros)")

        plt.grid()
        plt.legend()
        plt.show()

    def grafico_3():
        # Velocidade em funcao do Tempo
        plt.clf()
        plt.title("Velocidade da bola e do robo em funcao do Tempo")
        plt.xlabel("Tempo (segundos)")
        plt.ylabel("Velocidade (M/S)")

        # esta e a velocidade VX e VY

        Vx = [((0.021 * (t * t)) - (0.34 * t) + 2.5) for t in tfinal]
        Vy = [(((-0.4 * t) + 1.8)) for t in tfinal]

        # Velocidadedes da bola
        plt.scatter(tfinal, Vx, s=10, label="Velocidade da bola em x")
        plt.scatter(tfinal, Vy, s=10, label="Velocidade da bola em y")

        # velocidades do robo

        plt.scatter(tfinal, [lista[2] for x in range(len(tfinal))], s=10, label="Velocidade da Robo em x")
        plt.scatter(tfinal, [lista[4] for x in range(len(tfinal))], s=10, label="Velocidade da Robo em y")

        plt.grid()
        plt.legend()
        plt.show()

    def grafico_4():
        plt.clf()
        plt.title("Aceleracao da bola e do robo em funcao do Tempo")
        plt.xlabel("Tempo (segundos)")
        plt.ylabel("Aceleracao (M/S²)")

        # esta e a aceleracao AX e AY
        T = arquivo[0]
        Ax = [(((-0.042 * t) - 0.34)) for t in tfinal]
        Ay = [(-0.4) for x in range(1, len(Ax) + 1)]

        # aceleracao da bola
        plt.scatter(tfinal, Ax, s=10, label="Aceleracao da bola em x")
        plt.scatter(tfinal, Ay, s=10, label="Aceleracao da bola em y")

        # aceleracao do robo

        plt.scatter(tfinal, [0 for x in range(len(tfinal))], s=10, label="Aceleracao do Robo em x")
        plt.scatter(tfinal, [0 for x in range(len(tfinal))], s=10, label="Aceleracao do Robo em y")

        plt.grid()
        plt.legend()
        plt.show()

    def grafico_5():
        plt.clf()
        plt.title("Distancia relativa entre a bola e o robo em funcao do Tempo")
        plt.xlabel("Tempo (segundos)")
        plt.ylabel("Distancia (Metros)")

        Xbola = [arquivo[1][0][x] for x in range(len(tfinal))]
        Ybola = [arquivo[2][0][x] for x in range(len(tfinal))]

        robox = posix
        roboy = posiy

        dist = []
        for Xrobo, Yrobo, Posix, Posiy in zip(Xbola, Ybola, robox, roboy):
            dist.append((sqrt(((Xrobo - Posix) ** 2) + ((Yrobo - Posiy) ** 2)) + Ri))

        plt.scatter(tfinal, dist, s=10, label="Aceleracao da bola em x")
        plt.grid()
        plt.legend()
        plt.show()

    funcs = [grafico_1, grafico_2, grafico_3, grafico_4, grafico_5]
    funcs[u]()


# funções para chamar os gráficos sem executá-los ao iniciar o programa
def graph1():
    contas(interceptacao(coord[0], coord[1]), 0)


def graph2():
    contas(interceptacao(coord[0], coord[1]), 1)


def graph3():
    contas(interceptacao(coord[0], coord[1]), 2)


def graph4():
    contas(interceptacao(coord[0], coord[1]), 3)


def graph5():
    contas(interceptacao(coord[0], coord[1]), 4)


# declarando os botões dos gráficos
grafico1 = tk.Button(
    window,
    text="Gráfico 1",
    fg="black",
    bg="#38e6d6",
    command=graph1,
    font=('Arial', 14, "bold")
)

grafico2 = tk.Button(
    window,
    text="Gráfico 2",
    fg="black",
    bg="#A0DBFF",
    command=graph2,
    font=('Arial', 14, "bold")
)

grafico3 = tk.Button(
    window,
    text="Gráfico 3",
    fg="black",
    bg="#38e6d6",
    command=graph3,
    font=('Arial', 14, "bold")
)

grafico4 = tk.Button(
    window,
    text="Gráfico 4",
    fg="black",
    bg="#A0DBFF",
    command=graph4,
    font=('Arial', 14, "bold")
)

grafico5 = tk.Button(
    window,
    text="Gráfico 5",
    fg="black",
    bg="#38e6d6",
    command=graph5,
    font=('Arial', 14, "bold")
)

# imagem ora bolas
image1 = Image.open("imagens\image.png")
image2 = image1.resize((260, 180), Image.ANTIALIAS)
test = ImageTk.PhotoImage(image2)
label1 = tk.Label(image=test, bg="#050a30")
label1.image = test
label1.place(x=20, y=0)

# declarando TEXTO x e y do robô (apenas visual)
xlabel = tk.Label(text="X:", bg="#050a30", fg='white', font=("Arial", 13))
ylabel = tk.Label(text="Y:", bg="#050a30", fg='white', font=("Arial", 13))

# botões dos gráficos
grafico1.place(x=20, y=210, height=40, width=260)
grafico2.place(x=20, y=270, height=40, width=260)
grafico3.place(x=20, y=330, height=40, width=260)
grafico4.place(x=20, y=390, height=40, width=260)
grafico5.place(x=20, y=450, height=40, width=260)

# texto: Digite as posições iniciais do robõ:
tlabel = tk.Label(text="Digite as posições iniciais do robô:", bg="#050a30", fg='white', font=("Arial", 13))
tlabel.place(x=20, y=495, height=40, width=260)

# y inicial do robõ
xlabel.place(x=12, y=546)
inputix.place(x=40, y=540, height=40, width=100)

# x inicial do robô
ylabel.place(x=12, y=606)
inputiy.place(x=40, y=600, height=40, width=100)

# botão enviar
enviar.place(x=40, y=660, height=40, width=100)

# imagem robo
imager1 = Image.open("imagens\img.png")
imager2 = imager1.resize((110, 110), Image.ANTIALIAS)
test = ImageTk.PhotoImage(imager2)
labelr2 = tk.Label(image=test, bg="#050a30")
labelr2.image = test
labelr2.place(x=175, y=580)

window.mainloop()