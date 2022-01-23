import sys

def adjacent(x):
    for i in range(x):
        # 같은 열 or 대각선 위치
        if row[x] == row[i] or abs(row[i] - row[x]) == x-i:
            return False
        return True

def dfs(x):
    global result

    if x == N:
        result += 1
        return
    else:
        for i in range(N):
            row[x] = i
            if adjacent(x):
                dfs(x+1)

N = int(sys.stdin.readline())
result = 0
row = [0] * N
dfs(0)
print(result)
