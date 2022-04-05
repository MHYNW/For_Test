N = int(input())

time_array = []
cost_array = []
dynamic_array = [0] * N
max_value = 0

for _ in range(N):
    t, p = map(int, input().split())
    time_array.append(t)
    cost_array.append(p)

for i in range(N - 1, -1, -1):
    if time_array[i] + i < N:
        dynamic_array[i] = max(cost_array[i] + dynamic_array[time_array[i] + i], max_value)
        max_value = dynamic_array[i]
    else:
        dynamic_array[i] = max_value

print(max_value)

