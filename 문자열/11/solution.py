import sys
input = sys.stdin.readline
T = input().rstrip()
P = input().rstrip()


Pi = [0 for _ in range(len(P))]
idx = []
answer = 0

#1. 완탐/ 2번. KMP
def findPi(patt):
    global Pi
    length = 0  #비교되는 문자 위치(고정) j
    
    sIdx = 1    #비교하느 문자 위치     i
    while sIdx < len(patt):
        #문자가 같은경우
        if patt[sIdx] == patt[length]:
            length += 1
            Pi[sIdx] =  length
            sIdx += 1
        else:
            #첫문자가 아닌경우 -> Pi에서 시작위치 가져옴.
            if length != 0:
                length = Pi[length - 1]
            #첫문자인경우 +1
            else:
                Pi[sIdx] = 0
                sIdx += 1

def KMP(T,P):
    global answer, idx, Pi
    N = len(T)
    M = len(P)

    #Pi 구하기
    findPi(P)
    
    i = 0
    j = 0
    while i < N:
        #문자가 같을경우
        if P[j] == T[i]:
            i += 1
            j += 1
        #다른경ㅇ 
        elif P[j] != T[i]:
            #첫문자가 아닌경우 -> Pi에서 시작위치 가져옴.
            if j != 0:
                j = Pi[j - 1]
            #첫문자 인경우 +1
            else:
                i += 1
        if j == M: 
            idx.append(i - j + 1)
            answer += 1
            j = Pi[j - 1]
            

KMP(T, P)
print(answer)
print(*idx)
