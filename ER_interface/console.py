import time,requests
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *

#from matplotlib.pyplot import text, title


#default size 12, Times,italic/bold
def testtxt(canvas,x,y,s,fill_,text_):
    canvas.create_text(
    x,y,
    fill=fill_,
    font=f"Times {s} italic bold",
    text=text_)
def testrec(canvas,x1,y1,x2,y2,outline_,fill_):
    canvas.create_rectangle(x1, y1, x2, y2,outline=outline_,fill=fill_)

def testcir(canvas,x,y,r1,r2,fill_): # x,y, r1,r2
    canvas.create_oval(
    x, y, r1,r2,
    fill=fill_
    #tag="circ"
    )
def testme():
    url = f"{e.get()}"
    t = requests.get(url)

    if t.status_code == 200: 
        la2.config(text=f"{t.headers}")
        la2.after(100,testme)
        myLabel = Label(inner_win2,text=f"CMD SENT: ACTIAVTE {e.get()}")
        myLabel2 = Label(tab1can,text=f"CMD SENT: ACTIAVTE {e.get()}")


main_win = Tk()
main_win.title("Interface Project Demo")
main_win.geometry("1000x700")

pb1 = Progressbar(main_win,orient=HORIZONTAL,length=100,mode='determinate')
pb1.pack(expand=True)#################################
#################################
# TITLE BOX
#################################

#################################
#MAIN CANVAS
#################################
# main canvas area for the background
inner_win1 = Canvas(main_win,height=750,width=1100,bg="#000")
inner_win1.pack()
##################
tabs = Notebook(inner_win1)

tab1 = Frame(tabs)
tab2 = Frame(tabs)
tab3 = Frame(tabs)

tabs.add(tab1,text="General HS")
tabs.add(tab2,text="Detailed (in work)")
tabs.add(tab3,text="Command History (in work)")
tabs.pack(expand=1,fill="both")


tab1can = Canvas(tab1,height=650,width=950,bg="#000")
tab2can = Canvas(tab2,height=650,width=950,bg="#000")
tab3can = Canvas(tab3,height=650,width=250,bg="#000")
tab1can.pack()
tab2can.pack()
tab3can.pack()

_label = Label(tab1can,text="send request")
_label.pack() # to make it above main canvas
la2 = Label(tab1can,text="")
la2.pack()

e = Entry(tab1can,width=40)
e.pack()
cmd_ = Button(tab1can, text="CMD" ,command=testme)
cmd_.pack()
main_win.mainloop()