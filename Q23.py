N = map(int, input().split())

array = []

for _ in range(N):
    name, kor, eng, math = input().split()
    array.append(name, int(kor), int(eng), int(math))

array = sorted(array, key=lambda students: (-int(students[1]), int(students[2], -int(students[3]), students[0])))
# 2번째 원소로 내림차순, 3번째 원소로 오름차순, 4번째 원소로 내림차순, 1번째 원소로 오름차순

for students in array:
    print(students[0])


