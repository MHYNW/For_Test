string = input()
count_zero = 0
count_one = 0

if string[0] == '1':
    count_one += 1
else:
    count_zero += 1

for i in range(len(string) - 1):
    if string[i] < string[i + 1]:
        count_one += 1
    elif string[i] > string[i + 1]:
        count_zero += 1

print(min(count_zero, count_one))