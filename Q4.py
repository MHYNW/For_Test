N = int(input())

array = list(map(int, input().split()))

array.sort()

target = 1

for coin in array:
    if target < coin:
        break
    else:
        target += coin

print(target)
