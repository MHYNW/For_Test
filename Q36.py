a = input()
b = input()
n = 0
if len(a) > len(b):
    n = len(a)
else:
    n = len(b)

dp = ""
count = 0

for i in range(n):
    if a[i] == b[i]:
        dp.append[a[i]]
    else:
        count += 1
        a[i] = b[i]
