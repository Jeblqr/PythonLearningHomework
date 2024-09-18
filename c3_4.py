n, m = map(eval, input('请输入n和m：').split(','))
for i in range(1, n + 1):
    count = 0
    for j in range (1, 2 * n):
        if j <= n:
            if j > n - i:
                count += 1
                s = '%' + str(m) + 'd'
                print(s % count, end = '')
            else:
                print(m * ' ', end = '')
        else: 
            if j < n + i:
                count -= 1
                s = '%' + str(m) + 'd'
                print(s % count, end = '')
            else:
                print(m * ' ', end = '')
    print()
for i in range(n - 1, 0, -1):
    count = 0
    for j in range (1, 2 * n):
        if j <= n:
            if j > n - i:
                count += 1
                s = '%' + str(m) + 'd'
                print(s % count, end = '')
            else:
                print(m * ' ', end = '')
        else: 
            if j < n + i:
                count -= 1
                s = '%' + str(m) + 'd'
                print(s % count, end = '')
            else:
                print(m * ' ', end = '')
    print()
