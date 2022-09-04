import sys


def problem():
    # input = sys.stdin.readline
    # S = input().strip()
    # is_one = False
    # is_zero = False
    # zero_count = 0
    # one_count = 0
    # for num in S:
    #     if int(num) == 1:
    #         is_zero = False
    #         if is_one:
    #             continue
    #         else:
    #             is_one = True
    #             one_count += 1
    #     else:
    #         is_one = False
    #         if is_zero:
    #             continue
    #         else:
    #             is_zero = True
    #             zero_count += 1
    # print(zero_count, one_count)
    # print(min(zero_count, one_count))
    input = sys.stdin.readline
    S = input().strip()
    prev = '2'
    count = 0
    for num in S:
        if num != prev:
            count += 1
            prev = num
    print(count // 2)
