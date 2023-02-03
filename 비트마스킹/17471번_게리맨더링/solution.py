import sys
from itertools import combinations
from collections import deque
input = sys.stdin.readline

N = int(input())
volume = list(map(int,input().split()))
volume.insert(0,0)
edge = [[] for _ in range(N+1)]
for i in range(N):
    data = list(map(int,input().split()))
    start = i+1
    for j in range(1,len(data)):
        end = data[j]
        edge[start].append(end)

for e in edge:
    print(e)  

def bfs(c):
    #시작점
    start = c[0]
    
    q = deque()
    q.append(start)
    
    total = 0
    visited = 0
    visited |= (1 << (start-1))
    while q:
        now = q.popleft()
        total += volume[now]
        for vertex in edge[now]:
            if vertex in c and visited & (1 << (vertex-1)) == 0:
                q.append(vertex)
                visited |= (1 << (vertex-1))
    
    return total,visited
                
    
for i in range(1,N//2+1):
    comb = list(combinations(range(1,N+1),i))
    for c in comb:
        volume1, visited1 = bfs(c)
        volume2, visited2 = bfs([i for i in range(1,N+1) if i not in c])
        #print("c : ", c)
        #print("not in c : ", [i for i in range(1,N+1) if i not in c])
        #print(volume1, visited1,c) 
        #print(volume2, visited2,[i for i in range(1,N+1) if i not in c]) 
        #print("visited1 & visited2 : " , visited1 | visited2)
        #print( (1<<N)-1) 
        if visited1 | visited2 == (1<<N) -1:
            print ("TRUE : ", c,[i for i in range(1,N+1) if i not in c],volume1, volume2)
            
""" -
6
1 1 1 1 1 1
2 2 4
4 1 3 6 5
2 4 2
2 1 3
1 2
1 2
"""
    
    

    

    