import sys
from collections import deque

#0 : R  / 1 : D  / 2 : L  / 3 : U
dx = [0,1,0,-1]
dy = [1,0,-1,0]

def BFS():
    global answer
    q = deque()
    q.append((0,Rx,Ry,Bx,By))
    visited.add((Rx,Ry,Bx,By))
    
    while q:
        cnt,x1,y1,x2,y2 = q.popleft()
    
        if cnt > 10:
            break

        for i in range(4):
            rCount,rNx,rNy = move(i,x1,y1)
            bCount,bNx,bNy = move(i,x2,y2)
            #파란구슬이 떨어지는 경우(일단 파란구슬이 떨어지면 무조건 실패)
            if board[bNx][bNy] == 'O':
                continue

            #빨간구슬이 떨어지는 경우
            if board[rNx][rNy] == 'O':
                answer = cnt+1
                return 

            if rCount == 0 and bCount == 0:
                continue

            if rNx == bNx and rNy == bNy:
                if rCount > bCount:
                    rNx -= dx[i]
                    rNy -= dy[i]
                else:
                    bNx -= dx[i]
                    bNy -= dy[i]
            
            if (rNx,rNy,bNx,bNy) not in visited: 
                q.append((cnt+1,rNx,rNy,bNx,bNy))
                visited.add((rNx,rNy,bNx,bNy))
    return

def move(typ,x,y):
    count = 0
    while board[x + dx[typ]][y + dy[typ]]!='#' and board[x][y]!='O':
        x += dx[typ]
        y += dy[typ]
        count += 1

    return count,x,y

def solution(N,M,board):
    global answer
    answer = 0
    BFS()
    if answer == 0:
        return -1
    return answer


N,M = map(int,input().split())
board = []
visited = set()
Rx,Ry,Bx,By = 0,0,0,0


for i in range(N):
    board.append(list(input().split()[0]))

for i in range(len(board)):
    for j in range(len(board[i])):
        if board[i][j] == 'R':
            Rx,Ry = i,j
        elif board[i][j] == 'B':
            Bx,By = i,j


answer = solution(N,M,board)
print(answer)

"""
5 5
#####
#..B#
#.#.#
#RO.#
#####
"""