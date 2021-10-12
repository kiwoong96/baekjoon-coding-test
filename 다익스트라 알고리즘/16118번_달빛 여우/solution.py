import sys
input = sys.stdin.readline
import heapq
INF = sys.maxsize


N, M = map(int,input().split())
distanceA = [ INF for _ in range(N+1)]
distanceB = [ [INF for _ in range(2)] for _ in range(N+1)]
graph = [[]for _ in range(N+1)]

for i in range(M):
    start,end,dist = list(map(int,input().split()))
    graph[start].append((end,dist*2))
    graph[end].append((start,dist*2))

def dijkstraA(start):
    hq = []
    heapq.heappush(hq,(0,start))
    distanceA[start] = 0
    
    while hq:
        curDist , cur = heapq.heappop(hq)
        if curDist > distanceA[cur]:
            continue
            
        for nextNode, dist in graph[cur]:
            nextDist = curDist + dist
            if  nextDist < distanceA[nextNode]:
                distanceA[nextNode] = nextDist
                heapq.heappush(hq,(nextDist,nextNode))

def dijkstraB(start):
    hq = []
    heapq.heappush(hq,(0,start,False))
    #False -> 느리게 도착!
    #[NodeNo][0] : 다음번이 속도 빠르게
    #[NodeNo][1] : 다음번이 속도 느리게
    distanceB[start][0] = 0
    
    while hq:
        curDist , cur , flag = heapq.heappop(hq)
        #느리게 도착한경우 다음 빠르게
        if not flag and curDist > distanceB[cur][0]:
            continue
        #빠르게 도착한경우 다음 느리게
        elif flag and curDist > distanceB[cur][1]:
            continue

        for nextNode, dist in graph[cur]:
            if not flag:
                nextDist = curDist + dist // 2
                if nextDist < distanceB[nextNode][1]:
                    distanceB[nextNode][1] = nextDist
                    heapq.heappush(hq,(nextDist,nextNode,True))

            else:
                nextDist = curDist + dist * 2
                if  nextDist < distanceB[nextNode][0]:
                    distanceB[nextNode][0] = nextDist
                    heapq.heappush(hq,(nextDist,nextNode,False))


dijkstraA(1)
dijkstraB(1)

result = 0 

for i in range(1,N+1):
    if distanceA[i] < min(distanceB[i]):
        result += 1

print(result)
"""

"""

"""
5 6
1 2 3
1 3 2
2 3 2
2 4 4
3 5 4
4 5 3
"""

import sys; read = sys.stdin.readline
import math; INF = math.inf
from heapq import heappush, heappop

def fox(graph):
    s = 1
    distance = [INF] * (V+1)
    distance[s] = 0
    
    queue = []
    heappush(queue, (0, s))
    while queue:
        d, u = heappop(queue)
        if distance[u] < d:
            continue
            
        for v, w in graph[u].items():
            d_new = d + w
            if distance[v] > d_new:
                distance[v] = d_new
                heappush(queue, (d_new, v))
    return distance

def wolf(graph):
    s = 1
    distance = [[INF] * 2 for _ in range(V+1)]
    distance[s][1] = 0
    
    queue = []
    heappush(queue, (0, s, True))
    while queue:
        d, u, run = heappop(queue)
        if distance[u][run] < d: 
            continue
            
        for v, w in graph[u].items():
            if run:
                d_new = d + w // 2
            else:
                d_new = d + w * 2
            
            if distance[v][not run] > d_new:
                distance[v][not run] = d_new
                heappush(queue, (d_new, v, not run))
    return [min(d) for d in distance]

if __name__ == "__main__":
    V, E = map(int, read().split())
    graph = [dict() for _ in range(V+1)]
    for _ in range(E):
        u, v, w = map(int, read().split())
        graph[u][v] = w * 2
        graph[v][u] = w * 2
        
    distance_fox = fox(graph)
    distance_wolf = wolf(graph)
    
    cnt = 0
    for f, w in zip(distance_fox, distance_wolf):
        if f < w:
            cnt += 1
    print(cnt)
        