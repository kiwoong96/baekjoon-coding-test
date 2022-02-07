import sys
input = sys.stdin.readline

R,C = map(int,input().split())

board = []

for i in range(R):
    board.append(list(map(int,input().rstrip())))

DP1 = [[0 for _ in range(C)] for _ in range(R)] #오른쪽위
DP2 = [[0 for _ in range(C)] for _ in range(R)] #오른쪽아래
DP3 = [[0 for _ in range(C)] for _ in range(R)] #왼쪽위
DP4 = [[0 for _ in range(C)] for _ in range(R)] #왼쪽아래

#DP1 오른쪽 위
for i in range(R):
    for j in range(C-1,-1,-1):
        if (i == 0 or j == C-1) and board[i][j] == 1:
            DP1[i][j] = 1
            continue
        
        if board[i][j] == 1:
            DP1[i][j] = DP1[i-1][j+1] + 1

#DP2 오른쪽 아래
for i in range(R-1,-1,-1):
    for j in range(C-1,-1,-1):
        if (i == R-1 or j == C-1) and board[i][j] == 1:
            DP2[i][j] = 1
            continue
        
        if board[i][j] == 1:
            DP2[i][j] = DP2[i+1][j+1] + 1

#DP3 왼쪽 위
for i in range(R):
    for j in range(C):
        if (i == 0 or j == 0) and board[i][j] == 1:
            DP3[i][j] = 1
            continue
        
        if board[i][j] == 1:
            DP3[i][j] = DP3[i-1][j-1] + 1

#DP4 왼쪽 아래
for i in range(R-1,-1,-1):
    for j in range(C):
        if (i == R-1 or j == 0) and board[i][j] == 1:
            DP4[i][j] = 1
            continue
        
        if board[i][j] == 1:
            DP4[i][j] = DP4[i+1][j-1] + 1

def solution(R,C,board):
    result = 0
    MAX = 0
    for i in range(R):
        for j in range(C):
            maxDP = min(DP1[i][j], DP2[i][j])
            if maxDP < MAX :
                continue
            for k in range(maxDP,0,-1):
                rj = j + (k-1) * 2
                if rj >= C :
                    continue
                if k < MAX:
                    continue
                
                if min(DP3[i][rj], DP4[i][rj]) >= k:
                    MAX = max(MAX,k)
                    break
                    
    return MAX

print(solution(R,C,board))
            
"""
5 5
01100
01011
11111
01111
11111
"""