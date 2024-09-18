from random import randint

def calc(no):
    num = []
    while no:
        num.append(no % 10)
        no //= 10
    x = 0
    for i in range(12):
        x += num[i] if i % 2 else 3 * num[i]
    x = 10 - x % 10
    return 0 if x == 10 else x

def isCorrect(no):
    if len(no) != 12:
        return False
    for i in no:
        if not (i >= '0' and i <= '9'):
            return False
    return True


filename = 'log-%d.txt' % randint(1000000, 9999999)
file = open(filename, 'a')
no = '0'
while True:
    no = input('请输入ISBN-13的前12位：\n')
    file.write('请输入ISBN-13的前12位：\n' + no + '\n')
    if not isCorrect(no):
        continue
    num = no + str(calc(int(no)))
    op = 'ISBN号码：' + num[0:3] + '-' + num[3:4] + '-' \
        + num[4:7] + '-' + num[7:12] + '-' + num[12:13] 
    print(op)
    file.write(op)
    break
file.close()