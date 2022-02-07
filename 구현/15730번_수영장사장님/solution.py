import sys
from collections import deque
input = sys.stdin.readline

dx = [0,0,-1,1]
dy = [1,-1,0,0]

N,M = map(int,input().split())
board = []
for i in range(N):
    board.append(list(map(int,input().split())))

def solution(h):
    rtn = 0
    for x in range(N):
        for y in range(M):
            if board[x][y] and board[x][y] < h and not visited[x][y]:
                rtn += bfs(x,y,h)
    #print("h : ", h  , " rtn : " , rtn)
    return rtn

def bfs(x,y,h):
    q = deque()
    q.append((x,y))
    visited[x][y] = True
    possible = [(x,y)]
    isNo = False
    posWater = 0
    
    while q:
        x,y = q.popleft()
        for t in range(4):
            nx = x + dx[t]
            ny = y + dy[t]
            if 0<= nx < N and 0<= ny < M and board[nx][ny] != 0:
                if not visited[nx][ny]:
                    if board[nx][ny] < h:
                        visited[nx][ny] = True
                        q.append((nx,ny))
                        possible.append((nx,ny))
            else:
                isNo = True
        
    if isNo:
        pass
    else:
        #print(x,y)
        for x,y in possible:
            board[x][y] += 1
            posWater += 1
    
    return posWater
    
    
result = 0
for h in range(10):
    visited = [[False for _ in range(M)]for _ in range(N)]
    result += solution(h)
print(result)


# 101 * 101 * 10,000
# 102,010,000 ~ 200,000,000

"""
4 5
4 5 3 4 2
3 2 5 2 5
4 1 2 3 1
1 3 3 2 3
"""