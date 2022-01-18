import sys

N = int(sys.stdin.readline())
words = []
for i in range(N):
    words.append(sys.stdin.readline().strip())
    
words_set = set(words)
words = list(words_set) # 집합 -> 중복 제거
words.sort() # 정렬
words.sort(key = len) # 크기 순
for i in words:
    print(i)
