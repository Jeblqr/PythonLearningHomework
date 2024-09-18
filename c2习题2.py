def fun(xList, k):
    count = 1
    for i in range(len(xList)):
        if xList[i] == k:
            xList[i] = count * k
            count += 1

x=[2, 3, 1, 2, 3, 2, 5, 3, 3, 2]

fun(x, 3)  #调用函数，把x内值为3的元素依次更改为3、6、9、....
print(*x)  #将显示 2  3  1  2  6  2  5  9  12  2
fun(x, 2)  #调用函数，把x内值为2的元素依次更改为2、4、6、....
print(*x)  #将显示 2  3  1  4  6  6  5  9  12  8sS
fun(x, 6)  #调用函数，把x内值为6的元素依次更改为6、12、18、....
print(*x)  #将显示 2  3  1  4  6  12  5  9  12  8