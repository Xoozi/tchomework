
#图形解方程
#sqrt(x) + sqrt(1+x) = 4
#sqrt(x) + sqrt(1+x) - 4
#放大后发现, 有一个根
#r=3.528

def f(x):
    return sqrt(x) + sqrt(1+x) - 4

x = linspace(-10, 10, 100)
y = f(x)


xlabel('x')
ylabel('y')
plot(x, y, 'r-', [-10, 10], [0, 0], 'g-')
