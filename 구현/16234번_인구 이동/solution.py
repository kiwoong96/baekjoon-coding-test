import sys
from collections import deque

dx = [0,0,-1,1]
dy = [1,-1,0,0]

def BFS(visited,i,j):
    global team
    
    visited[i][j] = True
    q = deque()
    q.append([i,j])
    rtn = board[i][j]
    
    while q:
        i, j = q.popleft()
        team.append([i,j])
        for k in range(4):
            ni,nj = i+dx[k], j+dy[k]
            if not (0<= ni < N and 0<= nj < N):
                continue
            
            if not visited[ni][nj]:
                if L <= abs(board[i][j] - board[ni][nj]) <= R:
                    q.append([ni,nj])
                    visited[ni][nj] = True
                    rtn += board[ni][nj]
    
    if rtn == board[i][j]:
        rtn = 0
        team.popleft()
        
    return rtn

def solution():
    count = 0
    
    while True:
        totalCount = 0
        
        visited = [[False for _ in range(N)]for _ in range(N)]
        sumation = 0
        
        for i in range(N):
            for j in range(N):
                sumation = 0
                if not visited[i][j]:
                    sumation += BFS(visited,i,j)
                
                if sumation == 0:
                    continue
                else:
                    #print(team)
                    totalCount += 1
                    newVal = sumation//len(team)
                    
                    while team:
                        x, y = team.popleft()
                        board[x][y] = newVal
        if totalCount == 0:
            break
        count += 1
    return count
    
team = deque()
input = sys.stdin.readline
N,L,R = map(int,input().split())
board = []
for i in range(N):
    board.append(list(map(int,input().split())))

print(solution())
