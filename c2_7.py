students = {"Zebra":["physics","chemistry","biology"],
        "Lark":["physics","politics","history"],
        "Wendy":["geography","politics","history"],
        "Martin":["chemistry","biology","history"],
        "Stan":["chemistry","geography","history"]
        }
count = dict()
for i in students:
    c = students[i]
    for j in c:
        if count.get(j, 0) == 0:
            count[j] = []
        count[j].append(i)
s = sorted(count)
for i in count:
    count[i] = sorted(count[i])
for i in s:
    print('%s: ' % i, end = '')
    for j in range(len(count[i]) - 1):
        print("%s、" % count[i][j], end = '')
    print(count[i][len(count[i]) - 1])
