import tkinter as tk
from view import View
from tkinter import tix

class whatever(tk.Frame):
  def __init__(self, parent):
    super(whatever, self).__init__(parent)
    self.parent = parent

    self.checklist = tix.CheckList(self.parent, browsecmd=self.selectItem,
                                   options='hlist.columns 1', highlightthickness=1,
                                   highlightcolor='#B7D9ED')
    self.checklist.grid(sticky='ew', padx=20)

    self.checklist.hlist.config(bg='white', bd=0, selectmode='none', selectbackground='white',
                                selectforeground='black', drawbranch=True, pady=5, header=True)

    self.checklist.hlist.header_create(0, itemtype=tix.TEXT, text='Orders',
                                       relief='flat')
    global test
    self.checklist.hlist.add("CL1", text=test)
    self.checklist.hlist.add("CL1.Item1", text="subitem1")
    self.checklist.setstatus("CL1", "on")
    self.checklist.setstatus("CL1.Item1", "off")

  def selectItem(self, item):
      print(item)


root = tix.Tk()
whatever(root)
root.mainloop()
