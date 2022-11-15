from data import pega_arquivo
from math import sqrt

t = 1
Xbola = (-0.007 * (t**3)) - (0.17 * (t**2) + (2.5 * t) + 1)  #posição x da bola no instante t
Ybola = ((0.2 * (t**2) + (1.8 * t) + 0.7)) #posição y da bola no instante t
posicoesBOLA =pega_arquivo()
def interceptacao():
    Ri = 0.11


    while True:
        posix = float(input("Digite a posicao X do robo: "))
        if ((posix>=0) and (posix<=9)):
            break
        print("Digite valores entre [0 <= x <= 9]")
    while True:
        posiy = float(input("Digite a posicao Y do robo: "))
        if ((posiy>=0) and (posiy<=6)):
            break
        print("Digite valores entre [0 <= x <= 6]")


    distancia = [(sqrt(((Xbola - posix)**2) + ((Ybola - posiy)**2)) + Ri)for Xbola, Ybola in zip(posicoesBOLA[1][0], posicoesBOLA[2][0])]
    tempoRoboPonto = [((-23 + sqrt(529+800*d))/40) for d in distancia]
    difTempo =[(posicoesBOLA[0][0][i]-tempoRoboPonto[i]) for i in range((len(posicoesBOLA[0][0])))]
    lista=[]
    for i in range(len(difTempo)):

        if (difTempo[i]) > 0:
            print("dif ==",posicoesBOLA[0][0][i]-difTempo[i])
            lista.append([posicoesBOLA[0][0][i],posicoesBOLA[1][0][i],
                         posicoesBOLA[2][0][i],distancia[i],tempoRoboPonto[i],difTempo[i]])
            break

    print(lista)

    velocidadex = (lista[0][1]-posix)/lista[0][0]
    velocidadey = (lista[0][2]-posiy)/lista[0][0]

    xroboideal = posix + (velocidadex * lista[0][0])
    yroboideal = posiy + (velocidadey * lista[0][0])
    print(xroboideal)
    print(yroboideal)

    return lista
interceptacao()

