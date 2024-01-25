N, M = map(int, input().split())
N_basket = [0 for _ in range(N)]

for _ in range(M):
    i, j, k = map(int, input().split())
    for I in range(i, j+1):
        N_basket[I-1] = k
        
for i in range(N):
    print(N_basket[i], end = ' ')
    
