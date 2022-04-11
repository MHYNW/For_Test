N, L, R = map(int, input().split())
array = []
for i in range(N):
    array.append(list(map(int, input().split())))

visited = [[0] * N for _ in range(N)]
array_copy = [[0] * N for _ in range(N)]

def dfs(array, visited, united, x, y, k, count, summation):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    visited[x][y] = k
    count += 1
    united.append((x, y))
    summation += array[x][y]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx > (N - 1) or ny < 0 or ny > (N - 1):
            continue
        if visited[nx][ny] == 0 and abs(array[nx][ny] - array[x][y]) >= L and abs(array[nx][ny] - array[x][y]) <= R:
            count, summation = dfs(array, visited, united, nx, ny, k, count, summation)

    return count, summation



result = 0

while True:
    for i in range(N):
        for j in range(N):
            array_copy[i][j] = array[i][j]

    k = 0
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                k += 1
                summation = 0
                count = 0
                united = []
                count, summation = dfs(array, visited, united, i, j, k, count, summation)
                for nation in united:
                    x, y = nation
                    array[x][y] = summation // count
    if array == array_copy:
        break
    else:
        result += 1

print(result)




