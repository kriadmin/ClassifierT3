import numpy as np
from pprint import pprint

a = np.array([ [1,2,3], [4,5,6], [7,8,9]])
def all_eight(m):
    return [m,np.rot90(m),np.rot90(m,2),np.rot90(m,3), np.flipud(m), np.fliplr(m), m.T, np.rot90(m,2).T]

classes = []

i = 0
# while(i < 10000):
#     x = np.random.randint(-1,high=2,size=(3,3))
#     b = set(str(x) for x in all_eight(x))
#     if b not in classes:
#         classes.append(b)
#     i+=1
axes = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
def isWin(board):
    return any("".join(board[p] for p in axis) in ["XXX","OOO"] for axis in axes)

def validBoards(board="."*9,player=None,states=None):
    if player == None:
        result  = {board}  # count the empty board
        result |= validBoards(board,player="X",states=set()) # X goes 1st
        #result |= validBoards(board,player="O",states=set()) # O goes 1st
        return result
    opponent = "XO"[player=="X"]
    for pos,cell in enumerate(board):
        if cell != ".": continue
        played = board[:pos]+player+board[pos+1:] # simulate move
        if played in states : continue            # skip duplicate states
        states.add(played)                        # return the new state
        if isWin(played): continue                # stop game upon winning 
        validBoards(played,opponent,states)       # add subsequent moves 
    return states
dic = {'X':-1 , 'O':1 , '.':0}
S = [ np.array([dic[y] for y in x]).reshape((3,3)) for x in  validBoards()]
x = S[0]


np.array(list(map(int, str(x).replace('[','').replace(']','').replace('\n',' ').split())) ).reshape((3,3))

states = []

for s in S:
    b = set([' '.join(map(str,x.flatten())) for x in all_eight(s)])
    f = False
    for c in classes:
        if len(c.intersection(b)) != 0:
            f = True
            break
    if not f:
        classes.append(b)
        states.append(s)

pprint(classes[0])    

# with open("classes.txt","w") as f:
#     for c in classes:
#         f.write(",\n".join(c) + "\nt\n")

print(len(classes))