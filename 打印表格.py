def fun(i):
    print('%d\t%d\t%d\t' % (i, i ** 2, i ** 3))

def main():
    print("a\ta^2\ta^3\t")
    for i in range(1, 5):
        fun(i)

if __name__ == "__main__":
    main()