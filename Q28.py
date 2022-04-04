import sys

input = sys.stdin.readline

N = int(input())
array = list(map(int, input().split()))
print(array)

def binary_search(array, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == mid:
            return mid
        elif array[mid] > mid:
            return binary_search(array, start, mid - 1)
        else:
            return binary_search(array, mid + 1, end)
    return None

result = binary_search(array, 0, N - 1)

if result == None:
    print("-1")
else:
    print(result)


