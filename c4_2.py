s = input()
s = s + s[::-1]

for i in range(int(len(s) / 2) + 1):
    index = 0
    for j in range(len(s) + 2):
        if j == len(s) / 2 - i or j == len(s) / 2 + 1 + i:
            print(' ', end = '')
            continue
        print(s[index], end = '')
        index += 1
    print()

for i in range(int(len(s) / 2)):
    index = 0
    for j in range(len(s) + 2):
        if j == i + 1 or j == len(s) - i:
            print(' ', end = '')
            continue
        print(s[index], end = '')
        index += 1
    print()

