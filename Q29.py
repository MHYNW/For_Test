N, C = map(int, input().split())

house_array = []

for _ in range(N):
    house_array.append(int(input()))

house_array.sort()

def binary_search(array, start, end):
    result = 0
    while start <= end:
        mid = (start + end) // 2
        count = 1
        pin_point = house_array[0]
        for i in range(1, N):
            if house_array[i] >= pin_point + mid:
                count += 1
                pin_point = house_array[i]
        if count >= C:
            start = mid + 1
            result = mid
                
        elif count < C:
            end = mid - 1
    return result

print(binary_search(house_array, 1, house_array[N - 1] - house_array[0]))



