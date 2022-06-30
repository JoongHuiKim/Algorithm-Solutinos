sticker = [1, 3, 2, 5, 4]
list_answer = []
answer = 0
dp = [0] * len(sticker)

if len(sticker) == 1:
    answer = sticker[0]
else:
    dp[0] = sticker[0]
    dp[1] = dp[0]

    for i in range(2,len(sticker)-1):
        dp[i] = max(dp[i-1],dp[i-2] + sticker[i])

    list_answer.append(max(dp))

    dp = [0] * len(sticker)

    dp[0] = 0
    dp[1] = sticker[1]

    for j in range(2, len(sticker)):
        dp[j] = max(dp[j - 1], dp[j - 2] + sticker[j])

    list_answer.append(max(dp))
    answer = max(list_answer)

print(answer)
