from itertools import combinations
import sys
input = sys.stdin.readline

N,K = map(int,input().split())
words = []
    
#배울목록
alpha = set()
answer = 0
    
for _ in range(N):
    word = list(input().rstrip())
    word[-4:] = []
    word[:4] = []
    words.append(word)

    for w in word:
        alpha.add(w)
K -= 5
def check():
    result = 0
    for word in words:
        flag = True
        #배운경우
        for w in word:
            if w in study:
                pass
            else:
                flag = False
                break   
        if flag:
            result += 1
    return result

def solution(index,cnt):
    global answer
    if cnt == K:
        answer = max(answer, check())
        return
    for i in range(index, 26):
        if check[i] == True:
            continue
        check[i] = True
        go(i+1, cnt+1)
        check[i] = False
    for study in combinations(alpha,K):
        study = list(study)
        study.append('a')
        study.append('n')
        study.append('c')
        study.append('t')
        study.append('i')
        
    return answer
    
if K < 0:
    print(0)
elif K == 26:
    print(N)
else: 
    print(solution(0,0))

