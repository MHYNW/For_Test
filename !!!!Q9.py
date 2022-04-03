s = input()
n = len(s)
str_length = int(1e9)

for j in range(1, n // 2 + 1):
    count = 1
    string = ""
    prev = s[0:j]
    for i in range(j, n, j):
        if prev == s[i:i + j]:
            count += 1
        else:
            if count != 1:
                string += str(count) + prev
            else:
                string += prev
            count = 1
            prev = s[i:i + j]
    if count != 1:
        string += str(count) + prev
    else:
        string += prev
    str_length = min(len(string), str_length)

print(str_length)


