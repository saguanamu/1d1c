import sys
from itertools import combinations as combi

N = int(sys.stdin.readline())
S = [i for i in range(N)]
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
result = int(1e9) # 1*109

for r1 in combi(S, N//2):
    start, link = 0, 0
    r2 = list(set(S) - set(r1))

    for r in combi(r1, 2):
        start += matrix[r[0]][r[1]]
        start += matrix[r[1]][r[0]]

    for r in combi(r2, 2):
        link += matrix[r[0]][r[1]]
        link += matrix[r[1]][r[0]]
    result = min(result, abs(start-link))
print(result)
