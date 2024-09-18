import threading
import random
import os

hunger = 0
happiness = 0
healthiness = 0
hours = 0
status = ''
#presta = ''
sta = ['walk', 'play', 'feed', 'seedoctor', 'letalone', 'asleep', 'status']
staShow = ['我在散步', '我在玩耍', '我在吃饭', '我在看医生', '我醒着但很无聊', '我在睡觉']

def init():
    global hunger, happiness, healthiness, hours, status
    if not os.path.exists('log.txt'):
        open('log.txt', 'w')
    with open('log.txt', 'r') as f:
        s = f.readlines()
    if s == []:
        hunger = random.randint(0, 100)
        happiness = random.randint(0, 100)
        healthiness = random.randint(0, 100)
        hours = random.randint(0, 23)
        if 0 <= hours < 8:
            status = 'asleep'
        else:
            status = sta[random.randint(0, 4)]
        return True
    else:
        hunger = int(s[0].split()[1])
        happiness = int(s[1].split()[1])
        healthiness = int(s[2].split()[1])
        hours = int(s[3].split()[1])
        status = sta[int(s[4].split()[1])]
def save():
    with open('log.txt', 'w') as f:
        lines = 'hunger %d\nhappiness %d\nhealthiness %d\nhours %d\nstatus %d' \
            % (hunger, happiness, healthiness, hours, sta.index(status))
        f.write(lines)

def isAsleep():
    return  0 <= hours < 8

def sleep():
    global hunger
    hunger += 1

def wake():
    global hunger, happiness
    hunger += 2
    happiness -= 1

def walk():
    global hunger, healthiness
    hunger += 3
    healthiness += 1

def play():
    global hunger, happiness
    hunger += 3
    happiness += 2

def eat():
    global hunger, happiness
    happiness += 1
    hunger -= 5

def exam():
    global healthiness
    healthiness += 4

def wakeUp():
    global happiness
    happiness -= 4

def check():
    global hunger, happiness, healthiness
    if hunger < 20 or hunger > 80:
        healthiness -= 2
    if happiness < 20:
        healthiness -= 1
    normalize()

def normalize():
    global hunger, happiness, healthiness
    if healthiness < 0:
        healthiness = 0
    if healthiness > 100:
        healthiness = 100
    if hunger < 0:
        hunger = 0
    if hunger > 100:
        hunger = 100
    if happiness < 0:
        happiness = 0
    if happiness > 100:
        happiness = 100


def showStatus():
    print('当前时间： %d点' % hours)
    print('我当前的状态：%s......' % staShow[sta.index(status)])
    print('Happiness:     Sad %s Happy(%.3d)' % ('*' * (happiness * 50 // 100) + '-' * (50 - happiness * 50 // 100), happiness))
    print('Hungry:       Full %s Hungry(%.3d)' % ('*' * (hunger * 50 // 100) + '-' * (50 - hunger * 50 // 100), hunger))
    print('Health:       Sick %s Healthy(%.3d)' % ('*' * (healthiness * 50 // 100) + '-' * (50 - healthiness * 50 // 100), healthiness))
    print()

def fun_timer():
    #sta = ['walk', 'play', 'feed', \
    #    'seedoctor', 'letalone', 'asleep']
    global timer, hours, status, presta
    global healthiness, happiness, hunger
    hours += 1
    if hours == 24:
        hours = 0
    if hours == 0:
        #if status != sta[5]:        #用于睡觉醒后回退睡前状态
        #    presta = status         #题目没有明说需不需要这样，但是看演示程序是不需要的
        status = 'asleep'
    if hours == 8:
        #if presta:
        #    status = presta
        #    presta = ''
        #else:
        #    status = 'letalone'
        if status == 'asleep':
            status = 'letalone'
    if status == sta[0]:
        walk()
    elif status == sta[1]:
        play()
    elif status == sta[2]:
        eat()
    elif status == sta[3]:
        exam()
    elif status == sta[4]:
        wake()
    elif status == sta[5]:
        sleep()
    check()
    try:
        timer = threading.Timer(2.0, fun_timer)
        timer.start()
    except Exception:
        print()

def welcome():
    print('我的名字叫Tommy，一只可爱的猫咪....')
    print('你可以和我一起散步，玩耍，你也需要给我好吃的东西，带我去看病，也可以让我发呆....')
    print('Commands:\n1. walk: 散步\n2. play: 玩耍\n3. feed: 喂我\n4. seedoctor: 看医生\n5. letalone: 让我独自一人\n6. status: 查看我的状态\n7. bye: 不想看到我')
    print()

def bye():
    print('记得来找我！Bye.....')
    save()

def operate():
    global status
    s = input('你想：')
    if s == 'bye':
        bye()
        return True
    if not s in sta:
        print('我不懂你在说什么')
        print()
        return
    if s == 'status':
        showStatus()
        return
    if status == 'asleep':
        if s == 'letalone':
            print('我在睡觉......')
            print()
            return
        else:
            yes = input('你确认要吵醒我吗？我在睡觉，你要是坚持吵醒我，我会不高兴的！（y表示是/其他表示不是）')
            if yes == 'y':
                wakeUp()
            else:
                print()
                return
    status = s
    print('%s......' % staShow[sta.index(status)])
    print()

def main():
    welcome()
    init()
    fun_timer()
    while True:
        if operate():
            return

if __name__ == '__main__':
    main()
