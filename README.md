# turtle绘制螺旋结构

利用递归思想，使用turtle模块绘制螺旋结构，结果如图：

![spiral](/Users/wangqing/Desktop/研一上学期/计算机基础/turtle绘图作业/spiral.png)

* 递归螺旋：开始我是按下面这样画一圈一循环写的，但后来看示例，因为类似正方形，所以画笔每转一次一循环就可以了~作了修改

**`def draw(turtle, length):**`**

    if length>0:      #边长大于0递归，画到最中心停止
        turtle.forward(length)
        turtle.left(90)
        turtle.forward(length)
        turtle.left(90)
        draw(turtle,length-4)
* exitonclick()：作用是使turtle对象进入等待模式，点击可以清理并退出运行。  



参考资料：  

* [Python的画图模块turtle命令](https://www.pythontab.com/html/2017/pythongui_1121/1185.html)

* [数据结构与算法 22 递归图形](https://blog.csdn.net/python2014/article/details/22187531)