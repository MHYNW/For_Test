s = input()
n = len(s)
array = []

'''slice the string'''
for i in range(n):
    array.append(int(s[i]))

'''get maximum calculate'''
for i in range(1, n):
    array[i] = max((array[i - 1] + array[i]), (array[i - 1]*array[i]))

print(array[n - 1])


