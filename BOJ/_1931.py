import sys


def problem():
    input = sys.stdin.readline
    N = int(input())
    input_list = [list(map(int, input().split())) for _ in range(N)]
    input_list.sort(key=lambda x: (x[1], x[0]))
    # input_list.sort(key=lambda x:x[0])
    min = 0
    answer_list = list()
    for class_time in input_list:
        if class_time[0] >= min:
            answer_list.append(class_time)
            min = class_time[1]
    print(len(answer_list))
