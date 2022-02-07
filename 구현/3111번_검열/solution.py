import sys
input = sys.stdin.readline

#마지막 문단바꾸기 제거
A = input().rstrip()
T = input().rstrip()

#list형태로 scailing
reverse_A = list(reversed(A))
A = list(A)

frontIdx = 0
backIdx = len(T)-1

front = []
back = []

flag = True     #True -> front / False -> back

while frontIdx <= backIdx:
    
    if flag:
        front.append(T[frontIdx])
        frontIdx += 1
        #print(front[-len(A):])
        if front[-len(A):] == A:
            #front = front[:-len(A)] #len(a) = 1 , len(front) = 300,000 * 300,000 * 25
            front[-len(A):] = []
            flag = False
    else:
        back.append(T[backIdx])
        backIdx -= 1
        
        if back[-len(A):] == reverse_A:
            back[-len(A):] = []
            flag = True
    
while back :
    front.append(back.pop())

    if front[-len(A):] == A:
        # front = front[:-len_A]
        front[-len(A):] = []

answer = "".join(front)
print(answer)
    