import sys

N,M,B = map(int, sys.stdin.readline().split())

board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

minTime = 1e9
minIdx = 1e9

for h in range(256,-1,-1):
    #추가
    plus = 0
    #제거
    minus = 0
    for i in range(N):
        for j in range(M):
            if board[i][j] < h:
                plus += h - board[i][j]
            else:
                minus += board[i][j] - h
    
    restBlock = minus - plus + B

    if restBlock < 0:
        continue
    
    time = plus + 2 * minus
    if minTime > time:
        minTime = time
        minIdx = h

print(minTime,minIdx)
    

