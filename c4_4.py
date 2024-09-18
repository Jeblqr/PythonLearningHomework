from tkinter.filedialog import asksaveasfilename
import re
print('请选择一个文本文件...')
s = asksaveasfilename()
print('您选择的文件是 %s' % s)
with open(s, 'r') as file:
    st = file.read()
origin = input('输入要被替换的旧文本：')
sub = input('输入用于替换的新文本：')
###make 
o = ''
for i in origin:
    o += '[%c%c]' % (i.lower(), i.upper()) 
rex = re.compile(o)
m = rex.subn(sub, st)
with open(s, 'w') as file:
    file.write(m[0])
print('完成！共完成%d处替换。' % m[1])
