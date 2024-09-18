from random import randint
import picture
#这么长截图复制不下啊

def prt(step, x, y, n, status, mat):
    for i in range(n):
        for j in range(n):
            print(mat[i][j], end = '')
        print()
    print('Steps %d; Y=%d, X=%d, N=%d; Status: %s' % (step, y, x, n, status))

def simulate(n):
    times = 0
    sta = 'IN'
    x = n // 2
    y = n // 2
    mat = [['.' for j in range(n)] for i in range(n)]
    mat[x][y] = 'O'
    prt(0, x, y, n, sta, mat)
    while sta == 'IN':
        times += 1
        dirc = randint(0, 3)
        d = ''
        if dirc == 0:
            x -= 1
            d = '⌃'
        elif dirc == 1:
            x += 1
            d = '⌄'
        elif dirc == 2:
            y -= 1
            d = '‹'
        elif dirc == 3:
            y += 1
            d = '›'
        if x == 0 or y == 0 or x == n - 1 or y == n - 1:
            sta = 'OUT'
        mat[x][y] = d
        prt(times, x, y, n, sta, mat)
        picture.showMatrix(mat)
        mat[x][y] = 'O'
    return times


n, k = eval(input())
sta = 0
for i in range(1, k + 1):
    print('N=%d时开始第%d次模拟...' % (n, i,))
    times = simulate(n)
    sta += times
    print('N=%d时第%d次模拟结束，共%d步走出。' % (n, i, times))
print('N=%d时平均' % n, end = '')
print(sta / k, end = '')
print('步走出！！！') 