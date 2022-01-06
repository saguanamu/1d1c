import sys

N = int(sys.stdin.readline())
strlist = []

for i in range(N):
    string = sys.stdin.readline().strip()
    strlist.append(string)

# 중복 제거
list_set = set(strlist )
strlist = list(list_set)

strlist .sort(key=lambda x:(len(x), x))

for i in range(len(strlist)):
    print(strlist[i])
