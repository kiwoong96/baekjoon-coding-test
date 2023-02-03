from operator import truediv
import sys
#from collections import defaultdict
input = sys.stdin.readline

N, M = map(int,input().split())

meetings = []

for _ in range(M):
    meetings.insert(0,list(map(int,input().split())))

result = list(map(int,input().split()))
result.insert(0,0)

maybe = set()
never = set()

def solution():
    for meeting in meetings:
        flag = True
        target = result[meeting[1]]
        for i in range(2,len(meeting)):
            member = meeting[i]
            #모든값이 같은 경우
            if result[member] == target:
                continue
            #하나라도 다른값이 있는경우
            flag = False
            break
        
        #모든값이 같은경우
        if flag:
            #모두 감염
            if target == 1:
                for member in meeting:
                    maybe.add(member)
            #모두 비감염
            else:
                for member in meeting:
                    never.add(member)
        #하나라도 다른경우
        else:
            
            for member in meeting:
                if result[member] == 1:
                    if member in maybe:
                        maybe.pop
            print("No")
            return
        
    #print("Maybe : " , maybe)
    #print("Never : " , never)

    for n in never:
        if n in maybe:
            maybe.remove(n)

    answer = ''

    print("YES")

    for i in range(1, N+1):
        if i in maybe:
            answer += '1 '
        else:
            answer += '0 '
    answer.rstrip()
    print(answer)
    

solution()
#print(meetings)
"""
7 3
3 1 2 3
3 3 4 5
3 5 6 7
0 0 1 1 1 1 1
"""

"""
print(N,M)
for m in meeting:
    print(m)
print(result)
"""
              
            
            