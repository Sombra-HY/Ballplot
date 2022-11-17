import tkinter as tk


class janela():

    # Parametros padroes


    def __init__(self, resolucaox="300", resolucaoy="300", cor1 = "black", cor2 ="white"):
        self.f = cor1
        self.l = cor2

        self.valorx = resolucaox
        self.valory = resolucaoy

        self.window = tk.Tk()
        self.window.geometry("%sx%s" % (self.valorx, self.valory))

        self.grafico5 = tk.Button(self.window, text="Gráfico 5", fg = self.f, bg = self.l, command= chama())
        self.grafico5.place(x=20, y=10, height=10, width=260)

        self.window.mainloop()

    def reso(self):
        print(self.valorx, self.valory)
        self.valory = "900"
        self.valorx = "900"
        return self


def chama():
    pass




widget = janela()
widget.reso()

