import sys

N = int(sys.stdin.readline())
arr = []

for i in range(N):
    [x, y] = map(int, sys.stdin.readline().split())
    reverse = [y, x]
    arr.append(reverse)

result = sorted(arr)

for i in range(N):
    print(result[i][1], result[i][0])
