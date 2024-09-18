from random import randint
a = randint(0, 9)
b = randint(0, 9)
c = randint(0, 9)
p = dict()
pp = dict()
p[a] = p.get(a, 0) + 1
p[b] = p.get(b, 0) + 1
p[c] = p.get(c, 0) + 1
print("中奖号码是%s" % str(a) + str(b) + str(c))
no = input('请输入你的彩票号码（三位数）：')
x = int(no[0])
y = int(no[1])
z = int(no[2])
pp[x] = pp.get(x, 0) + 1
pp[y] = pp.get(y, 0) + 1
pp[z] = pp.get(z, 0) + 1
count = 0
if x == a and y == b and z == c:
    print("完全匹配：你获得10,000元。")
else:
    for i in pp:
        count += min(pp.get(i, 0), p.get(i, 0))
    if count == 3:
        print("匹配所有数字：你赢得3,000元。")
    elif count == 1:
        print("匹配一个数字：你赢得1,000元。")
    else:
        print("很抱歉，没有中奖。")

