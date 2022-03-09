
from turtle import bgcolor, clear
from matplotlib.pyplot import text
import requests,os
from tkinter import *
from tkinter.ttk import *
from pathlib import Path
import yagmail

# working in logic to detect os and set file save directory

intro = 'This simple tool will make a\n request  to an API that holds \ndata from data breaches'
#
url = "https://breachdirectory.p.rapidapi.com/"
#
headers = {
    'x-rapidapi-host': "breachdirectory.p.rapidapi.com",
    'x-rapidapi-key': "< your rapid api key for breach directory >"
    }
#
querystring = {"func":"","term":""}
def api_call():
    searchq(f"{e.get()}",'auto')

def searchq(email_,func_):
    user = e2.get()
    password = e3.get()
    querystring["term"] = email_
    querystring["func"] = func_
    yag = yagmail.SMTP(user, password)
    receiver_email = user
    response = requests.request("GET", url, headers=headers, params=querystring)
    addin()

    openfile = f"{Path.home()}\Desktop\BreachData.txt" # windows 
    r=open(f"{openfile}",'a')
    r.write(f"Data entry for: {email_}")
    r.write(f"-------------------------\n\n")
    r.write(f"{response.json()}")
    r.write(f"-------------------------")
    r.write(f"-------------------------")
    r.close()
    addin()

    cmd_ = Button(c1, text="- - -")
    cmd_.place(x=250, y=360)   
    contents = f"data for emali: {email_} \n --------------------- {response.json()}"
    subject = f"Breach Directory : {email_}"
    yag.send(receiver_email, subject, contents)
    
    addin()

    nn = Button(c1,text="Click to close and view your files",command=view)
    nn.place(x=60,y=260)
    nn2 = Button(c1,text="Click to close",command=done)
    nn2.place(x=60,y=300)
    #hh = Label(text=f"file downloaded to {openfile}\n Click View/Close or Close or Search Again")
    #hh.place(x=20,y=210)
    c1.create_text(
        205,210,
        fill="white",
        font=f"Times 11 italic bold",
        text=f"file downloaded to {openfile}\n Click View/Close or Close or Search Again",tags='popup')
    nn3 = Button(c1,text="Searcg Again",command=again)
    nn3.place(x=150,y=360)
    addin()
    
def done():
    exit()

def view():
    openfile = f"{Path.home()}"
    os.system(f"powershell -c notepad.exe {openfile}\Desktop\stolendata.txt")
    exit()

def addin():
    pb1["value"]+=25 

def again():
    pb1['value'] = 0
    c1.delete('popup')
    e = Entry(c1,width=30)
    e.place(x=160,y=110)
    e2 = Entry(c1,width=30)
    e2.place(x=160,y=135)
    e3 = Entry(c1,width=30)
    e3.place(x=160,y=160)
    cmd_ = Button(c1, text="Next" ,command=api_call)
    cmd_.place(x=250, y=360)



root = Tk()
root.title("Email Breach Checker")
root.geometry("450x450")
root['bg']='red'
#
style = Style()
style.theme_use('default')
style.configure('TNotebook.Tab', background="Red")
style.map("TNotebook", background= [("selected", "red")])
#
tabs = Notebook(root)
tab1 = Frame(tabs)
tab2 = Frame(tabs)
tab3 = Frame(tabs)
tabs.add(tab1,text="Console")
tabs.add(tab2,text="Results")
tabs.add(tab2,text="Info/Help")
tabs.pack(expand=1,fill="both")
#

c1 = Canvas(tab1,height=450,width=450,bg="#000")
c1.place(x=0, y=0)
pb1 = Progressbar(c1,orient=HORIZONTAL,length=100,mode='determinate')
pb1.place(x=50, y=50)
e = Entry(c1,width=30)
e.place(x=160,y=110)
e2 = Entry(c1,width=30)
e2.place(x=160,y=135)
e3 = Entry(c1,width=30)
e3.place(x=160,y=160)


l1 = Label(c1,text="email to search")
l1.place(x=20, y=115)
l2 = Label(c1,text=f" your gmail : ")
l2.place(x=20, y=140)
l3 = Label(c1,text=" password ")
l3.place(x=20, y=165)
l4 = Label(c1,text=intro)
l4.place(x=250,y=300)

cmd_ = Button(c1, text="Next" ,command=api_call)
cmd_.place(x=250, y=360)
img = PhotoImage(file='')
Label(
    c1,
    image=img,width=100,
).place(x=355,y=10)
c2 = Canvas(root,height=20,width=200,bg="red")
c2.place(x=120, y=40)
c2.create_text(
        105,10,
        fill="white",
        font=f"Times 12 italic bold",
        text="breachchecker - v2",tags='heading')

reset_btn = Button(c1,text="Reset",command=again)
reset_btn.place(x=340,y=360)

c1.mainloop()
root.mainloop()