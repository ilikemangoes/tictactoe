def winner():
    if (board1[0][0]=='x' and board1[1][0]=='x' and board1[2][0]=='x') or (board1[0][0]=='o' and board1[1][0]=='o' and board1[2][0]=='o'):
        return True
    elif (board1[0][1]=='x' and board1[1][1]=='x' and board1[2][1]=='x') or (board1[0][1]=='o' and board1[1][1]=='o' and board1[2][1]=='o'):
        return True
    elif (board1[0][2]=='x' and board1[1][2]=='x' and board1[2][2]=='x') or (board1[0][2]=='o' and board1[1][2]=='o' and board1[2][2]=='o'):
        return True
    elif (board1[0][0]=='x' and board1[0][1]=='x' and board1[0][2]=='x') or (board1[0][0]=='o' and board1[0][1]=='o' and board1[0][2]=='o'):
        return True
    elif (board1[1][0]=='x' and board1[1][1]=='x' and board1[1][2]=='x') or (board1[1][0]=='o' and board1[1][1]=='o' and board1[1][2]=='o'):
        return True
    elif (board1[2][0]=='x' and board1[2][1]=='x' and board1[2][2]=='x') or (board1[2][0]=='o' and board1[2][1]=='o' and board1[2][2]=='o'):
        return True
    elif (board1[0][0]=='x' and board1[1][1]=='x' and board1[2][2]=='x') or (board1[0][0]=='o' and board1[1][1]=='o' and board1[2][2]=='o'):
        return True
    elif (board1[2][0]=='x' and board1[1][1]=='x' and board1[0][2]=='x') or (board1[2][0]=='o' and board1[1][1]=='o' and board1[0][2]=='o'):
        return True
    else:
        return False

def put_on_board(piece,row,column):
    board1[int(row)][int(column)]=piece
    print_board(board1)

def check_board(row,column):
    if row=='' or column=='': 
        return False
    if int(row)<3 and int(column)<3:

        if board1[int(row)][int(column)]=='_':
            return True
        else:
            return False
    else: 
        return False

def create_new_board():
    board=[
    ['_','_','_'],
    ['_','_','_'],
    ['_','_','_']
    ]
    return board

def print_board(board):
    for row in board:
        for position in range(0,3):
            print(row[position], end= ' ')
        print()

board1=create_new_board()
turn=0
print_board(board1)

while turn < 9:
    row=input('Which row do you want?:  ')
    column=input('Which column do you want?:  ')
    player=turn%2
    if check_board(row,column)==True:
        if player==0:
            put_on_board("x",row,column)
            print("it's player o's turn next")
           
        else:
            put_on_board("o",row,column)
            print("it's player x's turn next")
        turn=turn+1
    else:
        print("Sorry, we can't put a piece in the position you gave.")
    print()
    if winner():
        player=str(player)
        print('The winner of this game is player '+ player + '!')
        break
print('End of game :(')