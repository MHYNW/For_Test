import copy

N, M = map(int, input().split())
map_buffer = []
map_virus = [[0]*M for _ in range(N)]
count = 0
result = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(N):
    map_buffer.append(list(map(int, input().split())))

def dfs(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and nx < N and ny >= 0 and ny < M:
            if map_virus[nx][ny] == 0:
                map_virus[nx][ny] = 2
                dfs(nx,ny)

def get_score():
    score = 0
    for i in range(N):
        score += map_virus[i].count(0)
    '''
    for i in range(N):
        for j in range(M):
            if map_virus[i][j] == 0:
                score += 1
    '''
    return score

def main(count):
    global result
    if count < 3:
        for i in range(N):
            for j in range(M):
                if map_buffer[i][j] == 0:
                    map_buffer[i][j] = 1
                    count += 1
                    main(count)
                    count -= 1
                    map_buffer[i][j] = 0
    else:
        #map_virus = copy.deepcopy(map_buffer)
        for i in range(N):
            map_virus[i] = map_buffer[i][:]
        '''
        for i in range(N):
            for j in range(M):
                map_virus[i][j] = map_buffer[i][j]
        '''
        for i in range(N):
            for j in range(M):
                if map_virus[i][j] == 2:
                    dfs(i, j)
        result = max(get_score(), result)

main(0)
print(result)

