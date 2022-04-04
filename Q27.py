import sys

input = sys.stdin.readline

def find_number(array, target, N):
    left_index = binary_search_left(array, x, 0, N - 1)
    if left_index == None:
        return -1
    right_index = binary_search_right(array, x, 0, N - 1)

    return (right_index - left_index + 1)


def binary_search_left(array, target, start, end):
    while start <= end:
        mid = (start + end)//2
        if ((array[mid] == start) or (array[mid - 1] < target)) and array[mid] == target:
            return mid
        elif array[mid] < target:
            return binary_search_left(array, target, mid + 1, end)
        elif array[mid] >= target:
            return binary_search_left(array, target, start, mid - 1)

    return None

def binary_search_right(array, target, start, end):
    while start <= end:
        mid = (start + end)//2
        if ((array[mid] == end) or (array[mid + 1] > target)) and array[mid] == target:
            return mid
        elif array[mid] <= target:
            return binary_search_right(array, target, mid + 1, end)
        elif array[mid] > target:
            return binary_search_right(array, target, start, mid - 1)


N, x = map(int, input().split())
array = list(map(int, input().split()))

print(find_number(array, x, N))


