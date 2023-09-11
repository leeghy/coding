def factorial(number):
    result = 1
    for i in range(1, number + 1):
        result *= i
    return result


N, K = map(int, input().split())

ans = factorial(N) // (factorial(K) * factorial(N - K))

print(int(ans % 10007))
