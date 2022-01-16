import sys
from collections import deque

N = int(sys.stdin.readline())
d = deque()

for i in range(N):
    data = sys.stdin.readline().split()
    if data[0] == "push_front":
        d.appendleft(data[1])

    elif data[0] == "push_back":
        d.append(data[1])
        
    elif data[0] == "pop_front":
        
        if len(d) == 0:
            print(-1)
        else:
            print(d[0])
            d.popleft()

    elif data[0] == "pop_back":
        if len(d) == 0:
            print(-1)
        else:
            print(d[-1])
            d.pop()
            
    elif data[0] == "size":
        print(len(d))
        
    elif data[0] == "empty":
        if len(d) == 0:
            print(1)
        else:
            print(0)
            
    elif data[0] == "front":
        if len(d) == 0:
            print(-1)
        else:
            print(d[0])
            
    elif data[0] == "back":
        if len(d) == 0:
            print(-1)
        else:
            print(d[-1])
        
