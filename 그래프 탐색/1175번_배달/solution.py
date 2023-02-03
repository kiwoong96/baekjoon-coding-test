from collections import deque
import sys
input = sys.stdin.readline

N,M = map(int,input().split())
arr = []

sX,sY = 0,0
#visited [x][y][cCount][dir]
visited = [[[[False for _ in range(4)] for _ in range(4)] for _ in range(50)] for _ in range(50)]
cPos = dict()

tmpCount = 1
for i in range(N):
    tmp = list(input().rstrip())
    for j in range(len(tmp)):
        if tmp[j] == 'S':
            sX,sY = i,j
        elif tmp[j] == 'C':
            cPos[(i,j)] = tmpCount
            tmpCount += 1
    arr.append(tmp)

dx = [-1,1,0,0]
dy = [0,0,-1,1]

#print(cPos)

def solution():
    result = -1
    
    #x,y,cCount,dir,cnt
    q = deque()
    q.append((sX,sY,0,-1,0))
    
    
    while q:
        #print(q)
        x,y,cCount,direction,cnt = q.popleft()
        
        if cCount == 3:
            result = cnt
            break
        for i in range(4):
            
            #전진행방향 = 현진행방향
            if i == direction:
                continue
            #print(x,y,dx[i],dy[i])
            
            nx, ny = x+dx[i], y+dy[i]
            #print("nx : " ,nx ,"  ny : ", ny)
            if 0<=nx<N and 0<=ny<M:
                if arr[nx][ny] != '#':
                    if arr[nx][ny] == 'C' and visited[nx][ny][cCount+1][i] == False:
                        #내가 지금까지 방문한 C가 없는경우
                        if cCount == 0:
                            q.append((nx,ny,cPos[(nx,ny)],i,cnt+1))
                        #이미 방문한 C인 경우
                        elif cCount == cPos[(nx,ny)]:
                            q.append((nx,ny,cCount,i,cnt+1))
                        #방문하지 않은 C인 경우
                        else:
                            q.append((nx,ny,cCount | cPos[(nx,ny)],i,cnt+1))
                        visited[nx][ny][cCount+1][i] = True
                    elif arr[nx][ny] != 'C' and visited[nx][ny][cCount][i] == False:
                        q.append((nx,ny,cCount,i,cnt+1))
                        visited[nx][ny][cCount][i] = True
                  
    
    
    return result

print(solution())


#2169_로봇조종하기

