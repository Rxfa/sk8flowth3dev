import time,requests
from matplotlib.cbook import index_of
from tqdm import tqdm
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
words = ['login','admin','www','services']
def test():
    #y = requests.get("http:/localhost:8000/")
    for w in tqdm(words):
        root.update_idletasks
        pb1['value'] += 10
        l1.config(text=f"current : {w}")
        l1.after(10)
        time.sleep(.2)
        newL(w)
        
    l1.config(text="check tab 2 for results")
def newL(w_):
    nl = Label(c2,text=f"{w_}",width=10)
    nl.pack()
    time.sleep(.2)
    
def test2():
    root.update_idletasks()
    pb1['value'] += 25
    #time.sleep(.1)
        #if pb1['value'] == 30:

root = Tk()
root.title("Fuzzing Gui")
root.geometry("500x700")

tabs = Notebook(root)
tab1 = Frame(tabs)
tab2 = Frame(tabs)

tabs.add(tab1,text="tab1")
tabs.add(tab2,text="tab2")
tabs.pack(expand=1,fill="both")

Label(tab1,text="Welcome to Tab-1")
Label(tab2,text="Welcome to Tab-2")

#tab1can =  Canvas(tab1,height=650,width=950,bg="#000")
#tab2can = Canvas(tab2,height=100,width=100,bg="blue")
#tab1can.pack()
#tab2can.pack()


cmd_ = Button(tab1, text="CMD" ,command=test)
cmd_.pack()
e1 = Entry(tab1,width=20)
e1.pack()
c1 = Canvas(tab1,height=150,width=110,bg="#000")
c1.pack()

l1 = Label(tab1,text="N")
l1.pack()

pb1 = Progressbar(root,orient=HORIZONTAL,length=(len(words)*10),mode='determinate')
pb1.pack(expand=True)#################################

c2 = Canvas(tab2,height=150,width=310,bg="red")
c2.pack()


c1.mainloop()
c2.mainloop()
root.mainloop()