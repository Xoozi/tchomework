def f(x):
    return (x**3)/3.0
#(a)求f(x)的导函数fd(x)
#   f(x) = 1/3*x**3
#   fd(x) = x**2
#(b)在同区间上画f(x)和fd(x)的图形
#(c)对哪些x值fd(x)为正? 为零? 为负?
#   x = 0 时fd(x)为零
#   x != 0 时fd(x)为正
#
#(d)在x值的哪些区间上当x增加时函数f(x)递增?当x减少时f(x)递减?
#   f(x)在x!=0时单调递增
#   
#   这些和在(c)中发现的结果有什么关系?
#   x != 0 时fd(x)为正
#   f(x)单调递增
#   x = 0时 fd(x)为0
#   f(x)变化率为0

def fd(x):
    return x**2



x = linspace(-10, 10, 100)
y1 = f(x)
y2 = fd(x)


xlabel('x')
ylabel('y')
plot(x, y1, 'r-', x, y2, 'g-')
