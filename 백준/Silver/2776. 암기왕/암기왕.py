for _ in range(int(input())):
    N = int(input())
    N_set = set(map(int, input().split()))
    M = int(input())
    M_list = list(map(int, input().split()))

    for i in M_list:
        print(1) if i in N_set else print(0)