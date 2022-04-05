N = int(input())
array = list(map(int, input().split()))
dynamic_array = [1] * N

for i in range(1, N):
    for j in range(0, i):
        if array[j] > array[i]:
            dynamic_array[i] = max(dynamic_array[i], dynamic_array[j] + 1)

result = N - max(dynamic_array)
print(result)




