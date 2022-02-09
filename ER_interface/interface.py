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
    tab1can.itemconfig(e1ric,text=f"{ER1.rackHS()[1]}")
    tab1can.itemconfig(e1rfca,text=f"{ER1.rackHS()[3]}")
    tab1can.itemconfig(er1aaaspeed_,text=f"{ER1.rackHS()[2]}")
    
    tab1can.itemconfig(tt,text=f"{ER1.rackHS()}")
    tab1can.itemconfig(er1ric_cir,fill=f"{ER1.RIC['poweredric']}")
    tab1can.itemconfig(er1aaa_cir,fill=f"{ER1.RIC['poweredaaa']}")
    tab1can.itemconfig(er1rfca_cir,fill=f"{ER1.RIC['poweredrfca']}")
    tab1can.itemconfig(mainlight,fill=f"{ER1.MAIN['poweredc']}")
    tab1can.itemconfig(auxlight,fill=f"{ER1.AUX['poweredc']}")
                   
    tab1can.after(1000,er1display)
def eract():
    er1_.start()
    er1speed1.start()
    er1HS.start()
    er1afc1_.start()
    er1afc2_.start()
    ER1.SSPCM_Init()
 


# function for main prog bar
def start_data():
    for prog in range(20):
        tab1can.update_idletasks()
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

# function for progress bar
def cmd_issued():
    for prog in range(20):
        tab1can.update_idletasks()
        pb1['value'] += 5
        time.sleep(.1)
        #if pb1['value'] == 30:
          
            #time.sleep(1)


def openNewWindow():
     
    # Toplevel object which will
    # be treated as a new window
    newWindow = Toplevel(tab1can)
 
    # sets the title of the
    # Toplevel widget
    newWindow.title("New Window")
 
    # sets the geometry of toplevel
    newWindow.geometry("200x200")
 
    # A Label widget to show in toplevel
    Label(newWindow,
          text ="This is a new window").pack()
    inner_win2 = Canvas(newWindow,height=300,width=300,bg="red")
    inner_win2.pack()
    testtxt(inner_win2,50,60,10,"white","ER1 H&S : ")
    testcir(inner_win2,130,70,150,50,"#FFF")

    e = Entry(inner_win2,width=40)
    e.pack()

    la1 = Label(inner_win1,text="nnnn")

    cmd_4 = Button(newWindow, text="Test Window CMD",command=clicked(newWindow,la1))
    cmd_4.place(x=50, y=50)

def clicked(win,myLabel):
         myLabel = Label(win,text=e.get())
         myLabel.pack()    

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
inner_win1 = Canvas(main_win,height=750,width=1100,bg="#000")
inner_win1.pack()
##################
tabs = Notebook(inner_win1)

tab1 = Frame(tabs)
tab2 = Frame(tabs)

tabs.add(tab1,text="General HS")
tabs.add(tab2,text="Detailed (in work)")
tabs.pack(expand=1,fill="both")


tab1can = Canvas(tab1,height=650,width=950,bg="#000")
tab2can = Canvas(tab2,height=650,width=950,bg="#000")
tab1can.pack()
tab2can.pack()



#HS Side area
#################################
#function for a rectangle
#draw the main label
testrec(tab1can,0,0,160,40,"blue","white")
testtxt(tab1can,75,20,11,"black","EXPRESS RACK H&S")
#draw ER1 HS text
testtxt(tab1can,75,60,10,"white","ER1 H&S : ")
testcir(tab1can,130,70,150,50,"#FFF")
#draw ER2 HS text
testtxt(tab1can,75,90,10,"white","ER2 H&S : ")
testcir(tab1can,130,100,150,80,"#FFF")


#################################
#Main ER Boxes 
#################################

#ER1 Detail display
testrec(tab1can,200,10,300,210,"blue","white")
# RPC boxes
#main
mainlight = tab1can.create_rectangle(201, 10, 249, 20,outline="red",fill="white")
testtxt(tab1can,220,15,7,"black","MAIN")
#safing
auxlight = tab1can.create_rectangle(251, 10, 299, 20,outline="red",fill="white")
testtxt(tab1can,270,15,7,"black","AUX")

# RIC 
er1ric_cir = tab1can.create_oval(
    210, 35, 220,45,
    fill="white",
    tags="er1"
    )
testtxt(tab1can,240,40,8,"black","RIC")

e1ric = tab1can.create_text(
        260,40,
        fill="black",
        font=f"Times 8 italic bold",
        text="0 N",tags="e1")
# RFCA
er1rfca_cir = tab1can.create_oval(
    210, 55, 220,65,
    fill="white",
    tags="er1"
    )
testtxt(tab1can,240,60,8,"black","RFCA")

e1rfca = tab1can.create_text(
        280,60,
        fill="black",
        font=f"Times 8 italic bold",
        text="0 N",tags="e1")

# AAA
er1aaa_cir = tab1can.create_oval(
    210, 75, 220,85,
    fill="white",
    tags="er1"
    )

testtxt(tab1can,240,80,8,"black","AAA")
er1aaaspeed_ = tab1can.create_text(
        280,80,
        fill="black",
        font=f"Times 8 italic bold",
        text="0 N",tags="e1")
#ER2 Detail display
testrec(tab1can,310,10,410,210,"blue","white")


#################################
# NOT RACK STUFF and TESTING
#################################

e = Entry(main_win,width=50)
e.pack()
tt = tab1can.create_text(
        300,300,
        fill="white",
        font=f"Times 12 italic bold",
        text="0 N",tags="tryme")

cmd_ = Button(tab1can, text="CMD",command=eract)
cmd_.place(x=250, y=500)
cmd_2 = Button(tab1can, text="CMD w/ Status",command=start_data)
cmd_2.place(x=350, y=500)
cmd_3 = Button(tab1can, text="Test Window",command=openNewWindow)
cmd_3.place(x=450, y=500)


#################################
#BOTTOM TEXT AREA
#################################
_label2 = Label(main_win,text="Bottom Title Area")
#tab1can.after(1000,er1display)
_label2.pack() # to make it above main canvas


# text i need 

# updating telemtry values

tab1can.mainloop()
main_win.mainloop()

