N = int(input())

dict = {}

k = 0
for i in range(1,N+1):
    while True:
        k += 1
        temp = str(k)
        t_true = True
        for c in temp:
            if c == '1' or c == '2' or c == '4':
                continue
            else:
                t_true = False

        if t_true == True:
            break
    dict[i] = str(k)

print(dict[N])