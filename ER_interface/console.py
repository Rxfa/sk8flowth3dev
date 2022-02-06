from tokenize import Pointfloat
from graphics import *
from racks import *
#from loading_bar import *
#from test import *



def main():
    window = GraphWin("Window Name",1000,800) # window name and sizes
    window.setBackground('black') # bg color

    heading = Rectangle(Point(0,0),Point(150,100))
    heading.setFill('white')
    heading.setOutline('red')
    heading.draw(window)

    ER1DisplayBox = Rectangle(Point(200,20),Point(400,300))
    ER1DisplayBox.setFill('white')
    ER1DisplayBox.setOutline('yellow')
    ER1DisplayBox.draw(window)

    er1HS_stream = Text(Point(250,30),ER1.rackHS()[0])
    er1HS_stream.setTextColor('green')
    er1HS_stream.setSize(9)
    er1HS_stream.draw(window)

    er1aaabox = Circle(Point(260,80),10) # (from the left, from the top)
    er1aaabox.setFill('red')
    er1aaabox.draw(window)
    
    er1HS_stream_aaa_pwr = Text(Point(220,80),"AAA Pwr")
    er1HS_stream_aaa_pwr.setTextColor('black')
    er1HS_stream_aaa_pwr.setSize(9)
    er1HS_stream_aaa_pwr.draw(window)

    er1HS_stream_aaa = Text(Point(300,80),"")
    er1HS_stream_aaa.setTextColor('black')
    er1HS_stream_aaa.setSize(11)

    er1flow = Circle(Point(260,100),10) # (from the left, from the top)
    er1flow.setFill('red')
    er1flow.draw(window)
    
    er1HS_flow_pwr = Text(Point(220,100),"RFCA Pwr")
    er1HS_flow_pwr.setTextColor('black')
    er1HS_flow_pwr.setSize(9)
    er1HS_flow_pwr.draw(window)

    er1HS_stream_flow = Text(Point(300,100),"")
    er1HS_stream_flow.setTextColor('black')
    er1HS_stream_flow.setSize(11)
    
    text = Text(Point(70,30),"Rack HS Monitor") # (from the left, from the top)
    text.setTextColor('black')
    text.setSize(13)
    text.draw(window)
    
    l = Line(Point(147,100),Point(147,600))
    l.setOutline("white")
    l.setWidth(5)
    l.draw(window)

    er1HSlabel = Text(Point(50,120),"ER1 HS : ") # (from the left, from the top)
    er1HSlabel.setTextColor('white')
    er1HSlabel.draw(window)
    
    er1HSbox = Circle(Point(100,120),10) # (from the left, from the top)
    er1HSbox.setFill('white')
    er1HSbox.draw(window)


    er2HSlabel = Text(Point(50,160),"ER2 HS : ") # (from the left, from the top)
    er2HSlabel.setTextColor('white')
    er2HSlabel.draw(window)
    
    er2HSbox = Circle(Point(100,160),10) # (from the left, from the top)
    er2HSbox.setFill('white')
    er2HSbox.draw(window)

    er3HSlabel = Text(Point(50,200),"ER3 HS : ") # (from the left, from the top)
    er3HSlabel.setTextColor('white')
    er3HSlabel.draw(window)
    
    er3HSbox = Circle(Point(100,200),10) # (from the left, from the top)
    er3HSbox.setFill('white')
    er3HSbox.draw(window)

    er4HSlabel = Text(Point(50,240),"ER4 HS : ") # (from the left, from the top)
    er4HSlabel.setTextColor('white')
    er4HSlabel.draw(window)
    
    er4HSbox = Circle(Point(100,240),10) # (from the left, from the top)
    er4HSbox.setFill('white')
    er4HSbox.draw(window)

    er1HS = Text(Point(100,120),"N") # (from the left, from the top)
    er1HS.setTextColor('black')
    er2HS = Text(Point(100,160),"N") # (from the left, from the top)
    er3HS = Text(Point(100,200),"N") # (from the left, from the top)
    er4HS = Text(Point(100,240),"N") # (from the left, from the top)
    
    er1HS.draw(window)
    er2HS.draw(window)
    er3HS.draw(window)
    er4HS.draw(window)
    er1HS_stream_aaa.draw(window)
    er1HS_stream_flow.draw(window)

   # text.setTextColor('#FFF')
    

    while True:
        er1HS.setText(ER1.HS_count)
        er2HS.setText(ER2.HS_count)
        er3HS.setText(ER3.HS_count)
        er4HS.setText(ER4.HS_count)
        #er1HS_stream.setText(ER1.rackHS())
       

        if int(ER1.AAA['powered']) == 0:  
            
            er1aaabox.setFill('red')
            er1HS_stream_aaa.setText('N')
            ER1.SSPCM_Init()
            time.sleep(2)
        else:  
            er1aaabox.setFill('green')
            #ER1.AAA['powered'] = 0
            er1HS_stream_aaa.setText(f" {ER1.rackHS()[2]}")
        if int(ER1.FLOW['powered']) == 0:  
            
            er1flow.setFill('red')
            er1HS_stream_flow.setText('N')
            #ER1.SSPCM_Init()
            #time.sleep(2)
        else:  
            er1flow.setFill('green')
            #ER1.AAA['powered'] = 0
            er1HS_stream_flow.setText(f" {ER1.rackHS()[3]}")

        
        if int(ER1.HS_count) < 3:
            er1HS.setTextColor('red')
            er1HSbox.setFill('yellow')

        else: er1HS.setTextColor('black');er1HSbox.setFill('white')

        if int(ER2.HS_count) < 3:
            er2HSbox.setFill('yellow')
            er2HS.setTextColor('red')

        else: er2HS.setTextColor('black');er2HSbox.setFill('white')

        if int(ER3.HS_count) < 3:
                    er3HSbox.setFill('yellow')
                    er3HS.setTextColor('red')

        else: er3HS.setTextColor('black');er3HSbox.setFill('white')

        if int(ER4.HS_count) < 3:
            er4HSbox.setFill('yellow')
            er4HS.setTextColor('red')

        else: er4HS.setTextColor('black');er4HSbox.setFill('white')
    

    #inputbox = Entry(Point(200,350),20)
    #inputbox.setFill('white') # bg color
    #inputbox.draw(window)

    

    window.getMouse()
    window.close()


# start program 
main()