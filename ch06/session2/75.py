#e**x和ln x之间的互逆关系
#发现你的计算器在求复合函数e**ln x 和 ln e**x的值时的样子

def f1(x):
    return e**(log(x))

def f2(x):
    return log(e**x)

x  = linspace(0.5, 5.0, 10000)
y1 = f1(x)

y2 = f2(x)

plot(x, y1, '-r', x, y2, '-g')
