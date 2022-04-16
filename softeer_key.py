msg = input()
key = input()
key_buffer = []
alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
key_array = [[] * 5 for _ in range(5)]
divided_msg = []

def finding_index(key_array, a, b):
    a_index = [6, 6]
    b_index = [6, 6]
    for i in range(5):
        for j in range(5):
            if key_array[i][j] == a:
                a_index = [i, j]
            elif key_array[i][j] == b:
                b_index = [i, j]

            if a_index != [6, 6] and b_index != [6, 6]:
                return a_index, b_index

    return a_index, b_index


'''making key'''
for i in range(len(key)):
    if key_buffer.count(key[i]) == 0:
        key_buffer.append(key[i])
        alpha.remove(key[i])
    else:
        pass

for i in range(len(alpha)):
    key_buffer.append(alpha[i])

for i in range(5):
    key_array[i] = key_buffer[5 * i:5 * i + 5]

'''divide by 2 words'''
count = 1
while True:
    if count > len(msg):
        break
    elif count == len(msg):
        divided_msg.append([msg[count - 1], 'X'])
        break

    elif count == len(msg) - 1:
        if msg[count - 1] == msg[count]:
            if msg[count - 1] == 'X':
                divided_msg.append([msg[count - 1], 'Q'])
            else:
                divided_msg.append([msg[count - 1], 'X'])
            divided_msg.append([msg[count], 'X'])
        else:
            divided_msg.append([msg[count - 1], msg[count]])
        break

    if msg[count - 1] == msg[count]:
        if msg[count - 1] == 'X':
            divided_msg.append([msg[count - 1], 'Q'])
            count += 1
        else:
            divided_msg.append([msg[count - 1], 'X'])
            count += 1
        continue
    else:
        '''
        if count == len(msg) - 2:
            divided_msg.append([msg[count - 1], msg[count]])
            divided_msg.append([msg[count + 1], 'X'])
            break
            '''

        divided_msg.append([msg[count - 1], msg[count]])
        count += 2
        continue


'''encoding process'''
result = ""
result_array = []
for code in divided_msg:
    a, b = code
    a_index, b_index = finding_index(key_array, a, b)
    if a_index[0] == b_index[0]:
        result_array.append(key_array[a_index[0]][(a_index[1] + 1) % 5])
        result_array.append(key_array[b_index[0]][(b_index[1] + 1) % 5])
    elif a_index[1] == b_index[1] and a_index[0] != b_index[0]:
        result_array.append(key_array[(a_index[0] + 1) % 5][a_index[1]])
        result_array.append(key_array[(b_index[0] + 1) % 5][b_index[1]])
    elif a_index[0] != b_index[0] and a_index[1] != b_index[1]:
        result_array.append(key_array[a_index[0]][b_index[1]])
        result_array.append(key_array[b_index[0]][a_index[1]])
result = ''.join(result_array)
print(result)







