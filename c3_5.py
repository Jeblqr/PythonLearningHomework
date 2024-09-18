tempa, tempb = -1, -1
for i in range(1, 100001):
    snum = str(i)
    tempa, tempb = -1, -1
    for j in range(len(snum)):
        sa = snum[:j]
        sb = snum[j:]
        a = int(sa if sa != '' else 0)
        b = int(sb if sb != '' else 0)
        if (a + b) ** 2 == i:
            tempa = a
            tempb = b
            break
    if tempa != -1:
            print('%d=(%d+%d)**2'% (i, tempa, tempb))   

        