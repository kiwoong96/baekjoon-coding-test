import sys
input = sys.stdin.readline

#input
N = int(input())
arr = []
for i in range(N):
    arr.append(list(map(int,input().rstrip())))
    
def solution(N,arr):
    return DFS(0,1,0) + 1

def DFS(cur,visited,price):
    #이게 없으면 DFS
    if DP[cur][visited][price] != 0:
        return DP[cur][visited][price]
    
    #거쳐온 사람 수?
    cnt = 0
    
    for per in range(1,N):
        # 본인에게 판매 불가
        if per == cur:
            continue
        # 다음 판매액이 더 작거나 / 이미 구매한 사람의 경우 -> 판매 불가
        if arr[cur][per] < price or visited & (1<<per) > 0:  
            continue
        
        # 현재 방문 찍고 다음 방문
        cnt = max(cnt, 1+DFS(per,visited|(1<<per),arr[cur][per]))
        
    DP[cur][visited][price] = cnt
    
    return cnt #0(1번사람) 00000...1(1번사람만 구매) 0원
    
#DP[현재 사람 번호(cur)][방문 기록(visited)][가격(price)]
DP = [[[0 for _ in range(10)]for _ in range(1 << N)]for _ in range(N)]
print(solution(N,arr))


    