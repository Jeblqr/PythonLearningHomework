grade = []
for i in range(7):
    grade.append(eval(input('评委%s给出的成绩：' % chr(i + ord('A')))))
grade.sort()
print("去掉一个最高分：%d" % grade[6])
print("去掉一个最高分：%d" % grade[0])
grade.pop(0)
grade.pop(5)
print("最终得分：%.1f" % (sum(grade) / 5))