from collections import deque

def combinations(list, n):
    result = []
    if n == 0:
        return[[]]

    for i in range(len(list)):
        elem = list[i]
        for rest in combinations(list[i + 1:], n - 1):
            result.append([elem] + rest)

    return result

N, M = map(int, input().split())
map_arr = []
visited = [[0] * M for _ in range(N)]
q = deque()
zero_space = []

for _ in range(N):
    map_arr.append(list(map(int, input().split())))

for i in range(N):
    for j in range(M):
        if map_arr[i][j] == 0:
            zero_space.append((i, j))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
count = 0

wall_list = combinations(zero_space, 3)

def bfs(map_arr, q, x1, x2, x3, y1, y2, y3):

    for i in range(N):
        for j in range(M):
            visited[i][j] = map_arr[i][j]
            if map_arr[i][j] == 2:
                q.append((i, j))

    visited[x1][y1] = 1
    visited[x2][y2] = 1
    visited[x3][y3] = 1
    ct = 0

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and nx < N and ny >= 0 and ny < M and visited[nx][ny] == 0:
                visited[nx][ny] = 2
                q.append((nx, ny))
    for i in range(N):
        for j in range(M):
            if visited[i][j] == 0:
                ct += 1


    return ct


for i in wall_list:
    (x1, y1), (x2, y2), (x3, y3) = i
    bfs_result = bfs(map_arr, q, x1, x2, x3, y1, y2, y3)
    if bfs_result > count:
        count = bfs_result

print(count)

