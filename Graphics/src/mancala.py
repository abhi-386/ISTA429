###
### AUTHOR: ABHISHEK AGARWAL
### COURSE: CS110
### DESCRIPTION : THIS IS A PROGRAM BASED ON A GAME CALLED MANCALA WHICH WAS PLAYED IN INDIA AND SPEAERD THEIR AFTREWARDS.
###               THIS PROGRAM IS BASED ON DIFFRENT FUNCTION WHICH DOES DIFFRENT PARTS FOR THE PROGRAM.
###               THIS PROGRAM IS PLAYED BY TWO USER WHO RACE TO SCORE FIRST THREE POINTS AND WIN IT THE GAME.

from graphics import graphics
def user_input( player ):
    # THIS FUNCTION TAKES THE INPUT FROM USER
    # player: THIS TELL US WHICH PLAYER ARE WE TAKING A INPUT
    position = int(input("PLayer " + str( player ) + ": Enter position to start moving chips at:"))
    while True:
        if position in [1,2,3,4,5]:
            return position
        else:
           position = int(input("PLayer "+ str( player) + ": Enter position to start moving chips at:")) 
def create_graphics(gui):
    # THIS FUNCTION IS THE ONE WHICH CREATE BASIC STRUCTURE FOR CANVAS
    gui.rectangle(5,105,90,190,'green')
    x = 95
    while x < 505:
        x += 10
        gui.rectangle(x,105,90,90,'blue')
        gui.rectangle(x,205,90,90,'green')
        x += 90
    gui.rectangle(x+10,105,90,190,'blue')
    gui.text(50,90,'Player 1','black',20)
    gui.text(650,90,'Player 2','black',20)
    gui.text(350,40,'MANCALA','orange',50)
def display( gui , player_1 , player_2 , player1 , player2 ):
    # THIS IS A FUNCTION WHICH DISPLAY THE CANVAS WITH THE RECTANGLE
    # gui: THIS FIRST ARGUMENT WHICH ACCEPT THE GUI WHICH IS A VARIABLE WHICH STORE THE BASIC CANVAS
    # player_1 : THIS IS THE LIST WHICH STORE THE ROW SCORE FOR THE PLAYER 1
    # player_2 : THIS IS THE LIST WHICH STORE THE ROW SCORE FOR THE PLAYER 2
    # player1 : THIS IS A LIST WHICH STORE THE SCORE OF PLAYER 1
    # player2 : THIS IS A LIST WHICH STORE THE SCORE OF PLAYER 1
    gui.clear() # THIS INTIALLY CLEAR THE CANVAS BEFORE DISPLAYING NEW RESULT
    create_graphics(gui) # THIS CREATE THE CANVAS AGAIN WITH NEW RESULTS
    i = 0
    x = 150
    while i < len(player_1):
        gui.text( x , 150 ,  player_2[len(player_2)-1-i] ,'white',70 )
        gui.text( x  ,250 ,  player_1[i] ,'white',70 )
        x += 100
        i += 1
    gui.text( 50 , 200 , player1[0] , 'white' , 50 )
    gui.text( 650 , 200 , player2[0] , 'white' , 50 )
    gui.update_frame(30)
def player_turn (player , position , player_1 , player_2 , player1 , player2 ):
    # THIS IS A FUNCTION WHICH DOES THE MAIN WORK OF WORKING ION THE GAME
    # player : THIS IS A ARGUMENT WHICH TELL WHICH IS THIS PLAYER 
    # position : THIS TELL WHICH POSITION DOES THE PLAYTER WANTS TO START
    # player_1 : THIS IS THE LIST WHICH STORE THE ROW SCORE FOR THE PLAYER 1
    # player_2 : THIS IS THE LIST WHICH STORE THE ROW SCORE FOR THE PLAYER 2
    # player1 : THIS IS A LIST WHICH STORE THE SCORE OF PLAYER 1
    # player2 : THIS IS A LIST WHICH STORE THE SCORE OF PLAYER 1
    value = 0
    position -= 1
    if player == 1 :
        value = player_1 [ position ]
        player_1 [ position ] = 0
        position += 1
        while value > 0 :
            if player1[0] == 3:
                return # THIS OPT OF THE FUCTION WHEN TRIGGERED.
            elif position < 5:
                if value == 1 and player_1[position] == 0:
                    player1[0] += 1
                    return
                player_1[position] += 1
            elif position >= 5 and position <= 9:
                i = position - 5
                if value == 1 and player_2[i] == 0:
                    player1[0] += 1
                    return
                player_2[i] += 1
            elif position >9:
                position = 0
                player1[0] += 1
            position += 1
            value -= 1
    if player == 2:
        value = player_2 [ position ]
        player_2 [ position ] = 0
        position += 1
        while value > 0 :
            if player2[0] == 3:
                return
            elif position < 5:
                if value == 1 and player_2[position] == 0:
                    player2[0] += 1
                    return
                player_2[position] += 1
            elif position >= 5 and position <= 9:
                i = position - 5
                if value == 1 and player_1[i] == 0:
                    player2[0] += 1
                    return
                player_1[i] += 1
            elif position >9:
                position = 0
                player2[0] += 1
            position += 1
            value -= 1
        
def main():
    # THIS IS THE MAIN FUCTION WHICH IS REFERED FIRST.
    gui = graphics(700, 300, 'MANCALA') # CANVAS OF WIDTH 700 AND HEIGHT OF 300 UNDER THE NWME OF MANCALA IS CREATYED
    # THE FOLLOWING FOUR LIST CONTAIN THE SCORE FOR THE PLAYER
    player_1 = [3,3,3,3,3] 
    player_2 = [3,3,3,3,3]
    player1 = [0]
    player2 = [0] 
    while True: # THIS IS A CONDITION WHICH HELPS US TO SWITCH ON THE TURN BETWEEN THE PLAYER
        display( gui , player_1 , player_2 , player1 , player2 ) # IT INITIAL DISPLAY THE CANVAS
        player = 1
        position = user_input(player)
        player_turn (player , position , player_1 , player_2 , player1 , player2 )
        display( gui , player_1 , player_2 , player1 , player2 )
        if player1[0] == 3 :
            print ("PLayer", str( player ) + " wins!")
            exit = input ( "Press any key to exit" )
            return       
        player = 2
        position = user_input(player)
        player_turn (player , position , player_1 , player_2 , player1 , player2 )
        display( gui , player_1 , player_2 , player1 , player2 )
        if player2[0] == 3 :
            print ("PLayer", str( player ) + " wins!")
            exit = input ( "Press any key to exit" )
            return # THIS IS A ALTERNATIVE FOR EXIT.
main()
