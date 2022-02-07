import sys
input = sys.stdin.readline

N = int(input())
board = []

wood = []
target = []

for i in range(N):
    tmpList = list(input().rstrip())
    for j in range(len(tmpList)):
        if tmpList[j] == 'B':
            wood.append([i,j])
        elif tmpList[j] == 'E':
            target.append([i,j])
    board.append(tmpList)
"""
for b in board:
    print(b)
    
print(wood)
print(target)
"""

    



"""
5
B0011
B0000
B0000
11000
EEE00
"""