import data as dt
import numpy as np
import matplotlib.pyplot as plt
from math import sqrt


def arquivo():
    arquivo = dt.pega_arquivo()
    return arquivo

arquivo = arquivo()

t = 1
Xbola = (-0.007 * (t**3)) - (0.17 * (t**2) + (2.5 * t) + 1)  #posição x da bola no instante t
Ybola = ((0.2 * (t**2) + (1.8 * t) + 0.7)) #posição y da bola no instante t
Ri = 0.11


def interceptacao():
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

lista = interceptacao()

xroboideal = lista[1] + (lista[2] * lista[0])
yroboideal = lista[3] + (lista[4] * lista[0])

# a trajetoria do robo ate a bola em x e y em funcao do tempo
posix = [(lista[1] + lista[2] * t) for t in np.arange(0, lista[0], 0.02)]
posiy = [(lista[3] + lista[4] * t) for t in np.arange(0, lista[0], 0.02)]
tfinal = [arquivo[0][0][x] for x in range(0,len(posix))]

def grafico_1():
    # Trajetoria do robo,bola no mapa XY
    plt.clf()
    plt.title("Trajetoria da bola")
    plt.scatter([arquivo[1][0][x] for x in range(0,len(posix)+1)],
                [arquivo[2][0][x] for x in range(0,len(posix)+1)], s=10, label="Bola")
    plt.scatter(posix,posiy, s=10, label="Robo")

    plt.xlabel(" posicao X(m)")
    plt.ylabel(" posicao Y(m)")

    plt.grid()
    plt.legend()
    plt.show()

def grafico_2():
    # posicoes do robo e da bola em funcao do tempo
    plt.clf()
    plt.title("Posições da bola e do robo")
    plt.scatter(tfinal, [arquivo[1][0][x] for x in range(0,len(tfinal))], s=10, label="Bola em X")
    plt.scatter(tfinal, [arquivo[2][0][x] for x in range(0,len(tfinal))], s=10, label="Bola em Y")

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

    #velocidades do robo

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
    Ay = [(-0.4) for x in range(1,len(Ax)+1)]

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

    dist =[]
    for Xrobo, Yrobo, Posix, Posiy in zip(Xbola,Ybola,robox,roboy):
        dist.append((sqrt(((Xrobo - Posix) ** 2) + ((Yrobo - Posiy) ** 2)) + Ri))


    plt.scatter(tfinal, dist, s=10, label="Aceleracao da bola em x")
    plt.grid()
    plt.legend()
    plt.show()

