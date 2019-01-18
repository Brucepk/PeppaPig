# coding:utf-8
import turtle as tu

'''
Author：pk哥
Date：2019/1/18
公众号：Python知识圈
代码解析详见公众号：Python知识圈。
如疑问或需转载，请联系微信号：dyw520520，备注来意，谢谢。
'''
tu.pensize(4)  # 设置画笔的大小
tu.colormode(255)  # 设置GBK颜色范围为0-255
tu.color((255, 155, 192), "pink")  # 设置画笔颜色和填充颜色(pink)
tu.setup(850, 500)  # 设置主窗口的大小为850*500
tu.speed(10)  # 设置画笔速度为10

# 画鼻子部分
tu.pu()  # 提笔
tu.goto(-100, 100)  # 画笔前往坐标(-100,100)
tu.pd()  # 下笔
tu.seth(-30)  # 笔的角度为-30°
tu.begin_fill()  # 外形填充的开始标志
a = 0.4
for i in range(120):
    if 0 <= i < 30 or 60 <= i < 90:
        a = a + 0.08
        tu.lt(3)  # 向左转3度
        tu.fd(a)  # 向前走a的步长
    else:
        a = a - 0.08
        tu.lt(3)
        tu.fd(a)
tu.end_fill()  # 依据轮廓填充
tu.pu()  # 提笔
tu.seth(90)  # 笔的角度为90度
tu.fd(25)  # 向前移动25
tu.seth(0)  # 转换画笔的角度为0
tu.fd(10)
tu.pd()
tu.pencolor(255, 155, 192)  # 设置画笔颜色
tu.seth(10)
tu.begin_fill()
tu.circle(5)  # 画一个半径为5的圆
tu.color(160, 82, 45)  # 设置画笔和填充颜色
tu.end_fill()
tu.pu()
tu.seth(0)
tu.fd(20)
tu.pd()
tu.pencolor(255, 155, 192)
tu.seth(10)
tu.begin_fill()
tu.circle(5)
tu.color(160, 82, 45)
tu.end_fill()

# 画头部
tu.color((255, 155, 192), "pink")
tu.pu()
tu.seth(90)
tu.fd(41)
tu.seth(0)
tu.fd(0)
tu.pd()
tu.begin_fill()
tu.seth(180)
tu.circle(300, -30)  # 顺时针画一个半径为300,圆心角为30°的园
tu.circle(100, -60)
tu.circle(80, -100)
tu.circle(150, -20)
tu.circle(60, -95)
tu.seth(161)
tu.circle(-300, 15)
tu.pu()
tu.goto(-100, 100)
tu.pd()
tu.seth(-30)
a = 0.4
for i in range(60):
    if 0 <= i < 30 or 60 <= i < 90:
        a = a + 0.08
        tu.lt(3)  # 向左转3度
        tu.fd(a)  # 向前走a的步长
    else:
        a = a - 0.08
        tu.lt(3)
        tu.fd(a)
tu.end_fill()

# 画耳朵
tu.color((255, 155, 192), "pink")
tu.pu()
tu.seth(90)
tu.fd(-7)
tu.seth(0)
tu.fd(70)
tu.pd()
tu.begin_fill()
tu.seth(100)
tu.circle(-50, 50)
tu.circle(-10, 120)
tu.circle(-50, 54)
tu.end_fill()
tu.pu()
tu.seth(90)
tu.fd(-12)
tu.seth(0)
tu.fd(30)
tu.pd()
tu.begin_fill()
tu.seth(100)
tu.circle(-50, 50)
tu.circle(-10, 120)
tu.circle(-50, 56)
tu.end_fill()

# 画眼睛
tu.color((255, 155, 192), "white")
tu.pu()
tu.seth(90)
tu.fd(-20)
tu.seth(0)
tu.fd(-95)
tu.pd()
tu.begin_fill()
tu.circle(15)
tu.end_fill()
tu.color("black")
tu.pu()
tu.seth(90)
tu.fd(12)
tu.seth(0)
tu.fd(-3)
tu.pd()
tu.begin_fill()
tu.circle(3)
tu.end_fill()
tu.color((255, 155, 192), "white")
tu.pu()
tu.seth(90)
tu.fd(-25)
tu.seth(0)
tu.fd(40)
tu.pd()
tu.begin_fill()
tu.circle(15)
tu.end_fill()
tu.color("black")
tu.pu()
tu.seth(90)
tu.fd(12)
tu.seth(0)
tu.fd(-3)
tu.pd()
tu.begin_fill()
tu.circle(3)
tu.end_fill()

# 画腮
tu.color((255, 155, 192))
tu.pu()
tu.seth(90)
tu.fd(-95)
tu.seth(0)
tu.fd(65)
tu.pd()
tu.begin_fill()
tu.circle(30)
tu.end_fill()

# 画嘴
tu.color(239, 69, 19)
tu.pu()
tu.seth(90)
tu.fd(15)
tu.seth(0)
tu.fd(-100)
tu.pd()
tu.seth(-80)
tu.circle(30, 40)
tu.circle(40, 80)

# 画身体
tu.color("red", (255, 99, 71))
tu.pu()
tu.seth(90)
tu.fd(-20)
tu.seth(0)
tu.fd(-78)
tu.pd()
tu.begin_fill()
tu.seth(-130)
tu.circle(100, 10)
tu.circle(300, 30)
tu.seth(0)
tu.fd(230)
tu.seth(90)
tu.circle(300, 30)
tu.circle(100, 3)
tu.color((255, 155, 192), (255, 100, 100))
tu.seth(-135)
tu.circle(-80, 63)
tu.circle(-150, 24)
tu.end_fill()
# 手
tu.color((255, 155, 192))
tu.pu()
tu.seth(90)
tu.fd(-40)
tu.seth(0)
tu.fd(-27)
tu.pd()
tu.seth(-160)
tu.circle(300, 15)
tu.pu()
tu.seth(90)
tu.fd(15)
tu.seth(0)
tu.fd(0)
tu.pd()
tu.seth(-10)
tu.circle(-20, 90)
tu.pu()
tu.seth(90)
tu.fd(30)
tu.seth(0)
tu.fd(237)
tu.pd()
tu.seth(-20)
tu.circle(-300, 15)
tu.pu()
tu.seth(90)
tu.fd(20)
tu.seth(0)
tu.fd(0)
tu.pd()
tu.seth(-170)
tu.circle(20, 90)

# 画脚
tu.pensize(10)
tu.color((240, 128, 128))
tu.pu()
tu.seth(90)
tu.fd(-75)
tu.seth(0)
tu.fd(-180)
tu.pd()
tu.seth(-90)
tu.fd(40)
tu.seth(-180)
tu.color("black")
tu.pensize(15)
tu.fd(20)
tu.pensize(10)
tu.color((240, 128, 128))
tu.pu()
tu.seth(90)
tu.fd(40)
tu.seth(0)
tu.fd(90)
tu.pd()
tu.seth(-90)
tu.fd(40)
tu.seth(-180)
tu.color("black")
tu.pensize(15)
tu.fd(20)

# 画尾巴
tu.pensize(4)
tu.color((255, 155, 192))
tu.pu()
tu.seth(90)
tu.fd(70)
tu.seth(0)
tu.fd(95)
tu.pd()
tu.seth(0)
tu.circle(70, 20)
tu.circle(10, 330)
tu.circle(70, 30)
