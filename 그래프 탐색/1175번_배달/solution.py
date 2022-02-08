from collections import deque
import sys
from this import d
input = sys.stdin.readline

N,M = map(int,input().split())
arr = []

sI,sJ = 0,0

for i in range(N):
    tmp = list(input().rstrip())
    for j in tmp:
        if j == 'S':
            sI,sJ = i,j
    
dx = [-1,1,0,0]
dy = [0,0,-1,1]
# 방향 dir 위(0), 오른쪽(1), 아래(2), 왼쪽(3)

def solution():
    q = deque()
    q.append((sI,sJ))
    
    
    
    
    
    return



