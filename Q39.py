import heapq
INF = int(1e9)
T = int(input())

result = [0] * T

dx = [1, -1, 0, 0]      # up, down, right, left
dy = [0, 0, 1, -1]

for case in range(T):
    N = int(input())
    q = []
    array = []
    distance = [[INF] * N for _ in range(N)]

    for i in range(N):
        array.append(list(map(int, input().split())))

    heapq.heappush(q, (array[0][0], 0, 0))
    distance[0][0] = array[0][0]

    while q:
        path = 0
        cost, x, y = heapq.heappop(q)
        if distance[x][y] < cost:
            continue

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >=0 and nx < N and ny >= 0 and ny < N:
                path = array[nx][ny] + cost
                if path < distance[nx][ny]:
                    distance[nx][ny] = path
                    heapq.heappush(q, (path, nx, ny))

    result[case] = distance[N - 1][N - 1]

for case in range(T):
    print(result[case])
