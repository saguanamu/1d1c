import sys

_ = sys.stdin.readline()
N = map(int, sys.stdin.readline().split())
_ = sys.stdin.readline()
M = map(int, sys.stdin.readline().split())

hashmap = {}

for i in N:
    if i in hashmap:
        hashmap[i] += 1
    else:
        hashmap[i] = 1

print(' '.join(str(hashmap[j]) if j in hashmap else '0' for j in M))
