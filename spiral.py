import turtle

turtle.color('purple') #设置画笔颜色
turtle.pensize(2)      #设置画笔宽度
turtle.speed(5)        #设置画笔移动速度
t=turtle.Screen()

def draw(turtle, length):
    if length>0:      #边长大于0递归，画到最中心停止
        turtle.forward(length)
        turtle.left(90)        #每次画线后，画笔左转90度
        draw(turtle,length-4)  #利用递归再次画线，设置离上一圈的画线距离

draw(turtle,200)        #设置第一圈的边长
t.exitonclick()         #使turtle对象进入等待模式，点击清理退出运行
