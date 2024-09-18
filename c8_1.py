from random import shuffle

suits = '♥♠♦♣'
no = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
keys = [14, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
cards = [i for i in range(52)]
count1 = 0
count2 = 0

def judge(a, b):
    if a == 12:
        return b == 0
    if a == 0:
        return False
    return a + 1 == b

def take(ele):
    return keys[ele]

def check(d, cards):
    c = [[] for i in range(4)]
    count = 0
    print('      %c:  ' % d, end = '')
    for card in cards:
        c[card // 13].append(card % 13)
    for f in range(4):
        c[f].sort(key = take)
    for f in range(4):
        print(suits[f], end = ' ')
        for i in c[f]:
            print(no[i], end = ' ')
    print()
    for f in range(4):
        i = 0
        while i < len(c[f]) - 4:
            co = 1
            for j in range(i + 1, len(c[f])):
                if judge(c[f][j - 1], c[f][j]):
                    co += 1
                else:
                    break
                if co == 5:
                    count += 1
                    print(i)
                    i = j
                    break
            i += 1
    return count


while True:
    try:
        times = eval(input('请输入发牌总次数：'))
    except:
        pass
    else:
        break

for times_ in range(times):
    print('\n第%d次发牌>>>' % (times_ + 1))
    shuffle(cards)
    co = 0
    co += check('E', cards[0:13])
    co += check('S', cards[13:26])
    co += check('W', cards[26:39])
    co += check('N', cards[39:52])
    if co == 0:
        print('未出现同花顺...')
    else:
        count1 += co
        count2 += 1
        print('出现%d个同花顺！！！累计已出现%d个同花顺。' % (co, count1))

print()
print('''出现同花顺的个数：%d\n出现同花顺的发牌次数: %d\n发牌总次数: %d\n出现同花顺的发牌概率: %f''' \
      % (count1, count2, times, count2 / times))