import sys

N = int(sys.stdin.readline())
stack = []

for i in range(N):
    data = sys.stdin.readline().split()
    if data[0] == "push":
        stack.append(data[1])
    elif data[0] == "top":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
    elif data[0] == "size":
        print(len(stack))
    elif data[0] == "empty":
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif data[0] == "pop":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
        
