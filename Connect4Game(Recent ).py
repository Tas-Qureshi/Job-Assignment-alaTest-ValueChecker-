
# | | | | | |  0
#------------- 1
# | | | | | |  2
#------------- 3 
# | | | | | |  4
#------------- 5 
# | | | | | |  6
#------------- 7 
# | | | | | |  8
#------------- 9 
# | | | | | |  10
#1234567890123
#---------------------------------------------------------
#Variables



# drawing Board
#---------------------------------------------------------------------------

def drawBoard(currentField):
    rowsLimit = 11
    columnsLimit = 13
    #Loop for creating rows
    for row in range(rowsLimit):  #0,1,2,3,4,5,6,.,8,.,10
                                  #0,.,1,.,2,.,6,.,8,.,10
        
        if row%2 == 0: # 0,2,4,6,8,10
            #we need 0,2,4,6 to become 0,1,2,3 so we can add players values in the board for rows
            practicalRow= int(row/2)
            for column in range(columnsLimit):  #0,1,2,3,4,5,6,7,8,9,10
                                                #0,.,1,.,2,.,3,.,4,., 5
                
                if column%2 == 0: # 0,2,4,6,8,10,12
                   #we need 0,2,4,6,8,10,12 to become 0,1,2,3,4,5,6 so we can add players values in the board for rows
                    practicalColumn = int(column/2)
                    if column != columnsLimit-1:
                        print(currentField[practicalColumn][practicalRow], end = "")
                        #Print(" ", end="") # 1,3 iterations of the loop
                    else:
                        print(currentField[practicalColumn][practicalRow]) #5 iteration of the loop
                        
                else:
                    print("|", end="") #2,4
                     # print(" | | ")
                     #       "12345"
        else:
            print("-------------")



#Saving players move in the list
#-----------------------------------------------

field = [[" ", " ", " "," "," "," "], [" ", " ", " ", " "," "," "], [" ", " ", " "," "," ", " "], [" ", " ", " "," "," ", " "], [" ", " ", " "," "," ", " "], [" ", " ", " "," "," ", " "], [" ", " ", " "," "," ", " "]]

player = 1
# To Draw the board first
drawBoard(field)
#-------------------------------------------Wins--------------------------
#-------------Check each row (function)-----------------------------

def findWinInRows():
    for col in range(7):
        for row in range(5,-1,-1):
            if field[col][row] == "O" and field[col][row-1] == "O" and field[col][row-2] == "O" and field[col][row-3] == "O":
                 return True
                 break
            elif field[col][row] == "X" and field[col][row-1] == "X" and field[col][row-2] == "X" and field[col][row-3] == "X":
                  return True
                  break

#------------------------------------------------------------------------------
#--------------------------Check each Column (function)------------------------
def findWinInColumns():
  for col in range(6,2,-1):
        for row in range(6):
            if field[col][row] == "O" and field[col-1][row] == "O" and field[col-2][row] == "O" and field[col-3][row] == "O":
                return True
                break
            elif field[col][row] == "X" and field[col-1][row] == "X" and field[col-2][row] == "X" and field[col-3][row] == "X":
                   return True
                   break


#------------------------------------------------------------------------------

#--------------------- Check Reverse Diagnal function----------------------------------

def findWinInReverseDiagnals():
    for col in range(6,2,-1):
        for row in range(5,3,-1):
            if field[col][row] == "O" and field[col-1][row-1] == "O" and field[col-2][row-2] =="O" and field[col-3][row-3]=="O":
                #print("Correct for O")
                return True
                break
            elif field[col][row] == "X" and field[col-1][row-1] == "X" and field[col-2][row-2] =="X" and field[col-3][row-3] == "X":
                #print("Correct for X")
                return True
                break

#------------------------------------------------------------------------------

##---------------------------check Diagnal function----------------------------

def findWinInDiagnals():
    for col in range(6,2,-1):
        for row in range(3):
            if field[col][row] == "O" and field[col-1][row+1] == "O" and field[col-2][row+2] =="O" and field[col-3][row+3]== "O":
                return True
                break
            elif field[col][row] == "X" and field[col-1][row+1] == "X" and field[col-2][row+2] =="X" and field[col-3][row+3] == "X":
                return True
                break



#------------------------------------------------------------------------------

# while loop to keep the players in the play till end of game
while(True):
    print("0 1 2 3 4 5 6\n\nPlayers turn: ", player)
    #-------------------------------------------------------------
    # While loop=>check players only can enter integer values between 0 to 2
    while True:
        try:
            moveColumn = int(input("Please enter the Column : "))
            if moveColumn in range(7):
                break
            else:
                print("Please input only between 0 to 6") 
                continue
        except ValueError:
            print("Please input only number between 0 to 6")  
            continue
    
   # moveRow = int(input("Please enter the column:\n"))
            
   #-------------------------------------------------  
    # Move for players
    winPlayer1 = 0
    winPlayer2 = 0              
    if player == 1:
        #make move for player 1
        if moveColumn >= 0 and moveColumn <=6:
            for moveRow in range(5,-1,-1):
                if field[moveColumn][moveRow] == " ":
                    field[moveColumn][moveRow] = "O"
                    if findWinInRows() is True or findWinInColumns() is True or findWinInReverseDiagnals() or findWinInDiagnals() is True:
                        winPlayer1 = 1
                        drawBoard(field)
                        print("\nPlayer 1 Won")
                        break
                    break
                    #break
                else:
                    continue
        if winPlayer1 == 1:
            break
        player = 2
                    
    else:
        if moveColumn >= 0 and moveColumn <=6:
            for moveRow in range(5,-1,-1):
                if field[moveColumn][moveRow] == " ":
                    field[moveColumn][moveRow] = "X"
                    if findWinInRows() is True or findWinInColumns() is True or findWinInReverseDiagnals() or findWinInDiagnals() is True:
                         winPlayer2 = 1
                         drawBoard(field)
                         print("\nPlayer 2 Won")
                         break
                    break
                else:
                    continue
        if winPlayer2 == 1:
            break
        player = 1

                   
    drawBoard(field)   
    # for i in field:
    #      print(i)

                
                                     
         
            
        
    
    

