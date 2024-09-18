import re
s = input()
pat = re.compile(r'</?[^>]+>')
print(pat.sub('', s))
#老师你给的sample里面引号是中文的
