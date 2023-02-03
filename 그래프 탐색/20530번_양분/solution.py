import sys
input = sys.stdin.readline

N,Q = map(int,input().split())
graph = [[]for _ in range(N+1)]
questions = []

for i in range(N):
    start, end = map(int,input().split())
    graph[start].append(end)
    graph[end].append(start)

for i in range(Q):
    questions.append(list(map(int,input().split())))


print(graph)
print(questions)


    
