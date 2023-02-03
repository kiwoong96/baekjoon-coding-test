import sys
from collections import deque
from copy import deepcopy
input = sys.stdin.readline

N = int(input())
data = list(map(int,input().rstrip()))
x,y = map(int,input().split())

#print(data)

cnt = 0
stack = deque()
number = ''

#각 노드 순서 지정
for d in data:
    if d == 0:
        cnt += 1
        stack.append(cnt)
        number += str(cnt)
    else:
        top = stack.pop()
        number += str(top)
#print(number)

par = set()
parent = dict()
for n in number:
    if not stack:
        stack.append(n)
        par.add(n)
    elif stack[-1] == n:
        par.remove(n)
        top = stack.pop()
        tmp = deepcopy(par)
        parent[n] = tmp
    else:
        stack.append(n)
        par.add(n)
        
#print(parent)
for i in range(1,N+1):
    parent[str(i)].add(str(i))

#print(parent)
#print(number[x-1],number[y-1])
#print(parent[number[x-1]],parent[number[y-1]])
delNode = max(parent[number[x-1]].intersection(parent[number[y-1]]))

answer = list()
for i in range(len(number)):
    n = number[i]
    if n == delNode:
        answer.append(str(i+1))
    if len(answer) == 2:
        break
print(' '.join(answer))

"""
5
0001011011
((()())())
1233332221
___O__O___
4 7
c b
>> b (2 7) 1 10

4 5
1. 3 3 
((()())())
1233332221
_^____^___ 2 7 

            1         level = 1
      2         8     level = 2
   3  6  7     9  10  level = 3 


썩은사과 : 9 3
((()()())(()()))
1233333322333321
___X_______X____



2. 3 2 (같은 부모)
3. 3 2 (다른 부모)
((()())())
1233332221

4 7 >> c b
level : 2  >> 같은부모
((()())())
1233332221
_^____^___ 2 7

4 9 >> c e 
level : 1  >> 다른부모
((()())())
1233332221
^________^ 1 10








"""
"""
5
0001011011
4 5

5
0001011011
4 9

5
0001011011
2 4


5
0001011011
1 1

5
0001011011
1 2

5
0001011011
2 5

5
000101011011
5 8

5
0001011011
4 7
"""
