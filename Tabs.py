from tkinter import *                                    
from tkinter import ttk

root = Tk()
root.title("Tab Widget")
root.geometry("500x300")
tabControl = ttk.Notebook(root)

tab1 = Frame(tabControl)
tab2 = Frame(tabControl)

tabControl.add(tab1, text ='Tab 1')
tabControl.add(tab2, text ='Tab 2')
tabControl.pack(expand = 1, fill ="both")

ttk.Label(tab1,text ="Welcome to Tab 1").grid(padx = 30,pady = 30)
ttk.Label(tab2,text ="Let's learn together with coder.buzz!").grid(padx = 30,pady = 30)

root.mainloop()
