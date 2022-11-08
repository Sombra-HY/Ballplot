import data as dt
import numpy as np
import matplotlib.pyplot as plt
from math import sqrt


# #Outras fitas
# Ri = 0.11 #raio de interceptação
# #d = ((Xbola - Xr)**2)) + ((Ybola - Yr)**2)  #fórmula da distância entre dois pontos

# t = dt.pega_arquivo() #T =[[tempo],[],[]]


# #Grandezas
# aR = 4.0 #m/s  #aceleração do robô
# VfR = 2.3 #m/s  #velocidade final do robô

# #Posição
# Xbola = (-0.007 * (t**3)) - (0.17 * (t**2) + (2.5 * t) + 1)  #posição x da bola no instante t
# Ybola = ((0.2 * (t**2) + (1.8 * t) + 0.7)  #posição y da bola no instante t

# #Velocidade
# Vbx = ((0.021 * (t**2)) - (0.34 * t) + 2.5)  #velocidade da bola no eixo x no intante t
# Vby = ((-0.4 * t) + 1.8)  #velocidade da bola no eixo y no intante t
# Mvb = (Vbx + Vby)  #módulo da velocidade da bola no intante t

# #Aceleração
# Abx = ((-0.042 * t) - 0.34)  #aceleração da bola no eixo x no intante t
# Aby = -0.4  #aceleração da bola no eixo y no intante t
# Módulo da Aceleração da Bola Mab = (Abx + Aby)

#----------------------------------------------------------------------------------------------------------------------

#Dados dos graficos
#titulos =["Trajetoria da bola(x,y)","Coordenadas(x,y) da posição da bola e do robô em função do ",
#"tempo t","Velocidade(Vx,Vy) da bola e do robô em fução de t",
#"Aceleração(Ax,Ay) da bola e do robô em fução de t",
#"Distância relativa(d) entre o robô e a bola como função do tempo t"]

#labX = [" posicao X(m)", "Coordenadas(m)", "Velocidade (Metro/S)", "Aceleração (Metro/S²)", "Distância(m)"]
#labY = [" posicao Y(m)", " Tempo (Segundos)", "Tempo (Segundos)", "Tempo (Segundos)", "Tempo (Segundos)"]

# test
x = dt.pega_arquivo()
print("rodando...")


def grafico_1():
    # Trajetoria do robo,bola no mapa XY

    plt.title("Trajetoria da bola")
    plt.scatter(x[1], x[2], s=1.5, label="bola")
    plt.xlabel(" posicao X(m)")
    plt.ylabel(" posicao Y(m)")

    plt.grid()
    plt.legend()
    plt.show()

def grafico_2():
    # posicoes do robo e da bola em funcao do tempo

    plt.title("posicoes da bola e do robo")
    plt.scatter(x[0], x[1], s=1.5, label="bola em X")
    plt.scatter(x[0], x[2], s=1.5, label="bola em Y")
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
    T = x[0]
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
    plt.ylabel("Velocidade (M/S²)")

    # esta e a aceleracao AX e AY
    T = x[0]
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


grafico_1()
grafico_2()
grafico_3()
grafico_4()

# 1 2 3 4 OK/falata o robo

# def intercept():
#
#
#     Ri = 0.11
#     d = ((Xbola - Xr)**2)) + ((Ybola - Yr)**2)
#     if d >= Ri:
#         print("O robô interceptou a bola")
#
#
#     pass
