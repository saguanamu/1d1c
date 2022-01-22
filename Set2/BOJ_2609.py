import sys, math

m, n = map(int, sys.stdin.readline().split())


# 유클리드 호제
def gcd(m, n):
    while n > 0:
        m, n = n, m % n
    return m

def lcm(m, n):
    return m * n

print(gcd(m, n))
print(lcm(m, n))


# math
#print(math.gcd(m, n))
#print(math.lcm(m, n))
