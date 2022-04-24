import heapq


def solution(n, edge):
    INF = int(1e9)
    answer = 0
    q = []
    graph = [[] for _ in range(n + 1)]
    distance = [INF] * (n + 1)
    for route in edge:
        a, b = route
        graph[a].append(b)
        graph[b].append(a)

    '''
    for i in graph[1]:
        heapq.heappush(q, (0, i))
    '''
    heapq.heappush(q, (0, 1))
    distance[1] = 0

    while q:
        cost, node = heapq.heappop(q)
        if cost > distance[node]:
            continue
        for i in graph[node]:
            new_cost = cost + 1
            if new_cost < distance[i]:
                heapq.heappush(q, (new_cost, i))
                distance[i] = new_cost

    for i in range(1, n + 1):
        if distance[i] == INF:
            distance[i] = -1

        maximum = max(distance)
    print(maximum)
    for i in range(1, n + 1):
        if distance[i] == maximum:
            answer += 1

    return answer