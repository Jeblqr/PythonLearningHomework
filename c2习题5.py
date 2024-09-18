from random import randint
s = input('请输入一列数，以空格分隔：')
num = [eval(i) for i in s.split()]
num = [num.pop(randint(0, len(num) - 1)) for i in range(len(num))]
print('乱序结果：', *num)