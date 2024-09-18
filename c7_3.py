from math import sqrt

isPrime = []

def op(num, x, y):
    return str(num) + ' = ' + str(x) + ' + ' + str(y)

def calc(num):
    for i in range(int(num / 2), num):
        if isPrime[i] and isPrime[num - i]:
            return [num - i, i]
    return [0, 0]

def generate(filename, min, max):
    with open(filename, 'a') as file:
        for i in range(min, max + 1, 2):
            file.write(op(i, *calc(i)) + '\n')

def prime(max):
    global isPrime 
    max = int(max)
    isPrime = [True for i in range(max + 1)]
    isPrime[0] = isPrime[1] = False
    max_ = int(sqrt(max))
    for i in range(2, max_):
        if isPrime[i]:
            for j in range(2 * i, max + 1, i):
                isPrime[j] = False

prime(100000)
generate('Goldbach01.txt', 4, 9999)
for i in range(1, 11):
    generate('Goldbach%.2d.txt' % i, 10000 * i, \
             10000 * i + 9999)





