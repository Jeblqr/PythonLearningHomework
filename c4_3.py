c = input('请输入中心字符：')
x = eval(input('请输入层数：'))
for i in range(x):
    for j in range(2 * x - 1):
        if not j in range(x - i - 1, x + i):
           print(' ', end = '')
           continue
        print(chr((ord(c) - x + j + 1 - ord('A')) % 26 \
                  + ord('A')), end = '')
    print()


