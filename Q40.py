import heapq

N, M = map(int, input().split())
INF = int(1e9)

graph = [[] for _ in range(N + 1)]
distance= [INF] * (N + 1)

for _ in range(M):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)    #양방향성이기 때문에!!!!

q = []
heapq.heappush(q, (0, 1))
distance[1] = 0
while q:
    cost, node = heapq.heappop(q)
    if cost <= distance[node]:
        for i in graph[node]:
            result = cost + 1
            if result < distance[i]:
                distance[i] = result
                heapq.heappush(q, (result, i))

maximum = 0
index= 0
count = []

for i in range(N, 0, -1):
    if distance[i] != INF and maximum < distance[i]:
        maximum = distance[i]
        index = i
        count = [i]

    elif distance[i] != INF and maximum == distance[i]:
        count.append(i)
        index = i


print(index, maximum, len(count))

