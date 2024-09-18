a = ['', '一', '二', '三', '四', '五', '六', '七', '八', '九', '十']
def translator(num):
    if num < 10:
        return a[num]
    return a[num // 10] + a[10] + a[num % 10] #ppt示例里的一十六是不是多少有点问题

s = input('请输入0~100之间的任意一列整数：')
num = [eval(i) for i in s.split(',')]
num_ = []
for i in num:
    num_.append(translator(i))
print('该列数的中文表示：', end = '')
print(*num_, sep=',')