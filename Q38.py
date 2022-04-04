N, M  = map(int, input().split())

INF = int(1e9)
result = 0
graph = [[INF] * (N + 1) for _ in range(N + 1)]

for i in range (1, N + 1):
    graph[i][i] = 0

for i in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1

for step in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            graph[i][j] = min(graph[i][j], graph[i][step] + graph[step][j])

for i in range(1, N + 1):
    count = 0
    for j in range(1, N + 1):
        if i != j:
            if (graph[i][j] != INF) or (graph[j][i] != INF):
                count += 1
    if count == N - 1:
        result += 1

print(result)



