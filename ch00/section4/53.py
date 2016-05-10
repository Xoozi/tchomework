

#把函数f(x) = x*3 和g(x) = x*(1/3) 画在一张图上
#画f(g(x))
#画g(f(x))

def f(x):
    return x*3.0

def g(x):
    return x*(1.0/3.0)

def fg(x):
    return f(g(x))

def gf(x):
    return g(f(x))


x = linspace(-10, 10, 100)
xg = linspace(f(10), f(-10), 100)
y1 = f(x)
y2 = g(xg)
y3 = fg(xg)
y4 = gf(x)


xlabel('x')
ylabel('y')
plot(x, y1, 'r-', xg, y2, 'g-', xg, y3, 'b-', x, y4, 'r--')
