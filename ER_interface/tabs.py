import time
from tkinter import *
from tkinter.ttk import *

root = Tk()
root.geometry("500x500")
tabs = Notebook(root)

tab1 = Frame(tabs)
tab2 = Frame(tabs)

tabs.add(tab1,text="tab1")
tabs.add(tab2,text="tab2")
tabs.pack(expand=1,fill="both")

Label(tab1,text="Welcome to Tab-1")
Label(tab2,text="Welcome to Tab-2")

tab1can =  Canvas(tab1,height=650,width=950,bg="#000")
tab2can = Canvas(tab2,height=100,width=100,bg="blue")
tab1can.pack()
tab2can.pack()

#################################
# TITLE BOX
#################################
_label = Label(root,text="Main Label")
_label.pack() # to make it above main canvas
#################################
#MAIN CANVAS
#################################
# main canvas area for the background

root.mainloop()