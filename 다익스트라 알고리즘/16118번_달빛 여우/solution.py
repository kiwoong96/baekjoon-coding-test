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
    graph[start].append((end,dist))
    graph[end].append((start,dist))

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
    heapq.heappush(hq,(0,start,0))
    #[NodeNo][0] : 다음번이 속도 빠르게
    #[NodeNo][1] : 다음번이 속도 느리게
    distanceB[start][0] = 0
    
    while hq:
        curDist , cur , flag = heapq.heappop(hq)
        if curDist > distanceB[cur][flag]:
            continue
            
        for nextNode, dist in graph[cur]:
            if flag == 0:
                nextDist = curDist + dist / 2
            else:
                nextDist = curDist + dist * 2

            if  nextDist < distanceB[nextNode][~flag]:
                distanceB[nextNode][~flag] = nextDist
                heapq.heappush(hq,(nextDist,nextNode,~flag))


dijkstraA(1)
dijkstraB(1)

result = 0 

for i in range(1,N+1):
    if distanceA[i] < min(distanceB[i]):
        result += 1

print(result)


"""
5 6
1 2 3
1 3 2
2 3 2
2 4 4
3 5 4
4 5 3
"""