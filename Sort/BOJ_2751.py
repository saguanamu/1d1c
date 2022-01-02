import sys

""" quicksort 시간 초과
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
"""
N = int(input())
M = [int(sys.stdin.readline())
     for i in range(N)]

#for i in range(N):
#    M.append(int(input()))

#n = quicksort(M)
for i in sorted(M):
    print(i)

# bubble sort
#for i in range(len(M)):
#    for j in range(len(M)):
#        if M[i] > M[j]:
#            M[i], M[j] = M[j], M[i]

#for i in M:
#    print(i)

