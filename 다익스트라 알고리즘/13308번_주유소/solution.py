import heapq
import sys
input = sys.stdin.readline

def dijkstra(N,M,price,result,graph):
    hq = []
    
    #총 비용, 현재까지 가장 적은 주유비, 현재 노드
    heapq.heappush(hq, (0,price[1],1))

    while hq:
        curCost, curMinOil, curNode = heapq.heappop(hq)
        if curNode == N:
            return curCost
        if result[curNode][curMinOil] < curCost:
            continue
        for nextNode,distance in graph[curNode]:
            nextCost = curCost+distance*curMinOil
            nextMinOil = min(curMinOil,price[nextNode])
            if nextCost < result[nextNode][nextMinOil]:
                heapq.heappush(hq, (nextCost,nextMinOil,nextNode))
                result[nextNode][nextMinOil] = nextCost
        
    return

def solution(N,M,price,result,graph):
    res= dijkstra(N,M,price,result,graph)
    return res

N,M = map(int,input().split())
graph = [[]for _ in range(N+1)]
result = [[1e9 for _ in range(2501)]for _ in range(N+1)]
price = list(map(int,input().split()))
price.insert(0,0)
for i in range(M):
    start, end, distance = map(int,input().split())
    graph[start].append((end,distance))
    graph[end].append((start,distance))

answer = solution(N,M,price,result,graph)
print(answer)


"""
4 4
5 2 4 1
3 1 3
1 2 2
4 3 4
2 4 15

4 3
5 2 5 2
1 2 2
2 3 3
3 4 1

"""