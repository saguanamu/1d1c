import sys

def quicksort(list):
    if len(list) <= 1:
        return list
    pivot = list[0]
    left = []
    right = []
    for i in list[1:]:
        if i < pivot:
            left.append(i)
        else:
            right.append(i)
    return quicksort(left) + [pivot] + quicksort(right)

N = int(input())
M = [int(sys.stdin.readline()) for i in range(N)]

M2 = quicksort(M)
for i in M2:
    print(i)
