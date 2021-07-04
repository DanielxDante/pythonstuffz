from random import *

def InitialiseBoard():
    board = [["O"]*6] * 5
    for i in range(1,5):
          board[i] = ["O"] * 6
    return board

def GameFinished(count, user, ship):
    if count == 3:
        return True
    elif user == ship:
        return True
    else:
        return False
        
def Display(board):
    for row in board[1:]:
        print(" ".join(row[1:]))
    print()
        
grid = InitialiseBoard()
ship = (randint(1,4), randint(1,5)) #row, col
#grid[ship[0]][ship[1]] = "S"

count = 0
user = (0,0)

while GameFinished(count, user, ship) == False:

    Display(grid)
   
    row = int(input("Enter row (1 to 4):"))
    col = int(input("Enter col (1 to 5): "))
    user = (row, col)

    if user == ship:   
        grid[user[0]][user[1]] = "S"
    else:
        grid[user[0]][user[1]] = "X"
  
    count += 1

print()
if user == ship:
    print("You win!")
else:
    print("Game over...")
Display(grid)
