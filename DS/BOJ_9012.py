import sys

N = int(sys.stdin.readline())

for i in range(N):
    check = 0
    data = sys.stdin.readline().rstrip()
    for j in data:
        if j == '(':
            check+=1
        else:
            check-=1
        if check == -1:
            break
    if(check == 0):
        answer = "YES"
    else:
        answer = "NO"
    print(answer)
        


    
