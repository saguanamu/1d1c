import sys

N = int(sys.stdin.readline())
arr = []
for i in range(N):
    data = int(sys.stdin.readline())
    arr.append(data)

arr.sort()
for j in range(N):
    print(arr[j])
