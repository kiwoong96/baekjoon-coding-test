from collections import deque
import sys
input = sys.stdin.readline

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(x,y,h):
    q = deque()
    #물이 들어갈수 있는 위치
    possible = [[x,y]]
    
    q.append([x,y])
    visited[x][y] = True
    isNo = False
    posWater = 0
    while q:
        x,y = q.popleft()
        for t in range(4):
            nx = x + dx[t]
            ny = y + dy[t]
            if 0<= nx <N and 0<= ny < M and board[nx][ny] != 0:
                if not visited[nx][ny]:
                    if board[nx][ny] < h:
                        visited[nx][ny] = True
                        q.append([nx,ny])
                        possible.append([nx,ny])
            else:
                isNo = True
    
    if isNo:
        pass
    else:
        for x,y in possible:
            board[x][y] += 1
            posWater += 1
    
    return posWater
    
def solution(h):
    rtn = 0
    for x in range(N):
        for y in range(M):
            if board[x][y] and board[x][y] < h and not visited[x][y]:
                rtn += bfs(x,y,h)
    return rtn
    
N,M = map(int,input().split())

board = []
for i in range(N):
    board.append(list(map(int,input().rstrip())))
    
    
result = 0
for h in range(1,10):
    visited = [[False for _ in range(M)] for _ in range(N)]
    result += solution(h)
print(result)

