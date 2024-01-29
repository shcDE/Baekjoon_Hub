N, M = map(int, input().split())
N_list = [i+1 for i in range(N)]

for _ in range(M):
    i, j = map(int, input().split())
    N_list[i-1], N_list[j-1] = N_list[j-1], N_list[i-1]
    
for i in range(N):
    print(N_list[i], end = ' ')