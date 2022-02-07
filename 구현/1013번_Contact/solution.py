import sys
input = sys.stdin.readline

def DFA(idx, typ, s):
    #잘못된 경우
    if typ == -1:
        print("NO")
        return
    #종료 시점인 경우
    if idx == len(s) and (typ == 5 or typ == 6 or typ == 7):
        print("YES")
        return 
    #조건 체크중 문자열 종료인 경우
    if idx == len(s):
        print("NO")
        return 
    
    if typ == 0:
        if s[idx] == '0':
            DFA(idx+1, 2, s)
        else:
            DFA(idx+1, 1, s)
    elif typ == 1:
        if s[idx] == '0':
            DFA(idx+1, 3, s)
        else:
            DFA(idx+1, -1, s)
    elif typ == 2:
        if s[idx] == '0':
            DFA(idx+1, -1, s)
        else:
            DFA(idx+1, 6, s)
    elif typ == 3:
        if s[idx] == '0':
            DFA(idx+1, 4, s)
        else:
            DFA(idx+1, -1, s)
    elif typ == 4:
        if s[idx] == '0':
            DFA(idx+1, 4, s)
        else:
            DFA(idx+1, 5, s)
    elif typ == 5:
        if s[idx] == '0':
            DFA(idx+1, 2, s)
        else:
            DFA(idx+1, 7, s)
    elif typ == 6:
        if s[idx] == '0':
            DFA(idx+1, 2, s)
        else:
            DFA(idx+1, 1, s)
    elif typ == 7:
        if s[idx] == '0':
            DFA(idx+1, 8, s)
        else:
            DFA(idx+1, 7, s)
    elif typ == 8:
        if s[idx] == '0':
            DFA(idx+1, 4, s)
        else:
            DFA(idx+1, 6, s)

    return True
def solution(stringList):
    for s in stringList:
        #index, type, string
        DFA(0,0,s)


N = int(input())
stringList = []
for _ in range(N):
    stringList.append(input().rstrip())


solution(stringList)




import re

N = int(input())
string= []
for _ in range(N):
    string.append(input())

for i in string:
    p=re.compile('(100+1+|01)+')
    result=p.fullmatch(i)
    if result:
        print('YES')
    else:
        print('NO')



"""
7
10010111
011000100110001 
0110001011001
10011001
1001111111
01100010110011001
10000110001
"""