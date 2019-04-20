
import tkinter as tk

class MainWindow():
    def __init__(self, parent):
        top = self.top = tk.Toplevel(parent)
        self.myLabel = tk.Label(top, text='Request')
        self.myLabel.pack()
        self.myEntryBox = tk.Entry(top)
        self.myEntryBox.focus_set()
        self.myEntryBox.pack()
        self.mySubmitButton = tk.Button(top, text='OK', command=self.DestWin)
        self.mySubmitButton.pack()
    def DestWin(self):
        # call callback function setting value in MyFrame
        self.callback(self.myEntryBox.get())
        self.top.destroy()



    def set_callback(self, a_func):
        self.callback = a_func



class MyFrame(tk.Frame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        self.pack()

        self.myLabel1 = tk.Label(parent, text='Special Request')
        self.myLabel1.pack()
        self.mySubmitButton1 = tk.Button(parent, text='OK', command=self.get_group_name)
        self.mySubmitButton1.pack()


    def get_group_name(self):
        mw = MainWindow(None)

        # provide callback to MainWindow so that it can return results to MyFrame
        mw.set_callback(self.set_label)



    def set_label(self, astr = ''):
        self.myLabel1['text'] = astr
        print("###-----____________________*IMPORTANT!!!*____________________-----###")
        print(astr)
        print("-------------------Coustomer is always right!!!-----------------------")





root = tk.Tk()

mf = MyFrame(root)

root.mainloop()
