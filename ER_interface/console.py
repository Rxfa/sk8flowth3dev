from tokenize import Pointfloat
from graphics import *
from racks import *
#from loading_bar import *
#from test import *
from tqdm import tqdm
import time

def drawCir(xpos,ypos,r,color,win):
    drawcir = Circle(Point(xpos,ypos),r)
    drawcir.setFill(color)
    drawcir.draw(win)
    return drawcir

def drawCir2(xpos,ypos,r,color):
    drawcir = Circle(Point(xpos,ypos),r)
    drawcir.setFill(color)
    return drawcir

def drawText(xpos,ypos,txtin,color,s,win):
    drawtxt = Text(Point(xpos,ypos),txtin)
    drawtxt.setTextColor(color)
    drawtxt.setSize(s)
    drawtxt.draw(win)
    return drawtxt
def drawText2(xpos,ypos,txtin,color,s):
    drawtxt = Text(Point(xpos,ypos),txtin)
    drawtxt.setTextColor(color)
    drawtxt.setSize(s)
    return drawtxt

def drawRec(x1,y1,x2,y2,fill,outline,win):
    drawrect = Rectangle(Point(x1,y1),Point(x2,y2))
    drawrect.setFill(fill)
    drawrect.setOutline(outline)
    drawrect.draw(win)
    return drawrect

def drawRec2(x1,y1,x2,y2,fill,outline):
    drawrect = Rectangle(Point(x1,y1),Point(x2,y2))
    drawrect.setFill(fill)
    drawrect.setOutline(outline)
    return drawrect

def drawLine(x1,y1,x2,y2,color,w,win):
    l = Line(Point(x1,y1),Point(x2,y2))
    l.setOutline(color)
    l.setWidth(w)
    l.draw(win)

def main():
    window = GraphWin("Window Name",1000,800) # window name and sizes
    window.setBackground('black') # bg color

    #heading box
    drawRec(10,10,150,100,'white','gold',window)
    #heading text
    drawText(70,30,'Header Text','red',12,window)
    #draw line to seperate panel
    drawLine(147,100,147,600,'white',5,window)

    # ER1 label
    drawText(50,120,'ER1 HS : ','white',9,window)
    # ER2 label
    drawText(50,160,'ER2 HS : ','white',9,window)
    # ER3 label
    drawText(50,200,'ER3 HS : ','white',9,window)
    # ER4 label
    drawText(50,240,'ER4 HS : ','white',9,window)

    
     
################
####### ER1 
################
    
    
    # ER1 status circle
    er1hscir = drawRec2(75,110,120,130,'white','gold')
    er1hscir.draw(window)
    # ER1 count
    er1HS = drawText2(90,120,'0 N','black',9)
    er1HS.draw(window)
     # ER1 DisplayBox
    drawRec(200,20,400,300,'white','gold',window)
    # ER1 Name
    drawText(225,50,' - - ','black',9,window)

    # ER1 Display HS count
    er1HSinbox = drawText2(240,80,'HS Count:','black',9)
    er1HSinbox.draw(window)

    # ER1 Display AAA Pwr
    drawText(230,100,'AAA ','black',9,window)
    # ER1 AAA Pwr light
    er1aaapwr = drawCir2(260,100,7,'red')
    er1aaapwr.draw(window)
    # ER1 AAA Speed
    er1aaaspeed = drawText2(290,100,'0 N','black',9)
    er1aaaspeed.draw(window)

    # ER1 Display RFCA Flow
    drawText(230,120,'RFCA ','black',9,window)
    # ER1 RFCA Pwr light
    er1flowcir = drawCir2(260,120,7,'red')
    er1flowcir.draw(window)
    # ER1 RFCA Flow
    er1flow = drawText2(290,120,'0 N','black',9)
    er1flow.draw(window)
################
####### ER2
################
    er2hscir = drawRec2(75,150,120,170,'white','gold')
    er2hscir.draw(window)
    # ER2 count
    er2HS = drawText2(90,160,'0 N','black',9)
    er2HS.draw(window)
    
################
####### ER3
################
    er3hscir = drawRec2(75,190,120,210,'white','gold')
    er3hscir.draw(window)
    # ER3 count
    er3HS = drawText2(90,200,'0 N','black',9)
    er3HS.draw(window)
    
################
####### ER4 
################
    er4hscir = drawRec2(75,230,120,250,'white','gold')
    er4hscir.draw(window)
    # ER2 count
    er4HS = drawText2(90,240,'0 N','black',9)
    er4HS.draw(window)

   # text.setTextColor('#FFF')
    

    while True:
        er1HS.setText(ER1.HS_count)
        er2HS.setText(ER2.HS_count)
        er3HS.setText(ER3.HS_count)
        er4HS.setText(ER4.HS_count)
        #er1HS_stream.setText(ER1.rackHS())
    
        if int(ER1.AAA['powered']) == 0:  
            
            er1aaapwr.setFill('red')
            #er1HS_stream_aaa.setText('N')
            ER1.SSPCM_Init()
            time.sleep(2)
        else:  
            er1aaapwr.setFill('green')
            #ER1.AAA['powered'] = 0
            #er1HS_stream_aaa.setText(f" {ER1.rackHS()[2]}")
        if int(ER1.FLOW['powered']) == 0:  
            
            er1flowcir.setFill('red')
            #er1HS_stream_flow.setText('N')
            #ER1.SSPCM_Init()
            #time.sleep(2)
        else:  
            er1flowcir.setFill('green')
            #ER1.AAA['powered'] = 0
            #er1HS_stream_flow.setText(f" {ER1.rackHS()[3]}")

        
        if int(ER1.HS_count) < 3:
            er1HS.setTextColor('red')
            er1hscir.setFill('yellow')

        else: 
            er1HS.setTextColor('black')#;
            er1hscir.setFill('white')
        if int(ER2.HS_count) < 3:
            er2HS.setTextColor('red')
            er2hscir.setFill('yellow')

        else: 
            er2HS.setTextColor('black')#;
            er2hscir.setFill('white')
    

    #inputbox = Entry(Point(200,350),20)
    #inputbox.setFill('white') # bg color
    #inputbox.draw(window)

    

    window.getMouse()
    window.close()


# start program 
main()