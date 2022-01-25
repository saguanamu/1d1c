import sys
from math import gcd

N = int(sys.stdin.readline())
start = int(sys.stdin.readline())
arr = []

for i in range(N-1):
    num = int(sys.stdin.readline())
    arr.append(num - start)
    start = num

gcd_num = arr[0]
for j in range(1, len(arr)):
    gcd_num = gcd(gcd_num, arr[j])

result = 0
for each in arr:
    result += each // gcd_num-1
print(result)
