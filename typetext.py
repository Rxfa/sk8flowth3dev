
import time,os
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
import sqlite3
# Databases

# Create a database or connect to one
conn = sqlite3.connect('address_book.db')

# Create cursor
c = conn.cursor()

def testcmds():
    os.system(f"{e2.get()}")

def clicked2():
        txt = str(e.get())
        c.execute(f"""CREATE TABLE {txt} (first_name text,last_name text,address text,city text,	state text,zipcode integer)""")
        myLabel = Label(main_win,text=e.get())
        myLabel.pack()

main_win = Tk()
main_win.title("Interface Project Demo")
main_win.geometry("1000x700")

#################################
#MAIN CANVAS
#################################
# main canvas area for the background
la1 = Label(main_win,text="nnnn")
la1.pack()
e = Entry(main_win,width=40)
e.pack()
la2 = Label(main_win,text="")
la2.pack()
e2 = Entry(main_win,width=40)
e2.pack()






cmd_ = Button(main_win,text="Test Window CMD",command=testcmds)
cmd_.pack()
#inner_win1.pack()
#inner_win1.mainloop()
main_win.mainloop()