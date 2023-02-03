from collections import deque
import sys

input = sys.stdin.readline

while True:
    #0번째값 : n / 1번째부터 height
    data = list(map(int,input().split()))
    n = data.pop(0)
    #data = data[1:]

    if n == 0:
        break
    
    stack = deque()
    answer = 0
    
    for i in range(n):
        #스택이 비어있지않고, 높이가 감소하는 경우(최대넓이 계산)
        while len(stack) != 0 and data[stack[-1]] > data[i]:
            tmp = stack.pop()
            
            #마지막 값인 경우(이전 증가위치가 X)
            if len(stack) == 0:
                width = i
            else:
                width = i - stack[-1] - 1
            answer = max(answer, width * data[tmp])

        #스택이 비어있거나, 높이가 증가하는경우(삽입)
        stack.append(i)

    #나머지 각 증가위치~끝까지 minHeight로 계산한 값들
    while len(stack) != 0:
        tmp = stack.pop()
        
        #마지막 값인 경우(이전 증가위치 X)
        if len(stack) == 0:
            width = n
        else:
            width = n - stack[-1] - 1 
        answer = max(answer,width * data[tmp])

    print(answer)
    
"""
7 2 1 4 5 1 3 3
4 1000 1000 1000 1000
0
"""
            
    