def solution(food_times, k):
    answer = 0
    index = 0
    n = len(food_times)
    portion = k // n
    rest = k % n
    if sum(food_times) <= k:
        return -1
    else:
        for i in range(n):
            if food_times[i] >= portion:
                food_times[i] -= portion
            else:
                food_times[i] = 0
                rest += (portion - food_times[i])
        while rest > 0:
            if food_times[index] > 0:
                food_times[index] -= 1
                index = (index + 1) % n
                rest -= 1
            else:
                index = (index + 1) % n

        answer = index + 1

    return answer