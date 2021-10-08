import sys
input = sys.stdin.readline
import heapq
INF = sys.maxsize

def solution(start):
    hq = []
    heapq.heappush(hq, (0,start,0))
    distance[start][0] = 0
    
    while hq:
        dist, cur, cnt = heapq.heappop(hq)
        

        if dist > distance[cur][cnt]:
            continue
        
        for nextNode, cost in graph[cur]:
            nextDist = dist + cost
            if nextDist < distance[nextNode][cnt]:
                heapq.heappush(hq,(nextDist,nextNode, cnt))
                distance[nextNode][cnt] = nextDist

            if cnt < K and dist < distance[nextNode][cnt+1]:
                heapq.heappush(hq,(dist,nextNode,cnt+1))
                distance[nextNode][cnt+1] = dist



N,M,K = map(int,input().split())
graph = [[]for _ in range(N+1)]
distance = [[INF for _ in range(21)] for _ in range(N+1)]

for i in range(M):
    start,end,dist = map(int,input().split())
    graph[start].append((end,dist))
    graph[end].append((start,dist))

solution(1)

print(min(distance[N]))

"""
4 4 1
1 2 10
2 4 10
1 3 1
3 4 100
"""