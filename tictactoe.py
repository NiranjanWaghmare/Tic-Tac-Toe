import random
board = [['-','-','-'],['-','-','-'],['-','-','-']]
print("Lets play Tic Tac Toe")
count  = 0

i =0
j=0
print("\n")
print("These will be the coordinates of board")
print("\n")
for i in range(len(board)):
    for j in range(len(board)):
        print("[ %d %d ]" %(i, j), end = "  ")
    print("\n")
        
    

#checking cnditions
def check(X):
    if(((board[0][0] == X) and (board[1][1] == X) and (board[2][2] == X)) or ((board[0][2] == X) and (board[1][1] == X) and (board[2][0] == X)) or ((board[0][0] == X) and (board[0][1] == X) and (board[0][2] == X)) or ((board[1][0] == X) and (board[1][1] == X) and (board[1][2] == X)) or ((board[2][0] == X) and (board[2][1] == X) and (board[2][2] == X)) or ((board[0][0] == X) and (board[1][0] == X) and (board[2][0] == X)) or  ((board[0][1] == X) and (board[1][1] == X) and (board[2][1] == X)) or ((board[0][2] == X) and (board[1][2] == X) and (board[2][2] == X))):
        return 1
    else:
        return 0




def AllocateValues(token,x,y):
    while True:
        if board[x][y] == '-' :
            board[x][y] = token
            return False
        else:
            return True
    

            

while count < 9 :
    #print( "Count   ", count)
    result = True
    result1 = True
    if (check('X') == 1) :
        print("-"*50)
        print("You Win")   
        print("-"*50)
        count = 10
        break  
    elif check('O') == 1:
            print("-"*50)
            print("Computer Win")
            print("-"*50)
            count = 10
            break
    else:   
        while (result == True) :
            if count >= 9:
                print("Board is full!! player")
                break
                #print( "Count   ", count)
            #print("Player's turn : ")
            x, y = list(map(int,input("Enter the row and column number : ").split()))
            if((x in range(0,3)) and (y in range(0,3))):
                result = AllocateValues('X',x,y)
                if result == False:
                    count  = count + 1 
            else:
                print("Please enter between 0 to 2 for X and Y coordinate")

        while (result1 == True) :
            if count >= 8:
                break

            cx = random.randint(0,2)
            cy = random.randint(0,2)
            print("Computer's turn : ")
            print("Computer played on  : %d %d" %(cx ,cy))
            result1 = AllocateValues('O',cx,cy) 
            if result1 == False:
                count  = count + 1       
            
        for arr in board:
                print(arr)    
        if count >= 9:
                print("-"*50)
                print("Thankyou for playing")
                


        #check if we won

        # if board[0][0]:````
 