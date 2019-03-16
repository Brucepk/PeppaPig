## 本代码文章首发于公众号「Python知识圈」，如需转载，请通过公众号联系作者pk哥，谢谢

![公众号](https://github.com/Brucepk/pk.github.io/blob/master/gzh.jpg)

也可以通过微信联系我。

![微信](https://github.com/Brucepk/pk.github.io/blob/master/wx.jpg)

昨晚和今天，朋友圈被一则走心的广告刷屏了。很多伙伴直呼：看哭了。当爷爷电话里听到「不回来啊」的打击是很沉重的，一位父亲想念自己的儿子和孙子，总想把最好的给他们。

如果你的孩子问你要佩奇，你除了像视频中的爷爷那样独具匠心的做一个出来，你也可以去商店买一个，你还可以用 Python 画一个出来。

> 动态效果图见公众号


今天画佩奇的库是 turtle，之前我用 turtle 这个库画过五星红旗 [turtle 画五星红旗](https://dwz.cn/GLhIHCiQ)

> 动态效果图见公众号


之前我也用 turtle 库一行代码画出了美丽的螺旋：[turtle 画美丽的螺旋](https://dwz.cn/e0FZSWix)

> 动态效果图见公众号

#### 环境
语言：Python3
编辑器：Pycharm

turtle 库：它是 Python 的内置库，直接导入即可。
```
import turtle
```
#### turtle 库基本用法

绘制图形前先掌握下 turtle 库绘图的一些基本用法。
```
turtle.begin_fill()：准备开始填充图形。
turtle.goto(x, y)：将画笔移到坐标的位置。
turtle.forward(n)：向当前画笔方向移动 n 像素长。
turtle.left(m)：逆时针移动 m°
turtle.right(m)：顺时针移动 m°
turtle.end_fill()：图形填充完成。
```

#### 代码分析
首先我们设置好初始信息，包括画笔的大小，画笔颜色和填充颜色，主窗口的大小和画笔速度。

再画鼻子部分，代码较多，以下是部分代码，全部代码在公众号回复「佩奇」获取。
> 代码见公众号或者 code 部分

其他部分就不一一列举了，方法都是类似的，掌握了 turtle 库绘图的一些基本用法后，再自己慢慢调试基本就可以了。

全部源码在 code 部分。

最后，祝大家猪年暴富！

