W = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2, 1]
chq = ['1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2']

def calcchq(sno):
    S = 0
    for i in range(0, 17):
        num = int(sno[i])
        #print(num)
        S += num * W[i]
        S %= 11
    #print(chq[S])
    return chq[S]


no = eval(input('请输入身份证号：'))
sno = str(no)
if len(sno) == 17:
    print('完整的身份证号：%s' % (sno + str(calcchq(sno))))
else:
    if (str(calcchq(sno[0:17])) == sno[17]):
        print('该身份证号是正确的')
    else:
        print('该身份证号是错误的')