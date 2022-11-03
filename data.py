from tkinter import Tk as tk
from tkinter.filedialog import askopenfilename
import re as Re

# O arquivo data faz apenas o tratamento dos dados


def pega_arquivo():

    # VISAO GERAL
    # esta funcao lera um arquivo de escolha do usuario, apartir da segunda linha
    # rertonara uma lista composta [[x],[z],[z]]
    # podendo ter mais de um elemento no x, y e z
    #
    # LEITURA ACEITA
    # "Tempo" \t "posiX" \t "posiY" \n
    #


    # pede ao usuario o arquivo para o tratamento de dados, guardando o diretorio.

    janela = tk().withdraw()
    diretorio = askopenfilename(filetypes=(("Arquivos de texto", "*.txt"), ("Arquivos csv", "*.csv")))

    # Trataremos os dados do arquivo lendo os e os adicionando em uma "string"

    arquivo = open(diretorio, "r")

    Posix= []; Posiy =[]; Tempo = []; cont = 0; soma = ""

    if arquivo:

        # comecar a ler a linha apartir da segunda

        for linha in arquivo.readlines():

            cont += 1

            if cont >=2:
                soma += linha
        soma = Re.split("[\t\n]", soma)

        # Aqui distribuiremos cada coluna oara uma lista, tempo, posiX e posiY

        for x, y, z in zip(range(0, len(soma), 3), range(1, len(soma), 3), range(2, len(soma), 3)):

             # se a direcao da bola for negativa, nao sera demonstrado nos graficos, porta

            if (float(soma[y].replace(",", "."))<0 or float(soma[z].replace(",", "."))<0):
                break

            Tempo.append(float(soma[x].replace(",", ".")))
            Posix.append(float(soma[y].replace(",", ".")))
            Posiy.append(float(soma[z].replace(",", ".")))

            # retorno da lista em matriz

            # [[tempo],[posicao x],[posicao y]]

        return([[Tempo],[Posix],[Posiy]])
    else:
        print("arquivo nao selecionado")


