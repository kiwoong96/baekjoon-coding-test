import sys

input = sys.stdin.readline

def dfs(x,y,total,depth):
    global answer
    
    #5번 들어오면 max값 비교후 리턴
    if answer > total+maxVal*(3-depth):
        return
    if depth == 3:
        answer = max(answer,total)
        return
    
    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == False:
            if depth == 1:
                visited[nx][ny] = True
                dfs(x,y,total+arr[nx][ny],depth+1)
                visited[nx][ny] = False
            visited[nx][ny] = True
            dfs(nx,ny,total+arr[nx][ny],depth+1)
            visited[nx][ny] = False

def solution():
    global answer
    
    for i in range(N):
        for j in range(M):
            visited[i][j] = True
            dfs(i,j,arr[i][j],0)
            visited[i][j] = False
    print(answer)



N, M = map(int, input().split())
answer = 0
arr = []
maxVal = -1
visited = [[False for _ in range(M)]for _ in range(N)]
for _ in range(N):
    arr.append(list(map(int,input().split())))
maxVal = max(map(max, arr))

dx = [1,-1,0,0]
dy = [0,0,-1,1]

solution()

