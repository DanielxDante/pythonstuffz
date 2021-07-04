SIZE = 4
board1 = [[1, 0, 3, 0], [3, 0, 0, 2], [4, 3, 2, 1], [0, 0, 0, 3]]
board2 = [[0, 1, 3, 2], [2, 0, 1, 0], [1, 0, 0, 3], [3, 4, 2, 1]]
board3 = [[0, 0, 0, 0], [0, 1, 2, 4], [0, 3, 4, 1], [0, 4, 0, 2]]
in_a_row=[1,2,3,4]

def fill_row(board):
    changed=False

    for i in range(4):
        if board[i].count(0)==1:
            j=board[i].index(0)
            if 1 not in board[i]:
                board[i][j]=1
            elif 2 not in board[i]:
                board[i][j]=2
            elif 3 not in board[i]:
                board[i][j]=3
            elif 4 not in board[i]:
                board[i][j]=4
            changed=True
    return changed

def fill_col(board):
    checked=False
    lst=[]

    for i in range(4):
        for j in range(4):
            lst.append(board[j][i])

        if lst.count(0)==1:
            r=lst.index(0)
            if 1 not in lst:
                board[r][i]=1
            elif 2 not in lst:
                board[r][i]=2
            elif 3 not in lst:
                board[r][i]=3
            elif 4 not in lst:
                board[r][i]=4
                
            checked=True
            
        lst=[]
    return checked

def fill_section(board):
    checked=False
    lst=[]

    for i in range(0,4,2): #column
        for j in range(0,4,2): #row
            lst.append(board[j][i])
            lst.append(board[j][i+1])
            lst.append(board[j+1][i])
            lst.append(board[j+1][i+1])
            print(lst)

        if lst.count(0)==1:
            r=lst.index(0)
            print(r)
            if 1 not in lst:
                board[r][i]=1
            elif 2 not in lst:
                board[r][i]=2
            elif 3 not in lst:
                board[r][i]=3
            elif 4 not in lst:
                board[r][i]=4

            checked=True

        lst=[]
    return board
print(fill_section(board1))
