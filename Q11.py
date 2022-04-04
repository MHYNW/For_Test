N = int(input())
K = int(input())

map_array = [[0] * (N + 1) for _ in range(N + 1)]

'''apple =2, wall = 1, snake = -1, blank = 0'''

for i in range(K):
    a, b = map(int, input().split())
    map_array[a][b] = 2

for i in range(1, N + 1):
    map_array[i][1] = 1
    map_array[i][N] = 1
    map_array[1][i] = 1
    map_array[N][i] = 1

L = input()
control = []

for i in range(L):
    time, rotating = input().split()
    control.append((int(time), rotating))       # int(time) 오류생길수있음 유의

alive = True
time = 0
dx = [-1, 1, 0, 0]      # up, down, left, right
dy = [0, 0 , -1, 1]


#while alive:




