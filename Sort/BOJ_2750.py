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
M = []
for i in range(N):
    M.append(int(input()))

# bubble sort
#for i in range(len(M)):
#    for j in range(len(M)):
#        if M[i] < M[j]:
#            M[i], M[j] = M[j], M[i]


# 리스트 sort 이용
#M2 = M.sort()
#for N in M:
#    print(N)


n = quicksort(M)
for i in n:
    print(i)

