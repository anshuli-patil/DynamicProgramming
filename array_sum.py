import sys
from random import randint


def play_game(array, start, end):
    if start == end - 2:
        if array[start] == array[end - 1]:
            return 1
        else:
            return 0
    if start == end - 1:
        return 0

    index = split_index(array, start, end)

    if index is None:
        return 0
    else:
        return max(play_game(array, start, index),
                   play_game(array, index, end)) + 1


def split_index(array, start, end):
    sum_array = sum(array[start:end])

    if sum_array % 2 != 0:
        return None

    index = -1
    sum_half = 0

    for i in range(start, end):
        sum_half += array[i]
        if sum_half == sum_array / 2:
            index = i
            break
    if index == -1:
        return None
    else:
        return index + 1


arr = [randint(0,pow(10,9)) for i in range(pow(2,12))]
reverse_arr = list(arr)
reverse_arr.reverse()
arr.extend(reverse_arr)

arr = [3, 3, 3, 3, 1, 4, 3, 3, 3, 3, 1, 4]
# print(play_game(arr,0, len(arr)))
# print (split_index(arr, 0, len(arr)))



T = int(sys.stdin.readline())
for i in range(T):
    N = int(sys.stdin.readline())
    health = []
    line = sys.stdin.readline().split()
    for health_val in line:
        health.append(int(health_val))
    print (play_game(health, 0, N))

