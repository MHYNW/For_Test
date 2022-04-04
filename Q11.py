from collections import deque

N = int(input())
K = int(input())

map_array = [[0] * (N + 2) for _ in range(N + 2)]
'''apple =2, wall = 1, snake = -1, blank = 0'''

for i in range(K):
    a, b = map(int, input().split())
    map_array[a][b] = 2

for i in range(N + 2):
    map_array[i][0] = 1
    map_array[i][N + 1] = 1
    map_array[0][i] = 1
    map_array[N + 1][i] = 1

L = int(input())
control_direction = []
control_time = []

for i in range(L):
    time, rotating = input().split()
    control_time.append(int(time))
    control_direction.append(rotating)

alive = True
time = 0
dx = [-1, 0, 1, 0]      # up, right, down, left -> to rotate
dy = [0, 1, 0, -1]

head = [1, 1]
count = 0
x_default = 1
y_default = 1
snake = deque()
snake.append((head[0], head[1]))  # start
map_array[head[0]][head[1]] = -1

while alive:
    time += 1
    head[0] += dx[x_default]
    head[1] += dy[y_default]
    if map_array[head[0]][head[1]] == 0:
        map_array[head[0]][head[1]] = -1
        snake.append((head[0], head[1]))
        a, b = snake.popleft()      # tail banishing
        map_array[a][b] = 0
    elif map_array[head[0]][head[1]] == 2:
        map_array[head[0]][head[1]] = -1
        snake.append((head[0], head[1]))
    else:
        print(time)
        alive = False
    if count < L and control_time[count] == time:
        if control_direction[count] == 'L':
            x_default = (x_default - 1) % 4
            y_default = (y_default - 1) % 4
        else:
            x_default = (x_default + 1) % 4
            y_default = (y_default + 1) % 4

        count += 1







