from random import randint
a, b = map(eval, input('请输入两个数，以空格分隔：').split())
print('产生2000000个%d~%d之间的随机偶数... 统计结果如下：' % (a, b))
print('数值                次数                百分比')
count = dict()
la = a // 2
if a % 2 != 0:
    la += 1
lb = b // 2
for i in range(2000000):
    rnd = randint(la , lb)
    rnd = rnd * 2
    count[rnd] = count.get(rnd, 0) + 1
c = sorted(count)
for i in c:
    print("%-20d%-20d%.2f%%" % (i, count[i], count[i] / 2000000 * 100))