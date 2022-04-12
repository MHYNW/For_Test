from itertools import combinations
from itertools import product

N, M = map(int, input().split())
array = list(map(int, input().split()))

comb = list(combinations(array, 2))
result = 0

for i in comb:
    a, b = i
    if a != b:
        result += 1

print(result)

