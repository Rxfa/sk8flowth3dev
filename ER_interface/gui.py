import time,requests
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *

#from matplotlib.pyplot import text, title
# import filedialog module
from tkinter import filedialog

# Function for opening the
# file explorer window
def browseFiles():
	filename = filedialog.askopenfilename(initialdir = "./",
										title = "Select a File",
										filetypes = (("Text files",
														"*.txt*"),
													("all files",
														"*.*")))
	
	# Change label contents
	label_file_explorer.configure(text="File Opened: "+filename)
	

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
    lines = ["/","a1c43my"]
    for line in lines:

        t = requests.get(f"{url}/{line}")
 
    la2.config(text=f"{t.headers}")
    la2.after(150,testme)
    myLabel2 = Label(tab1can,text=f"SENT: {e.get()}")
    myLabel2.pack()



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

label_file_explorer = Label(tab2can,
							text = "File Explorer using Tkinter",
							width = 100)

	
button_explore = Button(tab2can,
						text = "Browse Files",
						command = browseFiles)

button_exit = Button(tab2can,
					text = "Exit",
					command = exit)

# Grid method is chosen for placing
# the widgets at respective positions
# in a table like structure by
# specifying rows and columns
label_file_explorer.grid(column = 1, row = 1)

button_explore.grid(column = 1, row = 2)

button_exit.grid(column = 1,row = 3)
main_win.mainloop()