import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split(' ')))
arr.sort()

M = int(sys.stdin.readline())
arr2= list(map(int, sys.stdin.readline().split(' ')))

def binary(target):
    l = 0
    r = N-1

    while l <= r:
        mid = (l+r) // 2
        if arr[mid] == target:
            return True

        if target < arr[mid]:
            r = mid - 1
        elif target > arr[mid]:
            l = mid + 1

for i in range(M):
    if binary(arr2[i]):
        print(1, end=' ')
    else:
        print(0, end=' ')


