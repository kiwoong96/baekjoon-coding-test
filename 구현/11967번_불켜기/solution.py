import sys
from collections import deque
from typing import DefaultDict
input = sys.stdin.readline

N,M = map(int,input().split())
rooms = DefaultDict(list)
visited = [[False for _ in range(N+2)] for _ in range(N+2)]
lights = [[False for _ in range(N+2)] for _ in range(N+2)]
for i in range(M):
    x1,y1,x2,y2 = map(int,input().split())
    rooms[(x1,y1)].append((x2,y2))

dx = [-1,1,0,0]
dy = [0,0,1,-1]
def solution():
    q = deque()
    q.append((1,1))
    visited[1][1] = True
    lights[1][1] = True
    result = 1
    
    while q:
        (x,y) = q.popleft()
        for (nx,ny) in rooms[(x,y)]:
            if not lights[nx][ny]:
                lights[nx][ny] = True
                q.append((nx,ny))
                result +=1  
                for i in range(4):
                    tx,ty = x+dx[i], y+dy[i]
                    if visited[tx][ty] == True or (x,y) == (1,1):
                        visited[x][y] = True
                
         
        for i in range(4):
            tx,ty = x+dx[i], y+dy[i]
            if not visited[tx][ty] and lights[tx][ty]:
                q.append((tx,ty))
                visited[tx][ty] = True
    
    return result


print(solution())


"""
3 6
1 1 1 2
2 1 2 2
1 1 1 3
2 3 3 1
1 3 1 2
1 3 2 1

>>5

4 10
1 1 1 2
1 2 1 3
1 2 4 1
1 3 1 4
1 3 3 1
1 4 2 4
1 4 2 1
2 1 4 4
3 1 4 3
4 1 3 4
"""