from collections import deque

N = int(input())

'''map input'''
map_arr = []
for _ in range(N):
    map_arr.append(list(map(int, input().split())))

'''finding start point of baby shark'''
start = []
shark_size = 2
shark_digested = 0

for i in range(N):
    for j in range(N):
        if map_arr[i][j] == 9:
            start = [i, j]
            map_arr[i][j] = 0
            break

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
time = 0

def get_distance(x, y):
    visited = [[-1] * N for _ in range(N)]
    q = deque()
    q.append((0, x, y))
    while q:
        dist, a, b = q.popleft()
        visited[a][b] = dist
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if visited[nx][ny] == -1 and map_arr[nx][ny] <= shark_size:
                q.append((dist + 1, nx, ny))

    return visited

def finding(visited, x, y):
    min_dist = int(1e9)
    for i in range(N):
        for j in range(N):
            if visited[i][j] != -1 and 1 <= map_arr[i][j] and map_arr[i][j] < shark_size:
                if visited[i][j] < min_dist:
                    x, y = i, j
                    min_dist = visited[i][j]
    if min_dist == int(1e9):
        return None
    else:
        return min_dist, x, y


x, y = start
while True:
    visited = get_distance(x, y)
    value = finding(visited, x, y)
    if value == None:
        break
    else:
        distance, x, y = value[0], value[1], value[2]
        map_arr[x][y] = 0
        shark_digested += 1
        if shark_digested == shark_size:
            shark_digested = 0
            shark_size += 1
        time += distance

print(time)
