

#图形解方程
#cos(x) = x
#cos(x) - x
#r=0.74938
#xoozi 形状比较有意思, 原来这种斜波纹可以这样构造

def f(x):
    return cos(x) - x

x = linspace(-10, 10, 100)
y = f(x)


xlabel('x')
ylabel('y')
plot(x, y, 'r-', [-10, 10], [0, 0], 'g-')
