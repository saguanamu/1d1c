import sys

priority = []

tc = int(sys.stdin.readline())
for i in range(tc):
    N, M = map(int, input().split())
    priority = list(map(int, input().split()))
    cur = [0 for i in range(N)]
    cur[M] = 1
    cnt = 0

    while True:
        if priority[0] == max(priority):
            cnt += 1
            if cur[0] == 1:
                print(cnt)
                break
            else:
                del priority[0]
                del cur[0]
        else:
            priority.append(priority[0])
            del priority[0]
            cur.append(cur[0])
            del cur[0]
    
