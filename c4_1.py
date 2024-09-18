def myFind(s, subs, times):
    count = 0
    for i in range(len(s) - len(subs) + 1):
        for j in range(len(subs)):
            if s[i + j] != subs[j]:
                count -= 1
                break
        count += 1
        if count == times:
            return i
    return -1

print(myFind('123004056007890', '00', 2))
print(myFind('AsAAssAAAssAAsAAAssAAAAsAAAssAAAAAssAAAaa', 'ss', 3))
print(myFind('123004056007890', '01', 2))