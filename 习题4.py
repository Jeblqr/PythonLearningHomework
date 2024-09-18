from math import sqrt

def calc(a, b, c):
    p = (a + b + c) / 2
    return  sqrt(p * (p - a) * (p - b) * (p - c))

def main():
    a, b, c = eval(input('''请输入三条边长，以","分隔：'''))
    print('此三角形的面积是%.2f。' % calc(a, b, c))

if __name__ == '__main__':
    main()