def  fill_zero(matrix,visited,cell):
    for row in range(0,len(matrix)):
        if matrix[row][cell[1]]==0:
            continue
        poss=1<< int(row*len(matrix[0])+cell[1])
        visited[0]=visited[0] ^ poss
        matrix[row][cell[1]]=0
    
    for col in range(0,len(matrix[0])):
        if matrix[cell[0]][col]==0:
            continue
        poss=1<< int((cell[0]*len(matrix[0]))+col)
        visited[0]=visited[0] ^ poss
        matrix[cell[0]][col]=0


def do_dfs(matrix,cell,visited):
    moves=[(0,1),(1,0)]
    pos=cell[0]*len(matrix[0])+cell[1]
    if len(str( bin(visited[0]) )[2:])>pos and str( bin(visited[0]))[2:][pos] =='1':
        return None
    poss=1<< int(cell[0]*len(matrix[0])+cell[1])
    visited[0]=visited[0] ^ poss

    if matrix[ cell[0] ][ cell[1] ]==0:
        fill_zero(matrix,visited,cell)  
    # else:
    #     for move in moves:
    #         new_move= move[0]+cell[0],move[1]+cell[1]         	
    #         if in_range(matrix,new_move):
    #             do_dfs(matrix,new_move,visited)


def  in_range(matrix,move):
    return 0<= move[0]<len(matrix) and   0<= move[1]<len(matrix[0])



def main(matrix):
    visited=[0]
    if len(matrix)<0 or len(matrix[0])<0:
        return matrix
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            cell=(i,j)
            do_dfs(matrix,cell,visited)
    return matrix

matrix=[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]

maxt=[
    [1,1,1],
    [1,0,1],
    [1,1,1]
]
print(main(matrix))