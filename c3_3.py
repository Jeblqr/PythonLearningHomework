from random import randint
grade = 0
num = eval(input('你想做几道题？'))
for i in range(1, num + 1):
    a = randint(10, 99)
    b = randint(10, 99)
    ans = eval(input('第%d道：%d+%d = ?' % (i, a, b)))
    if ans == a + b:
        print('答对了！加一分。')
        grade += 1
    else:
        print('答错了！不得分。正确答案是%d。' % (a + b))
print('你做了%d道题，共答对了%d道。' % (num, grade))