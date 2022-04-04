from collections import deque

N, K = map(int, input().split())
array = []
virus_list = []
for _ in range(N):
    array.append(list(map(int, input().split())))
S, X, Y = map(int, input().split())

for i in range(N):
    for j in range(N):
        if array[i][j] != 0:
            virus_list.append((array[i][j],0, i, j))

virus_list.sort()
q = deque(virus_list)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

while q:
    virus, s, a, b = q.popleft()
    if s == S:
        break
    for i in range(4):
        nx = a + dx[i]
        ny = b + dy[i]
        if nx >= 0 and nx < N and ny >= 0 and ny < N:
            if array[nx][ny] == 0:
                array[nx][ny] = virus
                q.append((virus, s + 1, nx, ny))

result = array[X - 1][Y - 1]
print(result)

