#画函数以求出区间, 函数在这些区间上
#(a)增  [0, +∞)
#(b)减  无
#(c)凹向上 [0.7194, +∞)
#(d)凹向下 [0, 0.7194)
#然后定位和识别
#(e)局部极值 x=0.14处取得局部极小值, x=1.399处取得局部极大值, x=2.45处取得局部极小值
#(f)拐点一阶导数增减性变化的点, 只有在x=1时二阶导数由正变负

#xoozi 我搞错了怪不得觉得做这几道题这么难
#这题就是让人用软件画函数图形然后在图上量解的
#所以后面几道题要求解析解很难算, 又不能配方
#直接画图解, 没啥计算量

def f(x):
    return (x**(0.25)) * (x + 3)

def fd(x):
    return 0.25 * x**(-0.75) * (x + 3) + x**(0.25)

def fdd(x):
    return 0.25 * (-0.75*x**(-1.75)* (x+3) + x**(-0.75)) + x**(0.25)

plot([-6, 6], [0, 0], '-k')


plot([-6, 10], [0, 0], '-k')

x = linspace(0.2, 2, 1000)
y = f(x)
yd= fd(x)
ydd=fdd(x)
plot(x, y, '-r', x, yd, '-g', x, ydd, '-b')
