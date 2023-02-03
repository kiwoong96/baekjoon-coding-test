import sys
import copy
input = sys.stdin.readline


N, M, C = map(int, input().split())
gemList = list(map(int, input().split()))

dp = [[[0 for k in range(C+1)] for j in range(M+1)] for i in range(1 << 14)]
#i :보석의 상태 (10000000000000)
#j :현재 가방의 순번 (1,2,3 ... N)
#k :현재 가방의 남아있는 용량(0,1,2 ... C)



def solution(gem, bagIdx, capacity) :
    
    # 모든 보석을 사용한 상태 or 가방의 인덱스가 범위 밖
    # 11111111
    if gem == ((1 << N) - 1) or bagIdx >= M :
        return 0

    # 이미 방문한 dp값
    if dp[gem][bagIdx][capacity] != 0 :
        return dp[gem][bagIdx][capacity]

    nowResult = 0

    # 모든 보석을 돌면서 전부 탐색
    for i in range(N) : 

        # 현재 사용하려는 i번째 보석이 이미 사용중 or 남아있는 용량 보다 큰 경우
        if (gem & (1 << i)) != 0 or gemList[i] > C : 
            continue

        # 현재가방 용량에 담을수 있는 경우
        if (capacity >= gemList[i]) :
            tmpGem = copy.deepcopy(gem)
            tmpGem |= (1 << i)  #i번째 상태 1(사용중)
            nowResult = max(nowResult, solution(tmpGem, bagIdx, capacity - gemList[i]) + 1)
        # 현재가방에 넣지 못하는 용량일 경우
        else :
            nowResult = max(nowResult, solution(gem, bagIdx + 1, C))


    dp[gem][bagIdx][capacity] = nowResult
    return nowResult

print(solution(0, 0, C))