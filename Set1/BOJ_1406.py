import sys

strdata = list(sys.stdin.readline().rstrip())
N = int(sys.stdin.readline())
cur = []

for i in range(N):
    data = list(sys.stdin.readline().split())

    if data[0] == 'L':
        if strdata:
            cur.append(strdata.pop())

    elif data[0] == 'D':
        if cur:
            strdata.append(cur.pop())

    elif data[0] == 'B':
        if strdata:
            strdata.pop()

    elif data[0] == 'P':
        strdata.append(data[1])

strdata.extend(reversed(cur))
print(''.join(strdata))
        
