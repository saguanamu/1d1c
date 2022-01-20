combi = [0 for i in range(13)]

def dfs(start, depth):
    if depth == 6:
        for i in range(6):
            print(combi[i], end=' ')
        print()
        return
    for i in range(start, len(lotto)):
        combi[depth] = lotto[i]
        dfs(i+1, depth+1)
        
while True:
    lotto = list(map(int, input().split()))
    if lotto[0] == 0:
        break
    lotto = lotto[1:]
    dfs(0, 0)
    print()
