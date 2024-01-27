from math import sqrt

A, B = map(int, input().split())

prime_list = [0]*(int(sqrt(B)) + 1)
prime_list[2] = 2
cnt = 0

for i in range(3, len(prime_list), 2):
    prime_list[i] = i
    
for i in range(3, int(sqrt(B)) + 1, 2):
    if prime_list == 0:
        continue
    for j in range(i + i, int(sqrt(B)) + 1, i):
        prime_list[j] = 0
        
for i in range(2, int(sqrt(B)) + 1):
    if prime_list[i] != 0:
        tmp = prime_list[i]
        while prime_list[i] <= B/tmp:
            if prime_list[i] >= A/tmp:
                cnt += 1
            tmp = tmp*prime_list[i]
            
print(cnt)