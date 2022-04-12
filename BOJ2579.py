#점화식
#N = n+n-1+n-3
#N = n+n-2
N = int(input())
data = []
data.append(0)
for i in range(N):
    data.append(int(input()))

dp = [0]*(N+1)

def f(n):
    if N <= 2:
        for j in range(1, N+1):
            dp[j] = dp[j - 1] + data[j]
        return dp[n]
    else:
        dp[1] = data[1]
        dp[2] = data[2] + dp[1]
        for i in range(3, N + 1):
            dp[i] = max(data[i] + data[i - 1] + dp[i - 3], data[i] + dp[i - 2])
        return dp[n]


print(f(N))
