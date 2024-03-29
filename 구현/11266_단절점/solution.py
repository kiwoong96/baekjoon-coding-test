import sys
from collections import defaultdict

sys.setrecursionlimit(10**6)

def dfs(here, cnt):
    order[here] = cnt

    children = 0
    ret = order[here]

    for next in graph[here] :
        if order[next] :
            ret = min(ret, order[next])

        else :
            children += 1
            subtree = dfs(next, cnt+1)

            if cnt != 1 and subtree >= order[here] :
                cutVertex.add(here)

            ret = min(subtree, ret)

    if cnt == 1 and children >= 2 :
        cutVertex.add(here)

    return ret






# N개
V,E = map(int, sys.stdin.readline().split())
graph = defaultdict(list)
cutVertex = set()
candidates = set()

for _ in range(E) :
    a,b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
    candidates.add(a)
    candidates.add(b)

order = [None for _ in range(V+1)]
cnt = 1

for vertex in candidates :
    if not order[vertex] :
        dfs(vertex, 1)

print(len(cutVertex))

for vertex in sorted(list(cutVertex)) :
    print(vertex, end=" ")