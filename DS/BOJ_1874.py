import sys

n = int(sys.stdin.readline())
stack = []
answer = []
flag = 0
current = 1

for i in range(n):
    data = int(sys.stdin.readline())
    while current <= data:
        stack.append(current)
        answer.append('+')
        current += 1
    if stack[-1] == data:
        stack.pop()
        answer.append('-')
    else:
        print('NO')
        flag = 1
        break
if flag == 0:
    for i in answer:
        print(i)
