from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import os 

root=Tk()
root.geometry("300x300")

def shutdown():
	a=messagebox.askyesno(" ","Do you wish to shutdown your computer ?")
	if a==1:			#yes returns 1
		os.system("shutdown /s /t 1")
	else:				#no returns 0
		return
	
ttk.Button(root,text="Shut Down",cursor="hand2",command=shutdown).pack(pady=100)
root.mainloop()
