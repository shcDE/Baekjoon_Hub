import sys

n = int(sys.stdin.readline())
n_list=[i+1 for i in range(n)]

while len(n_list) > 1:
    for i in range(0, len(n_list), 2):
        n_list[i] = 0
        
    while 0 in n_list:
        n_list.remove(0)
print(n_list[0])