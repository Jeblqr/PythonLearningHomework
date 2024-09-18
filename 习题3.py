def nextYear(init):
    return init + 365*24*60*60 // 7 + 365*24*60*60 // 45 - 365*24*60*60 // 13 - 365*24*60*60 // 79

def main():
    amount = 3120324986
    for i in range(1, 6):
        amount = nextYear(amount)
        print(amount)

if __name__ == '__main__':
    main()