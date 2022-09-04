def problem():
    import sys

    input = sys.stdin.readline
    N = int(input())
    # N_set = set(map(int, input().split()))
    N_list = list(map(int, input().split()))
    M = int(input())
    M_list = list(map(int, input().split()))
    # for num in M_list:
    #     if num in N_set:
    #         print(1)
    #     else:
    #         print(0)
    N_list.sort()
    # 원래 짜던대로 하면 슬라이싱이기 때문에 시간이 오래 걸린다.
    # 그러므로 이 방식대로 인덱싱을 하는 것이 좋다.

    def binary_search(value, start, end):
        print(N_list[start : end + 1])
        if start > end:
            return False
        median = (start + end) // 2
        if N_list[median] > value:
            return binary_search(value, start, median - 1)
        elif N_list[median] < value:
            return binary_search(value, median + 1, end)
        else:
            return True

    for num in M_list:
        if binary_search(num, 0, N - 1):
            print(1)
        else:
            print(0)
