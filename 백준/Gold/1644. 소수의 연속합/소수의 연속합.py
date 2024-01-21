from math import sqrt

N = int(input())

arr = [1 for _ in range(N+1)]
arr[0] = 0
arr[1] = 0

for i in range(2, int(sqrt(N)) + 1):
    if arr[i]:
        for j in range(i*2, N+1, i):
            arr[j] = 0
            
arr = [i for i in range(2, N+1) if arr[i]] + [0]

l1 = 0
l2 = 0
st = arr[l1]
cnt = 0

while l2 < len(arr) - 1:
    if st == N:
        cnt += 1
        st -= arr[l1]
        l1 += 1
        l2 += 1
        st += arr[l2]
    elif st < N:
        l2 += 1
        st += arr[l2]
    else:
        st -= arr[l1]
        l1 += 1
        
print(cnt)