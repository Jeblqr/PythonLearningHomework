
# 2020.4.14 by Xiao Chuan (cxiao@fudan.edu.cn)

# 作为库函数，此文件无需改动！！！

__W_WIDTH = 800   # 可自行调整窗口大小
__W_HEIGHT = 600  # 可自行调整窗口大小

import turtle
import time
__rootTurtle = turtle.TK.Tk()
__cv1 = turtle.TK.Canvas(__rootTurtle)
__cv2 = turtle.TK.Canvas(__rootTurtle)


def randdot():
    import random
    return "●" if random.randint(0,9)<3 else "□"

def randMatrix(rows, cols):
    return [[randdot() for i in range(cols)] for j in range(rows)]

__firstCanvas = True
def showMatrix(matrix,intervalseconds=0):
    global __firstCanvas,__cv1,__cv2,__rootTurtle,__W_WIDTH,__W_HEIGHT
    if __firstCanvas:
        __cv1 = turtle.TK.Canvas(__rootTurtle, width=__W_WIDTH, height=__W_HEIGHT)
        showMatrix0(matrix,__cv1,__cv2,intervalseconds)
    else:
        __cv2 = turtle.TK.Canvas(__rootTurtle, width=__W_WIDTH, height=__W_HEIGHT)
        showMatrix0(matrix,__cv2,__cv1,intervalseconds)
    __firstCanvas = not __firstCanvas    

        
def showMatrix0(matrix,cv,oldcv,intervalseconds):

    s = turtle.TurtleScreen(cv)

    p = turtle.RawTurtle(s)
    p.penup()
    p.speed(10)
    p.hideturtle()

    rows = len(matrix)
    cols = len(matrix[0])
    rowcenter = rows//2
    colcenter = cols//2
    s.clear()
    for row in range(rows):
        for col in range(cols):        
            p.goto((col-colcenter)*30 , (rowcenter-row)*30)
            p.write(matrix[row][col],font=('arial',20,'normal'))
    oldcv.destroy()
    cv.pack()
    if intervalseconds<=0:
        time.sleep(intervalseconds)
    
    

if __name__=="__main__":
    for i in range(10):
        showMatrix(randMatrix(5,5),0)
    
