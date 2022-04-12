N, M = map(int, input().split())
array = list(map(int, input().split()))

count = 0
for i in range(N):
    a = array[i]
    for j in range(i, N):
        b = array[j]
        if a != b:
            count += 1

print(count)
