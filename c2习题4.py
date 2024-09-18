import random
x = list(range(10))
random.shuffle(x)
print(x)
odd = []
even = []
for i in range(10):
    if x[i] % 2 == 0:
        even.append(x[i])
    else:
        odd.append(x[i])
random.shuffle(even)
counteven = 0
countodd = 0
for i in range(10):
    if x[i] % 2 == 0:
        x[i] = even[counteven]
        counteven += 1
    else:
        x[i] = odd[countodd]
        countodd += 1
print(x)
