board = [
    ['metal', 'green', 'ice', 'purple', 'yellow', 'blue', 'purple', 'blue'],
    ['ice', 'green', 'yellow', 'ice', 'yellow', 'purple', 'red', 'metal'],
    ['', 'red', 'metal', 'blue', 'green', 'ice', 'yellow', 'purple'],
    ['green', 'metal', 'purple', 'metal', 'red', 'yellow', 'red', 'blue'],
    ['ice', 'green', 'yellow', 'green', 'ice', 'blue', 'metal', 'green'],
    ['purple', 'blue', 'yellow', 'purple', 'red', 'red', 'yellow', 'yellow'],
    ['metal', 'green', 'blue', 'red', 'purple', 'ice', 'metal', 'green'],
    ['blue', 'ice', 'red', 'metal', 'metal', 'red', 'ice', 'purple']
]



matches=[]
for r, row in enumerate(board):
    for c, col in enumerate(row):
        if(c<5):
            if(col==board[r][c+2]==board[r][c+3]):
                matches.append([[r,c],[r,c+1]])
        if(r>0 and r<7 and c<7):
            if(col==board[r+1][c+1]==board[r-1][c+1]):
                matches.append([[r,c],[r,c+1]])
        if(r<6 and c<7):
            if(col==board[r+1][c+1]==board[r+2][c+1]):
                matches.append([[r,c],[r,c+1]])

        if(r>1 and c<7):
            if(col==board[r-1][c+1]==board[r-2][c+1]):
                matches.append([[r,c],[r,c+1]])
        
        if(c>2):
            if(col==board[r][c-2]==board[r][c-3]):
                matches.append([[r,c],[r,c-1]])
        if(r>0 and r<7 and c>0):
            if(col==board[r+1][c-1]==board[r-1][c-1]):
                matches.append([[r,c],[r,c-1]])
        if(r<6 and c>0):
            if(col==board[r+1][c-1]==board[r+2][c-1]):
                matches.append([[r,c],[r,c-1]])
        if(r>1 and c>0):
            if(col==board[r-1][c-1]==board[r-2][c-1]):
                matches.append([[r,c],[r,c-1]])
            
        if(r<5):
            if(col==board[r+2][c]==board[r+3][c]):
                matches.append([[r,c],[r+1,c]])
        if(c>0 and c<7 and r<7):
            if(col==board[r+1][c-1]==board[r+1][c+1]):
                matches.append([[r,c],[r+1,c]])
        if(c>1 and r<7):
            if(col==board[r+1][c-1]==board[r+1][c-2]):
                matches.append([[r,c],[r+1,c]])
        if(c<6 and r<7):
            if(col==board[r+1][c+1]==board[r+1][c+2]):
                matches.append([[r,c],[r+1,c]])

        if(r>2):
            if(col==board[r-2][c]==board[r-3][c]):
                matches.append([[r,c],[r-1,c]])
        if(c>0 and c<7 and r>0):
            if(col==board[r-1][c-1]==board[r-1][c+1]):
                matches.append([[r,c],[r-1,c]])
        if(c>1 and r>0):
            if(col==board[r-1][c-1]==board[r-1][c-2]):
                matches.append([[r,c],[r-1,c]])
        if(c<6 and r>0):
            if(col==board[r-1][c+1]==board[r-1][c+2]):
                matches.append([[r,c],[r-1,c]])
    
                #click_at_position(, )

#if match empty

print(matches)


#[[2, 5], [2, 6]]