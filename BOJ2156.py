N = int(input())
data = []
data.append(0)

for i in range(N):
    data.append(int(input()))

dp = [0] * (N+1)


def f(n):
    if n<=2:
        for i in range(1,N+1):
            dp[i] = dp[i-1] + data[i]
        return dp[n]

    else:
        dp[1] = data[1]
        dp[2] = data[1]+data[2]
        for i in range(3,N+1):
            dp[i] = max(data[i]+data[i-1]+dp[i-3], data[i]+ dp[i-2],dp[i-1])
        return dp[n]


print(f(N))
