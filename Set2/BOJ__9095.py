import sys

T = int(sys.stdin.readline())

def sol(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        return sol(n-1) + sol(n-2) + sol(n-3)

for i in range(T):
    n = int(sys.stdin.readline())
    print(sol(n))
