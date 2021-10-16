import sys
input = sys.stdin.readline
import copy
dx = [1,-1,0,0]
dy = [0,0,1,-1]
directions = [[]
            ,[[0],[1],[2],[3]]
            ,[[0,1],[2,3]]
            ,[[0,2],[2,1],[1,3],[3,0]]
            ,[[0,1,2],[1,2,3],[0,1,3],[0,2,3]]
            ,[[0,1,2,3]]]


def dfs(board,idx,sumation):
    global CCTV
    global answer
    tmpBoard = [board[i][:] for i in range(len(board))]

    if idx == cctvCnt:
        answer = min(N*M-cctvWallCnt-sumation,answer)
        return
    
    x,y,num = CCTV[idx]
    
    for direction in directions[num]:
        tmpBoard = [board[i][:] for i in range(len(board))]
        tmpSumation = sumation

        for d in direction:
            nx,ny = x,y
            while True:
                nx += dx[d]
                ny += dy[d]
                if 0<=nx<N and 0<=ny<M and tmpBoard[nx][ny] != 6:
                    if tmpBoard[nx][ny] == 0:
                        tmpBoard[nx][ny] = '#'
                        tmpSumation+= 1
                else:
                    break

        dfs(tmpBoard,idx+1,tmpSumation)
            
            

def solution():

    dfs(board,0,0)
    return


N,M = map(int,input().split())
board = []
CCTV = []
for i in range(N):
    board.append(list(map(int,input().split())))

cctvCnt = 0
cctvWallCnt = 0
answer = sys.maxsize
for i in range(N):
    for j in range(M):
        if board[i][j] != 0 and board[i][j] != 6:
            CCTV.append((i,j,board[i][j]))
            cctvCnt += 1
        if board[i][j] !=0:
            cctvWallCnt += 1
solution()
print(answer)
