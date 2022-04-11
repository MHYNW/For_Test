from collections import deque

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)
visited[1] = 1

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(graph):
    q = deque()
    q.append((1, 0))
    while q:
        now, cost = q.popleft()
        for i in graph[now]:
            if visited[i] == 0:
                visited[i] = cost + 1
                cost = visited[i]
                q.append((i, cost))


bfs(graph)

print(visited)


