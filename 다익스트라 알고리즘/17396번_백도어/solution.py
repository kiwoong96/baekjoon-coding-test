import sys
import heapq
input = sys.stdin.readline

def dijkstra(N,M,sight,dist,graph):
    hq = []
    
    #cost, cur
    heapq.heappush(hq,(0,0))
    dist[0] = 0

    while hq:
        cost, cur = heapq.heappop(hq)
        
        if cur == N-1:
            return cost

        if cost > dist[cur]:
            continue

        for nextNode, distance in graph[cur]:
            nextCost = cost+distance
            if nextCost < dist[nextNode] and sight[nextNode] == 0:
                heapq.heappush(hq,(nextCost,nextNode))
                dist[nextNode] = nextCost
        
    return -1

def solution(N,M,sight,dist,graph):
    ans = dijkstra(N,M,sight,dist,graph)
    return ans

N,M = map(int,input().split())
sight = list(map(int,input().split()))
dist = [sys.maxsize for _ in range(N)]
graph = [[] for _ in range(N)]
sight[-1] = 0

for i in range(M):
    start,end,distance = list(map(int,input().split()))
    graph[start].append((end,distance))
    graph[end].append((start,distance))

result = solution(N,M,sight,dist,graph)
print(result)

"""
5 7
0 0 0 1 1
0 1 7
0 2 2
1 2 4
1 3 3
1 4 6
2 3 2
3 4 1
"""