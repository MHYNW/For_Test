string = input()
sum_num = 0
array_str = []

for i in range(len(string)):
    if ord(string[i]) >= 65:            #isalpha == True 써도 될듯
        array_str.append(string[i])
    else:
        sum_num += int(string[i])

array_str.sort()
if sum_num != 0:
    array_str.append(sum_num)

for i in range(len(array_str)):
    print(array_str[i], end="")