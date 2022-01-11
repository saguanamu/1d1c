import sys
from collections import deque

T = int(sys.stdin.readline())

for _ in range(T):
    data = sys.stdin.readline().strip()
    n = int(sys.stdin.readline())
    arr_data = sys.stdin.readline()[1:-2].split(",")
    queue = deque()
    
    for each in arr_data:
        if each != '':
            queue.append(each)

    flag = 0
    reverse = 0

    for each in data:
        if each == 'R':
            if reverse == 0:
                reverse = 1
            else:
                reverse = 0
        else:
            if queue and queue[0] != '':
                if reverse == 0:
                    queue.popleft()
                else:
                    queue.pop()
            else:
                flag = 1
                break
    if flag == 1:
        print("errror")
    else:
        if reverse == 1:
            queue.reverse()
        print('[', end='')
        for j in range(len(queue)):
            if j == len(queue)-1:
                print(str(queue[j]), end='')
            else:
                print(queue[j], end=',')
        print(']')
