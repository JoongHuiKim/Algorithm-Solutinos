def solution(data,N):
    if N == 1:
        return data[0][0]

    for i in range(1, N):
        for j in range(i + 1):
            if j == 0:
                data[i][j] = data[i - 1][j] + data[i][j]
            elif j == i:
                data[i][j] = data[i - 1][len(data[i - 1]) - 1] + data[i][j]
            else:
                data[i][j] = max(data[i - 1][j - 1] + data[i][j], data[i - 1][j] + data[i][j])

    return max(data[N - 1])

data = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
N = len(data)

print(solution(data,N))
