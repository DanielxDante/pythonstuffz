def make_matrix(seq):
    mat=[]
    for row in seq:
        mat.append(list(row))
    return mat

def rows(mat):
    no_rows=0
    for row in mat:
        no_rows+=1
    return no_rows

def cols(mat):
    no_cols=0
    for row in mat:
        for col in mat:
            no_cols+=1
        return no_cols

def get(mat,i,j):
    return mat[i][j]

def set(mat,i,j,val):
    mat[i][j]=val
    return "Value set"

def transpose(mat):
    pass #IDK

def print_matrix(mat):
    for row in range(0,3):
        line=""
        for col in range(0,3):
            line+=str(mat[row][col])+"    "
        print(line)

m=[[1,2,3],[4,5,6],[7,8,9]]
print(make_matrix(m))
print(rows(m))
print(cols(m))
print(set(m,0,0,2))
print(get(m,0,0))
print(print_matrix(m))

