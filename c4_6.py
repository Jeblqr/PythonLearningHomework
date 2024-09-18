import re
prime = [1, 2, 3, 5, 7, 11, 13, 17, 19]
pat = re.compile(r'^[01]{1,9}$(?!\x20)')
s = input('请输入十位以下的火星码：')
while pat.match(s) == None:
    s = input('请输入十位以下的火星码：')
num = 0
for i in range(0, len(s)):
    temp = int(s[i])
    for j in range(0, len(s) - i): #优化可以提前把prime做个累乘预处理，写死在代码里
        temp *= prime[j]           #但是懒得了
    num += temp   
print('该火星码对应的十进制数为：%d' % num)
