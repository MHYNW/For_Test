T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    array_input = list(map(int, input().split()))
    graph = [[0]*m for _ in range(n)]
    for i in range(n):
        graph[i] = array_input[i*m:(i + 1)*m]

    for a in range(1, m):
        for b in range(n):
            if b == 0:
                graph[b][a] += max(graph[b][a - 1], graph[b + 1][a - 1])
            elif b == n - 1:
                graph[b][a] += max(graph[b][a - 1], graph[b - 1][a - 1])
            else:
                graph[b][a] += max(graph[b][a - 1], graph[b - 1][a - 1], graph[b + 1][a - 1])
    result = 0
    for i in range(n):
        result = max(result, graph[i][m - 1])

    print(result)


