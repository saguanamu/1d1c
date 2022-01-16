import sys
# 메모리 초과 오류
N = int(sys.stdin.readline())
M = [0] * 10001

for i in range(N):
    num_value = int(sys.stdin.readline())
    M[num_value] = M[num_value] + 1

for i in range(10001):
    if M[i] != 0:
        for j in range(M[i]):
            print(i)
