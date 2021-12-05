import sys

r, c = map(int, sys.stdin.readline().split())
# 지도 입력
board = [list(map(int, input().split())) for _ in range(r)]

#행이 홀수인 경우
if r % 2 == 1:
    print(("R" * (c - 1) + "D" + "L" * (c - 1) + "D") * (r // 2) + "R" * (c - 1))
#열이 홀수인 경우
elif c % 2 == 1:
    print(("D" * (r - 1) + "R" + "U" * (r - 1) + "R") * (c // 2) + "D" * (r - 1))
#행,열이 모두 짝수인 경우
elif r % 2 == 0 and c % 2 == 0:
    minVal = 1e9 
    minPos = [-1, -1] 
    #최솟값 찾기 
    for i in range(r):
        #짝수번째 행
        if i % 2 == 0: 
            #홀수번째 열
            for j in range(1, c, 2):
                if minVal > board[i][j]:
                    minVal = board[i][j]
                    minPos = [i, j]
        #홀수번째 열
        else:
            #짝수번째 행
            for k in range(0, c, 2):
                if minVal > board[i][k]:
                    minVal = board[i][k]
                    minPos = [i, k]

    result = ("D" * (r - 1) + "R" + "U" * (r - 1) + "R") * (minPos[1] // 2)
    x = 2 * (minPos[1] // 2)
    y = 0
    xbound = 2 * (minPos[1] // 2) + 1
    while x != xbound or y != r - 1:
        if x < xbound and [y, xbound] != minPos:
            x += 1
            result += 'R'
        elif x == xbound and [y, xbound - 1] != minPos:
            x -= 1
            result += 'L'
        if y != r - 1:
            y += 1
            result += 'D'

    result += ('R' + 'U' * (r - 1) + 'R' + 'D' * (r - 1)) * ((c - minPos[1] - 1) // 2)
    #result += ('R' + 'U' * (r - 1) + 'R' + 'D' * (r - 1)) * ((c - lowPosition[1] - 1) // 2)

    print(result)