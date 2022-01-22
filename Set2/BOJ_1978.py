import sys

N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split(' ')))
prime = 0

for i in nums:
    cnt = 0
    if(i == 1):
        continue
    for j in range(2, i+1):
        if(i%j == 0):
            cnt += 1
    if(cnt == 1):
        prime += 1
print(prime)
