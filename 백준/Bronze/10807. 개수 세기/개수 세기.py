N = int(input())
N_list = list(map(int, input().split()))
v = int(input())

cnt = 0

for i in range(N):
    if N_list[i] == v:
        cnt += 1
        
print(cnt)