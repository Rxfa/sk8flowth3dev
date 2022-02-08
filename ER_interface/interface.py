import time
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *

#from matplotlib.pyplot import text, title


from racks import *

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
    _label2.after(1000,testme)

def er1display(): 
    inner_win1.itemconfig(e1ric,text=f"{ER1.rackHS()[1]}")
    inner_win1.itemconfig(e1rfca,text=f"{ER1.rackHS()[3]}")
    inner_win1.itemconfig(er1aaaspeed_,text=f"{ER1.rackHS()[2]}")
    
    inner_win1.itemconfig(tt,text=f"{ER1.rackHS()}")
    inner_win1.itemconfig(er1ric_cir,fill=f"{ER1.RIC['poweredric']}")
    inner_win1.itemconfig(er1aaa_cir,fill=f"{ER1.RIC['poweredaaa']}")
    inner_win1.itemconfig(er1rfca_cir,fill=f"{ER1.RIC['poweredrfca']}")
    inner_win1.itemconfig(mainlight,fill=f"{ER1.MAIN['poweredc']}")
    inner_win1.itemconfig(auxlight,fill=f"{ER1.AUX['poweredc']}")
                   
    inner_win1.after(1000,er1display)
def eract():
    er1_.start()
    er1speed1.start()
    er1HS.start()
    er1afc1_.start()
    er1afc2_.start()
    ER1.SSPCM_Init()
 


# function for progress bar
def progress():
    for prog in range(20):
        inner_win1.update_idletasks()
        pb1['value'] += 5
        time.sleep(.1)
        if pb1['value'] == 30:
            er1_.start()
            er1speed1.start()
            er1HS.start()
            er1afc1_.start()
            er1afc2_.start()
            er2_.start()
            er2speed2.start()
            er2HS.start()
            er2afc1_.start()
            er2afc2_.start()
            
            #time.sleep(1)
            
        if pb1['value'] == 60 : 
            er1display()
            time.sleep(1)
        if pb1['value'] > 95 : 
            pb1['value'] = 5
            ER1.SSPCM_Init()

def openNewWindow():
     
    # Toplevel object which will
    # be treated as a new window
    newWindow = Toplevel(inner_win1)
 
    # sets the title of the
    # Toplevel widget
    newWindow.title("New Window")
 
    # sets the geometry of toplevel
    newWindow.geometry("200x200")
 
    # A Label widget to show in toplevel
    Label(newWindow,
          text ="This is a new window").pack()
    inner_win2 = Canvas(newWindow,height=100,width=100,bg="red")
    inner_win2.pack()
    testtxt(inner_win2,50,60,10,"white","ER1 H&S : ")
    testcir(inner_win2,130,70,150,50,"#FFF")

    

#def main():

main_win = Tk()
main_win.title("Interface Project Demo")
main_win.geometry("1000x700")

pb1 = Progressbar(main_win,orient=HORIZONTAL,length=100,mode='determinate')
pb1.pack(expand=True)#################################
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
# RPC boxes
#main
mainlight = inner_win1.create_rectangle(201, 10, 249, 20,outline="red",fill="white")
testtxt(inner_win1,220,15,7,"black","MAIN")
#safing
auxlight = inner_win1.create_rectangle(251, 10, 299, 20,outline="red",fill="white")
testtxt(inner_win1,270,15,7,"black","AUX")

# RIC 
er1ric_cir = inner_win1.create_oval(
    210, 35, 220,45,
    fill="white",
    tags="er1"
    )
testtxt(inner_win1,240,40,8,"black","RIC")

e1ric = inner_win1.create_text(
        260,40,
        fill="black",
        font=f"Times 8 italic bold",
        text="0 N",tags="e1")
# RFCA
er1rfca_cir = inner_win1.create_oval(
    210, 55, 220,65,
    fill="white",
    tags="er1"
    )
testtxt(inner_win1,240,60,8,"black","RFCA")

e1rfca = inner_win1.create_text(
        280,60,
        fill="black",
        font=f"Times 8 italic bold",
        text="0 N",tags="e1")

# AAA
er1aaa_cir = inner_win1.create_oval(
    210, 75, 220,85,
    fill="white",
    tags="er1"
    )

testtxt(inner_win1,240,80,8,"black","AAA")
er1aaaspeed_ = inner_win1.create_text(
        280,80,
        fill="black",
        font=f"Times 8 italic bold",
        text="0 N",tags="e1")
#ER2 Detail display
testrec(inner_win1,310,10,410,210,"blue","white")


#################################
# NOT RACK STUFF and TESTING
#################################

e = Entry(main_win,width=50)
e.pack()
tt = inner_win1.create_text(
        300,300,
        fill="white",
        font=f"Times 12 italic bold",
        text="0 N",tags="tryme")

cmd_ = Button(inner_win1, text="CMD",command=eract)
cmd_.place(x=25, y=100)
cmd_2 = Button(inner_win1, text="CMD w/ Status",command=progress)
cmd_2.place(x=25, y=150)
cmd_3 = Button(inner_win1, text="Test Window",command=openNewWindow)
cmd_3.place(x=25, y=175)
#################################
#BOTTOM TEXT AREA
#################################
_label2 = Label(main_win,text="Bottom Title Area")
#inner_win1.after(1000,er1display)
_label2.pack() # to make it above main canvas


# text i need 

# updating telemtry values

inner_win1.mainloop()
main_win.mainloop()

