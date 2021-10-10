import sys
input = sys.stdin.readline

"""
dxy = [
    [[0,0],[1,0],[2,0],[2,1]],
    [[0,0],[1,0],[2,0],[2,-1]],
    [[0,0],[0,-1],[1,-1],[2,-1]],
    [[0,0],[0,1],[1,1],[2,1]],
    [[0,0],[1,0],[1,1],[1,2]],
    [[0,0],[1,0],[1,-1],[1,-2]],
    [[0,0],[-1,0],[-1,-1],[-1,-2]],
    [[0,0],[-1,0],[-1,1],[-1,2]],
    [[0,0],[1,0],[1,1],[2,1]],
    [[0,0],[1,0],[1,-1],[2,-1]],
    [[0,0],[0,1],[1,1],[1,2]],
    [[0,0],[0,1],[-1,1],[-1,2]],
    [[0,0],[1,0],[2,0],[1,1]],
    [[0,0],[1,0],[2,0],[1,-1]],
    [[0,0],[0,1],[0,2],[1,1]],
    [[0,0],[0,1],[0,2],[-1,1]],
    [[0,0],[0,1],[1,0],[1,1]],
    [[0,0],[1,0],[2,0],[3,0]],
    [[0,0],[0,1],[0,2],[0,3]]]


def find(x,y):

    max_value = -1
    for k in dxy:
        result = 0
        for z in k:
            try:
                now_x = x+z[0]
                now_y = y+z[1]
                result += board[now_x][now_y]
            except:
                result = 0
                continue
        if max_value < result:
            max_value = result

    return max_value


result = -1

for i in range(N):
    for j in range(M):
        tmp = find(i,j)
        if result < tmp:
            result = tmp

print(result)
"""

"""
N, M = map(int,input().split())

board = []

for i in range(N):
    board.append(list(map(int,input().split())))

visited = [[0 for _ in range(M)]for _ in range(N)]

dx = [0,1,0,-1]
dy = [1,0,-1,0]

ans = 0

def dfs(x,y,idx,total):
    global ans
    if idx == 3:
        ans = max(ans,total)
        return
    
    for i in range(4):
        nx, ny = x+dx[i] , y+dy[i]
        if 0<=nx<=N and 0<=ny<=M and visited[nx][ny]==0:
            if idx==1:
                visited[nx][ny] = 1
                dfs(x,y,idx+1,total+board[x][y])
                visited[nx][ny] = 0
            visited[nx][ny] = 1
            dfs(nx,ny,idx+1,total+board[nx][ny])
            visited[nx][ny] = 0

print(ans)

"""
