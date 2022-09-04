import sys


def problem():
    input = sys.stdin.readline
    input_list = input().strip().split('-')
    result = 0

    for num in input_list[0].split("+"):
        result += int(num)

    for element in input_list[1:]:
        sum_ = 0
        for num in element.split("+"):
            sum_ += int(num)
        result -= sum_
    print(result)
