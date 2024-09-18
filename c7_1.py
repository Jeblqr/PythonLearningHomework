from tkinter.filedialog import asksaveasfilename
sum = 0
print('请选择一个分数文件...')
fn = asksaveasfilename()
print('您选择的文件是', fn)
f = open(fn, 'r')
s = f.readlines()
f.close()
f = open(fn, 'w')
num = []
count = 0
for line in s:
    li = line.split()
    if li:
        for j in li:
            f.write(j)
            f.write(' ')
        num += li
        count += len(li)
        f.write('\n')
    for i in li:
        sum += int(i)
print('您的文件包括下列分数：', end = '')
print(*num, sep = ',')
if count != 0:
    f.write('共有%d个分数\n总分数是%d\n平均分是%.2f' \
            % (count, sum, sum / count))
else:
    f.write('共有%d个分数\n总分数是%d\n平均分是%.2f' \
            % (count, sum, 0))
print('统计完毕，请查看原文件 %s' % fn)
f.close()
