import sys
input = sys.stdin.readline

N = int(input())
board = []

for i in range(N):
    board.append(list(input().rstrip()))

if board[0][0] == '0':
    board[1][1] = ""
else:
    board[1][1] = "*"

if board[0][N-1] == '0':
    board[1][N-2] = ""
else:
    board[1][N-2] = "*"

if board[N-1][0] == '0':
    board[N-2][1]= ""
else:
    board[N-2][1] = "*"

if board[N-1][N-1] == '0':
    board[N-2][N-2] = ""
else:
    board[N-2][N-2] = "*"

dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,1,1,1,0,-1,-1,-1]

#윗줄
i = 0
for j in range(1,N-2):
    if board[i][j] == 0:
        continue
    else:
        cnt = 0
        tmpList = []
        for dt in range(8):
            x = i + dx[dt]
            y = j + dy[dt]
            if x < 0 or x >= N or y < 0 or y >= N:
                continue
            else:
                if board[x][y] == "*":
                    cnt += 1
                elif board[x][y] == '#':
                    tmpList.append((x,y))
        
        if int(board[i][j]) == cnt:
            for tx,ty in tmpList:
                board[tx][ty] = ''
        else:
            if int(board[i][j]) - cnt == len(tmpList):
               for tx,ty in tmpList:
                   board[tx][ty] = '*'


#아랫줄
i = N-1
for j in range(1,N-2):
    if board[i][j] == 0:
        continue
    else:
        cnt = 0
        tmpList = []
        for dt in range(8):
            x = i + dx[dt]
            y = j + dy[dt]
            if x < 0 or x >= N or y < 0 or y >= N:
                continue
            else:
                if board[x][y] == "*":
                    cnt += 1
                elif board[x][y] == '#':
                    tmpList.append((x,y))
        
        if int(board[i][j]) == cnt:
            for tx,ty in tmpList:
                board[tx][ty] = ''
        else:
            if int(board[i][j]) - cnt == len(tmpList):
               for tx,ty in tmpList:
                   board[tx][ty] = '*'


 

#왼쪽
j = 0
for i in range(1,N-2):
    if board[i][j] == 0:
        continue
    else:
        cnt = 0
        tmpList = []
        for dt in range(8):
            x = i + dx[dt]
            y = j + dy[dt]
            if x < 0 or x >= N or y < 0 or y >= N:
                continue
            else:
                if board[x][y] == "*":
                    cnt += 1
                elif board[x][y] == '#':
                    tmpList.append((x,y))
        
        if int(board[i][j]) == cnt:
            for tx,ty in tmpList:
                board[tx][ty] = ''
        else:
            if int(board[i][j]) - cnt == len(tmpList):
               for tx,ty in tmpList:
                   board[tx][ty] = '*'

#오른쪽
j = N-1
for i in range(1,N-2):
    if board[i][j] == 0:
        continue
    else:
        cnt = 0
        tmpList = []
        for dt in range(8):
            x = i + dx[dt]
            y = j + dy[dt]
            if x < 0 or x >= N or y < 0 or y >= N:
                continue
            else:
                if board[x][y] == "*":
                    cnt += 1
                elif board[x][y] == '#':
                    tmpList.append((x,y))
        
        if int(board[i][j]) == cnt:
            for tx,ty in tmpList:
                board[tx][ty] = ''
        else:
            if int(board[i][j]) - cnt == len(tmpList):
               for tx,ty in tmpList:
                   board[tx][ty] = '*'


"""
for b in board:
    print(b)
"""
 
result = 0

for i in range(N):
    for j in range(N):
        if board[i][j] == '*' or board[i][j] == '#':
            result += 1

print(result)