import tkinter as tk
from model import Model
from view import View



class Controller:
    def __init__(self):
        #make GUI root
        self.root = tk.Tk()
        # init Model and View
        self.model = Model()
        self.view = View(self.root,self.model)
        self.root.title("Gyoza Bar Ann: Checkout & Order System")

        

        

        # construct GUI
        self.view.make_gui()
        

    def run(self):
        #starts GUI program
        self.root.mainloop()

if __name__== '__main__':
    # main program
    c = Controller()
    c.run()

