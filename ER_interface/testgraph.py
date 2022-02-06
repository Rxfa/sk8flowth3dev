from graphics import *
from racks import *


def main():
    window = GraphWin("HS Monitor",1000,1000) # window name and sizes
    #window.setBackground('black') # bg color
    er1HSbox = Circle(Point(100,100),10) # (from the left, from the top)
    er1HSbox.setFill('white')
    er1HSbox.draw(window)
    er1HScount = Text(Point(50,100),"ER1 HS : ") # (from the left, from the top)
    er1HScount.draw(window)

    er2HSbox = Circle(Point(100,150),10) # (from the left, from the top)
    er2HSbox.setFill('white')
    
    er2HScount = Text(Point(50,150),"ER2 HS : ") # (from the left, from the top)
    er2HSbox.draw(window)
    er2HScount.draw(window)
    

    er3HSbox = Circle(Point(100,200),10) # (from the left, from the top)
    er3HSbox.setFill('white')
    
    er3HScount = Text(Point(50,200),"ER3 HS : ") # (from the left, from the top)
    er3HSbox.draw(window)
    er3HScount.draw(window)
    

    er4HSbox = Circle(Point(100,250),10) # (from the left, from the top)
    er4HSbox.setFill('white')
    er4HScount = Text(Point(50,250),"ER4 HS : ") # (from the left, from the top)
    er4HSbox.draw(window)
    er4HScount.draw(window)

    er1HS = Text(Point(100,100),"First Text") # (from the left, from the top)
    er2HS = Text(Point(100,150),"First Text") # (from the left, from the top)
    er3HS = Text(Point(100,200),"First Text") # (from the left, from the top)
    er4HS = Text(Point(100,250),"First Text") # (from the left, from the top)
    er1HS.draw(window)
    er2HS.draw(window)
    er3HS.draw(window)
    er4HS.draw(window)
   # text.setTextColor('#FFF')
    

    while True:
        er1HS.setText(ER1.HS_count)
        er2HS.setText(ER2.HS_count)
        er3HS.setText(ER3.HS_count)
        er4HS.setText(ER4.HS_count)
        
        if int(ER1.HS_count) < 3:
            er1HS.setTextColor('red')
            er1HSbox.setFill('yellow')

        else: er1HS.setTextColor('black');er1HSbox.setFill('white')

        if int(ER2.HS_count) < 3:
            er2HS.setTextColor('red')

        else: er2HS.setTextColor('black')

        if int(ER3.HS_count) < 3:
            er3HS.setTextColor('red')

        else: er3HS.setTextColor('black')

        if int(ER4.HS_count) < 3:
            er4HS.setTextColor('red')

        else: er4HS.setTextColor('black')


# start program 
main()