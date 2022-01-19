N, K = map(int, input().split())
arr = [i for i in range(1, N+1)]

human = []
cur = 0

for j in range(N):
    cur += K-1
    if cur >= len(arr):
        cur = cur % len(arr)
    human.append(str(arr.pop(cur)))
print("<", ", ".join(human)[:], ">", sep='')
