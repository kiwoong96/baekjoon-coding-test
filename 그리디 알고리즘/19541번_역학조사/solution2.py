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

def solution():
    count = 0
    for meeting in meetings:
        count += 1
        flag = True
        target = result[meeting[1]]
        for i in range(2,len(meeting)):
            member = meeting[i]
            #하나라도 다른값이 있는경우
            if result[member] != target:
                flag = False
                break

        #하나라도 다른경우
        if not flag:
            if count == 1:
                print("NO")
                return
            for member in meeting[1:]:
                if result[member] == 1:
                    result[member] = 0

        
    #print("Maybe : " , maybe)
    #print("Never : " , never)
    answer = ''

    print("YES")

    for i in range(1, len(result)):
        if result[i] == 1: 
            answer += '1 '
        else:
            answer += '0 '
    answer.rstrip()
    print(answer)
    

solution()