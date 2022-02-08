import time
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *

from matplotlib.pyplot import text, title

from er1 import ER1

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
    _label2.config(text=f"{ER1.rackHS()}")
    _label2.after(1100,testme)

#def main():

main_win = Tk()
main_win.title("Interface Project Demo")
main_win.geometry("1000x700")
#################################
# TITLE BOX
#################################
_label = Label(main_win,text="HS Monitor Display")
_label.pack() # to make it above main canvas
#################################
#MAIN CANVAS
#################################
# main canvas area for the background
inner_win1 = Canvas(main_win,height=650,width=950,bg="#000")
inner_win1.pack()
#################################
#HS Side area
#################################
#function for a rectangle
#draw the main label
testrec(inner_win1,0,0,160,40,"blue","white")
testtxt(inner_win1,75,20,11,"black","EXPRESS RACK H&S")
#draw ER1 HS text
testtxt(inner_win1,75,60,10,"white","ER1 H&S : ")
testcir(inner_win1,130,70,150,50,"#FFF")
#draw ER2 HS text
testtxt(inner_win1,75,90,10,"white","ER2 H&S : ")
testcir(inner_win1,130,100,150,80,"#FFF")


#################################
#Main ER Boxes 
#################################

#ER1 Detail display
testrec(inner_win1,200,10,300,210,"blue","white")

#ER2 Detail display
testrec(inner_win1,310,10,410,210,"blue","white")

inner_win1.create_text(
        300,300,
        fill="white",
        font=f"Times 12 italic bold",
        text="THIS!!!!")
#################################
#BOTTOM TEXT AREA
#################################
_label2 = Label(main_win,text="Bottom Title Area")
_label2.pack() # to make it above main canvas


# text i need 


while True:
    _label2.after(1100,testme)
    main_win.mainloop()

