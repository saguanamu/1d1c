import sys
N = int(sys.stdin.readline())

num = list(map(int, input().split()))
num_sort = sorted(list(set(num)))
dic = {num_sort[i] : i for i in range(len(num_sort))}

for i in num:
    print(dic[i], end = ' ')
