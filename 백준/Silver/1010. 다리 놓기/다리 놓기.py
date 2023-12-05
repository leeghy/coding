T = int(input())

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def permutation(n, r):
    result = 1
    for i in range(r):
        result *= n
        n -= 1
    return result


for i in range(T):
    N, M = map(int, input().split())
    print(permutation(M, N) // factorial(N))