from collections import deque

T = int(input())

for _ in range(T):
    p = input()
    n = int(input())
    int_raw = input()[1:-1]
    int_list = deque(int_raw.split(','))

    flag = 0

    if n == 0:
        int_list = []

    for i in range(len(p)):
        if p[i] == "R":
            flag += 1
        else:
            if len(int_list) == 0:
                print("error")
                break
            else:
                if flag % 2 == 0:
                    int_list.popleft()
                else:
                    int_list.pop()

    else:
        if flag % 2 == 0:
            print("[" + ",".join(int_list) + "]")
        else:
            int_list.reverse()
            print("[" + ",".join(int_list) + "]")

