import sys
from collections import Counter

N = int(sys.stdin.readline())
M = []

for _ in range(N):
    M.append(int(sys.stdin.readline()))

print(round(sum(M)/N)) # 산술평균

# 중앙값
M.sort()
print(M[N//2])

# 최빈값
cnt_M = Counter(M).most_common(2)
if len(cnt_M) > 1 and cnt_M[0][1] == cnt_M[1][1]:
    print(cnt_M[1][0])
else:
    print(cnt_M[0][0])
    
print(max(M)-min(M)) # 최댓값 - 최솟값
