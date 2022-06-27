#m	n	puddles	return
#4	3	[[2, 2]]	4


m = 3#열
n = 3  #행
puddles = [[1, 3], [3, 1]]
answer = 0

matrix = [[0]*(m+1) for _ in range(n+1)]

matrix[1][1] = 1

for i in range(1,n+1):
    for j in range(1,m+1):
        if i == 1 and j == 1:
            continue
        else:
            if len(puddles) > 0:
                if [j,i] in puddles:
                    matrix[i][j] = 0
                else:
                    matrix[i][j] = matrix[i][j - 1] + matrix[i - 1][j]
            else:
                matrix[i][j] = matrix[i][j - 1] + matrix[i - 1][j]



print(matrix[n][m]%1000000007)