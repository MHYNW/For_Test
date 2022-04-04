from collections import deque

INF = int(1e9)  # set const.
Flag = False    # Flag for existence of K
N, M, K, X = map(int, input().split())  # input

'''init lists'''
graph = [[] for i in range(N + 1)]
distance = [INF] * (N + 1)
distance[X] = 0

'''input graph'''
for _ in range(1, M + 1):
    a, b = map(int, input().split())
    graph[a].append(b)

'''BFS by queue'''
q = deque()
q.append(X)
while q:
    now = q.popleft()
    for i in graph[now]:
        if distance[i] == INF:
            distance[i] = distance[now] + 1
            q.append(i)

for i in range(1, N + 1):
    if distance[i] == K:
        print(i)
        Flag = True

if Flag == False:
    print('-1')






