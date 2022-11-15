import data as dt
import numpy as np
import matplotlib.pyplot as plt
from math import sqrt
arquivo = dt.pega_arquivo()
t = 1

Xbola = (-0.007 * (t**3)) - (0.17 * (t**2) + (2.5 * t) + 1)  #posição x da bola no instante t
Ybola = ((0.2 * (t**2) + (1.8 * t) + 0.7)) #posição y da bola no instante t




def interceptacao():
    Ri = 0.11

    while True:
        posix = float(input("Digite a posicao X do robo: "))
        if ((posix >= 0) and (posix <= 9)):
            break
        print("Digite valores entre [0 <= x <= 9]")
    while True:
        posiy = float(input("Digite a posicao Y do robo: "))
        if ((posiy >= 0) and (posiy <= 6)):
            break
        print("Digite valores entre [0 <= x <= 6]")

    distancia = [(sqrt(((Xbola - posix) ** 2) + ((Ybola - posiy) ** 2)) + Ri) for Xbola, Ybola in
                 zip(arquivo[1][0], arquivo[2][0])]
    tempoRoboPonto = [((-23 + sqrt(529 + 800 * d)) / 40) for d in distancia]
    difTempo = [(arquivo[0][0][i] - tempoRoboPonto[i]) for i in range((len(arquivo[0][0])))]
    lista = []
    for i in range(len(difTempo)):

        if (difTempo[i]) > 0:
            print("dif ==", arquivo[0][0][i] - difTempo[i])
            lista.append([arquivo[0][0][i], arquivo[1][0][i],
                          arquivo[2][0][i], distancia[i], tempoRoboPonto[i], difTempo[i]])
            break

    print(lista)

    velocidadex = (lista[0][1] - posix) / lista[0][0]
    velocidadey = (lista[0][2] - posiy) / lista[0][0]
    h = lista[0][0]
    xroboideal = posix + (velocidadex * h)
    yroboideal = posiy + (velocidadey * h)

    return h, posix, velocidadex, posiy, velocidadey

# t_intercept =[]
# inter = interceptacao()
# for i in range(len(arquivo[0][0])):
#     if arquivo[0][0][i] <= inter[0]:
#         t_intercept.append(arquivo[0][0][i])
#
# print(t_intercept)

lista= interceptacao()

xroboideal = lista[1] + (lista[2] * lista[0])
yroboideal = lista[3] + (lista[4] * lista[0])


def grafico_1():
    # Trajetoria do robo,bola no mapa XY

    plt.title("Trajetoria da bola")
    plt.scatter(arquivo[1], arquivo[2], s=10, label="Bola")
    plt.scatter(
        [(lista[1]+lista[2] * t) for t in np.arange(0, lista[0], 0.02)],
        [(lista[3]+lista[4] * t) for t in np.arange(0, lista[0], 0.02)], s=10, label="Robo")
    plt.xlabel(" posicao X(m)")
    plt.ylabel(" posicao Y(m)")

    plt.grid()
    plt.legend()
    plt.show()

def grafico_2():
    # posicoes do robo e da bola em funcao do tempo

    plt.title("posicoes da bola e do robo")
    plt.scatter(arquivo[0], arquivo[1], s=1.5, label="bola em X")
    plt.scatter(arquivo[0], arquivo[2], s=1.5, label="bola em Y")

    plt.scatter([(lista[1]+lista[2] * t) for t in np.arange(0, lista[0], 0.02)], arquivo[1], s=1.5, label="Robo em X")
    plt.scatter(arquivo[0], arquivo[2], s=1.5, label="Robo em Y")


    plt.xlabel(" cordenadas (metro)")
    plt.ylabel(" Tempo (segundos)")

    plt.grid()
    plt.legend()
    plt.show()

def grafico_3():
    # Velocidade em funcao do Tempo

    plt.title("Velocidade da bola e do robo em funcao do Tempo")
    plt.xlabel("Tempo (segundos)")
    plt.ylabel("Velocidade (M/S)")

    # esta e a velocidade VX e VY
    T = arquivo[0]

    Vx = [((0.021 * (t * t)) - (0.34 * t) + 2.5) for t in T[0]]
    Vy = [(((-0.4 * t) + 1.8)) for t in T[0]]

    # Velocidadedes da bola
    plt.scatter(T, Vx, s=1.5, label="Velocidade da bola em x")
    plt.scatter(T, Vy, s=1.5, label="Velocidade da bola em y")

    #velocidades do robo
    plt.grid()
    plt.legend()
    plt.show()

def grafico_4():
    plt.title("Aceleracao da bola e do robo em funcao do Tempo")
    plt.xlabel("Tempo (segundos)")
    plt.ylabel("Aceleracao (M/S²)")

    # esta e a aceleracao AX e AY
    T = arquivo[0]
    Ax = [(((-0.042 * t) - 0.34)) for t in T[0]]
    Ay = [(-0.4 + 1.8)*(x/x) for x in range(1,len(Ax)+1)]

    # aceleracao da bola
    plt.scatter(T, Ax, s=1.5, label="Aceleracao da bola em x")
    plt.scatter(T, Ay, s=1.5, label="Aceleracao da bola em y")

    # aceleracao do robo

    plt.grid()
    plt.legend()
    plt.show()

def grafico_5():
    pass




grafico_2()