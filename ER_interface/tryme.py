from interface import testtxt,testrec
#################################
#Main ER Boxes 
#################################

#ER1 Detail display
testrec(inner_win1,200,10,300,210,"blue","white")
# RPC boxes
#main
testrec(inner_win1,201,10,249,20,"red","white")
testtxt(inner_win1,220,15,7,"black","MAIN")
#safing
testrec(inner_win1,251,10,299,20,"red","white")
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