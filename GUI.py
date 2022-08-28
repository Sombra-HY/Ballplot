from tkinter import *

class Application:
    def __init__(self, master=None):


        self.widget = Frame()
        self.widget.pack()
        self.widget["bg"] = "red"
        self.widget["width"] = "300"
        self.widget["height"] = "300"

        self.widget1 = Frame()
        self.widget1.pack()
        self.widget["bg"] = "blue"

        self.contanier1 = Label(self.widget1, text= "ola", width=20,height=20, bg="blue")
        self.contanier1.pack()

root = Tk()
Application(root)
root.geometry("1920x1080")
root.mainloop()