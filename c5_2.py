from random import randint
win = 0
times = 0
def play():
    global win, times
    ti = 1
    sum = 0
    ia = randint(1, 6)
    ib = randint(1, 6)
    print('(%d, %d) ' % (ia, ib), end = '')
    if ia + ib in [7, 11]:
        print('You Win. 掷骰子1次！', end = '')
        win += 1
        times += 1
        return
    if ia + ib in [2, 3, 12]:
        print('You Lose. 掷骰子1次！', end = '')
        times += 1
        return
    while True:
        a = randint(1, 6)
        b = randint(1, 6)
        ti += 1
        print('(%d, %d) ' % (a, b), end = '')
        if a + b == 7:
            print('You Lose. 掷骰子%d次！' % ti, end = '')
            break
        if a + b == ia + ib:
            print('You Win. 掷骰子%d次！' % ti, end = '')
            win += 1
            break
    times += ti
n = eval(input('请输入要玩的局数：'))
for i in range(1, n + 1):
    print('第%d局：' % i, end = '')
    play()
    print()
print('胜率：%.2f，平均每局掷骰子%d次。' % (win / n, times / n))
