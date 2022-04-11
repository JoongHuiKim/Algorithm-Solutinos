N = int(input())
dp = [0]*(1001)

def f(n):
    dp[1] = 1
    dp[2] = 2

    for j in range(3, n + 1):
        dp[j] = (dp[j - 2] + dp[j - 1]) % 10007

    return dp[N]

print(f(N))