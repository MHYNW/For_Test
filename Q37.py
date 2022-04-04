n = int(input())
m = int(input())

INF = int(1e9)
graph = [[INF]*(n + 1) for _ in range(n + 1)]

'''set diagonal 0'''
for i in range(n + 1):
    graph[i][i] = 0

for _ in range(m):
    start_node, end_node, cost = map(int, input().split())
    '''중복 대비'''
    if cost < graph[start_node][end_node]:
        graph[start_node][end_node] = cost

for step in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            graph[i][j] = min(graph[i][j], graph[i][step] + graph[step][j])

'''print'''
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if graph[i][j] == INF:      #도달하지 못하는 경우
            print(0, end=" ")
        else:
            print(graph[i][j], end=" ")
    print()
