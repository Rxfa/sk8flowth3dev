from graphics import *


def drawCir(xpos,ypos,r):
    drawcir = Circle(Point(xpos,ypos),r)
    return drawcir

def drawText(xpos,ypos,txtin):
    drawtxt = Text(Point(xpos,ypos),txtin)
    return drawtxt

def main():
    window = GraphWin("HS Monitor",500,500) # window name and sizes
    #window.setBackground('black') # bg color
    er1HSbox = drawCir(100,100,10) # (from the left, from the top)
    er1HSbox.setFill('white')
    er1HSbox.draw(window)
    er1HScount = drawText(50,100,"ER1 HS : ") # (from the left, from the top)
    er1HScount.draw(window)


    #er1HS = Text(Point(100,100),"First Text") # (from the left, from the top)

    #er1HS.draw(window)
    window.getMouse()
    window.close()
   # text.setTextColor('#FFF')
       
    




# start program 
main()