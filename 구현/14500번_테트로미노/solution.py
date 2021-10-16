
"""
import sys; input = sys.stdin.readline

def dfs(r, c, count, sumation):
    global answer
    
    #시간 줄이기(없어도 동작가능)
    if answer >= sumation + maxVal * (3 - count):
        return
    
    if count == 3:
        answer = max(answer, sumation)
        return
    else:
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < M and visit[nr][nc] == 0:
                #현재 상태를 한번 더탐(테트리스 모형중 특이한 모형)
                if count == 1:
                    visit[nr][nc] = 1
                    dfs(r, c, count + 1, sumation + arr[nr][nc])
                    visit[nr][nc] = 0
                visit[nr][nc] = 1
                dfs(nr, nc, count + 1, sumation + arr[nr][nc])
                visit[nr][nc] = 0

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visit = [([0] * M) for _ in range(N)]


dr = [-1, 0, 1, 0] 
dc = [0, 1, 0, -1]
answer = 0

#arr중 가장 큰 값
maxVal = max(map(max, arr))

#DFS
for r in range(N):
    for c in range(M):
        visit[r][c] = 1
        dfs(r, c, 0, arr[r][c])
        visit[r][c] = 0

print(answer)
"""


import sys
input = sys.stdin.readline

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def dfs(x,y,count,total):
    global answer
    
    if answer > total+maxVal*(3-count):
        return
    if count == 3:
        answer = max(answer,total)
        return

    for i in range(4):
        nx,ny = x+dx[i], y+dy[i]
        if 0<=nx<N and 0<=ny<M and visited[nx][ny] == False:
            if count == 1:
                visited[nx][ny] = True
                dfs(x,y,count+1,total+board[nx][ny])
                visited[nx][ny] = False
            visited[nx][ny] = True
            dfs(nx,ny,count+1,total+board[nx][ny])
            visited[nx][ny] = False
    return

def solution(N,M,board,visited):
    global answer

    for i in range(N):
        for j in range(M):
            visited[i][j] = True
            dfs(i,j,0,board[i][j])
            visited[i][j] = False
    
    return answer

N, M = map(int,input().split())
board = []
answer = 0

for i in range(N):
    board.append(list(map(int,input().split())))
visited = [[False for _ in range(M)] for _ in range(N)]

maxVal = max(map(max, board))

solution(N,M,board,visited)
print(answer)