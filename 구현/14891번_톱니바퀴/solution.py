import sys
from typing import Collection
input = sys.stdin.readline

def dfs(clockNum,dir):
    global point
    global visited
    visited[clockNum] = True
    
    #현재 바퀴의 left와 왼쪽 바퀴의 오른쪽 비교(다른경우)
    if clockNum != 0 and data[clockNum][point[clockNum][0]] != data[clockNum-1][point[clockNum-1][1]] and visited[clockNum-1] == False:
        visited[clockNum-1] = True
        if dir == 1:
            dfs(clockNum-1,-1)
        elif dir == -1:
            dfs(clockNum-1,1)
        visited[clockNum-1] = False
    
    
    if clockNum != 3 and data[clockNum][point[clockNum][1]] != data[clockNum+1][point[clockNum+1][0]] and visited[clockNum+1] == False :
        visited[clockNum+1] = True
        if dir == 1:
            dfs(clockNum+1,-1)
        elif dir == -1:
            dfs(clockNum+1,1)
        visited[clockNum+1] = False
    
    visited[clockNum] = False

    if dir == 1:
        point[clockNum][0] = (point[clockNum][0]-1)%8
        point[clockNum][1] = (point[clockNum][1]-1)%8
    else:
        point[clockNum][0] = (point[clockNum][0]+1)%8
        point[clockNum][1] = (point[clockNum][1]+1)%8
    
    return

def solution(order):
    for clockNum, dir in order:
        dfs(clockNum-1,dir)
    return


topni = [input().split() for _ in range(4)]
data = [[0 for _ in range(8)]for _ in range(4)]
#left,right
point = [[6,2] for _ in range(4)]
visited = [False for _ in range(4)]
for i in range(4):
    for j in range(8):
        data[i][j] = topni[i][0][j]

K = int(input())
order = []
for i in range(K):
    order.append(list(map(int,input().split())))

solution(order)
answer = 0

for i in range(4): 
    answer += int(data[i][(point[i][0]+2)%8])* pow(2,i)

print(answer)


"""
10101111
01111101
11001110
00000010
2
3 -1
1 1


data= []
for i in range(4):
    data.append(input().split())[0]

for d in data:
    print(d)
print()

print(data[0][1])
"""