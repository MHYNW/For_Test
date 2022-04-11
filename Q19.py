N = int(input())
array = list(map(int, input().split()))
calculate = list(map(int, input().split()))
p = calculate[0]
m = calculate[1]
t = calculate[2]
d = calculate[3]

maxnum = -int(1e9)
minnum = int(1e9)

def dfs(step, now):
    global p, m, t, d, maxnum, minnum
    if step == N - 1:
        maxnum = max(maxnum, now)
        minnum = min(minnum, now)
    if step <= N - 2:
        if p > 0:
            p -= 1
            new = now + array[step + 1]
            dfs(step + 1, new)
            p += 1
        if m > 0:
            m -= 1
            new = now - array[step + 1]
            dfs(step + 1, new)
            m += 1
        if t > 0:
            t -= 1
            new = now * array[step + 1]
            dfs(step + 1, new)
            t += 1
        if d > 0:
            d -= 1
            if now < 0 and array[step + 1] < 0:
                new = (-now) // (-array[step + 1])
            elif now < 0 and array[step + 1] > 0:
                new = -((-now) // array[step + 1])
            elif now > 0 and array[step + 1] < 0:
                new = -(now // (-array[step + 1]))
            else:
                new = now // array[step + 1]
            dfs(step + 1, new)
            d += 1

dfs(0, array[0])

print(maxnum)
print(minnum)









