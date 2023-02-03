import sys
input = sys.stdin.readline

def printBoard():
    for b in board:
        print(b)
    print()
    return 

R,C = map(int,input().split())

board = []

for i in range(R):
    board.append(list(input().rstrip()))

printBoard()

#1. visited
#  - 0 : 미방문
#  - 1 : 이번턴에 방문
#  - 2 : 이번턴 이전에 방문
#2. 녹은 빙판 위치(새로 BFS탐색을 해야 하는 위치) next
#3. 현재 물의 위치.

#logic
# 현재 물의 위치에서 BFS로 방문함. visited가 0인 애들만.
# 만약 얼음을 만났을 경우 next에 담고 종료. 2로 전환
# BFS를 돌다가 얼음이 아닌경우를 만났으면 통로가 생김./






    






