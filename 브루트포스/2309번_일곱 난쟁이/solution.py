import sys

data = [0 for _ in range(9)]

for i in range(9):
    data[i] = int(input())

#combination
from itertools import combinations

combs = list(combinations(data,7))
result = [];

print()

for comb in combs:
    if sum(comb)==100:
        result = list(comb)
        break

result.sort()
for r in result:
    print(r)
