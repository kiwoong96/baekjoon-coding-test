import sys
from collections import deque

#클러스 체크
def get_cluster():
    q = deque()
    res = dict()
    
    cnt = 1     #클러스터 번호
    
    #모든 칸을 방문하여 클러스터확인(BFS)
    for i in range(n):
        for j in range(m):
            if check[i][j] == -1:
                if arr[i][j] == 'x':
                    q.append((i, j))
                    check[i][j] = cnt
                    
                    #BFS
                    while q:
                        x, y = q.popleft()
                        for k in range(4):
                            nx, ny = x + dx[k], y + dy[k]
                            if 0 <= nx < n and 0 <= ny < m:
                                if check[nx][ny] == -1:
                                    if arr[nx][ny] == 'x':
                                        q.append((nx, ny))
                                        check[nx][ny] = check[x][y]

                    cnt += 1
                    
    #각 클러스터 좌표 저장
    for i in range(n):
        for j in range(m):
            if check[i][j] != -1:
                if check[i][j] in res:
                    res[check[i][j]].append((i,j))          #res[1] = [(1,1),(1,2)]
                else:
                    res[check[i][j]] = [(i, j)]
    return res

#클러스터 하강
def down(d):
    #하강할 거리(각 클러스터 기준 최솟값)
    dist = [9876543210] * (max(d.keys()) + 1)
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 'x':
                #방향은 위로 진행(아래로진행하는 경우보다 효율적..?)
                x, y = i - 1, j
                cnt = 1
                meet = False
                while 0 <= x < n:
                    if arr[x][y] == 'x':
                        meet = True
                        break
                    else:
                        x -= 1
                        cnt += 1
                        
                #다른 클러스터를 만났을 경우에만 하강할 거리 갱신
                if meet:
                    if check[x][y] != check[i][j]:
                        dist[check[x][y]] = min(dist[check[x][y]], cnt)

    for i in d:
        d[i].sort(reverse = True)                               
        
        # 클러스터의 가장 밑에 있는 미네랄의 x좌표가 바닥이라면 continue      
        if d[i][0][0] == n - 1:
            continue
        
        for j in d[i]:
            x, y = j
            
            dist[check[x][y]] = min(dist[check[x][y]], n - x)
            if dist[check[x][y]] != 9876543210:
                arr[x][y] = '.'
                arr[x + dist[check[x][y]] - 1][y] = 'x'

#창던지는 함수
def throw(x, s):
    if s % 2 == 0:
        for i in range(m):
            if arr[x][i] == 'x':
                arr[x][i] = '.'
                break
    else:
        for i in range(m - 1, -1, -1):
            if arr[x][i] == 'x':
                arr[x][i] = '.'
                break

# 입력
n, m = map(int, sys.stdin.readline().split())
arr = [list(sys.stdin.readline().rstrip()) for _ in range(n)]
dx = [0,1,0,-1]
dy = [1,0,-1,0]
size = int(sys.stdin.readline())
info = list(map(int, sys.stdin.readline().split()))


for i in range(size):
    check = [[-1] * m for _ in range(n)]
    throw(n - info[i], i)
    temp = get_cluster()
    down(temp)
    
for i in arr:
    print(''.join(i))