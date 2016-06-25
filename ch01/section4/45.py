
#图形解方程
#x**3 - 3*x - 1 = 0
#放大后发现, 有三个根
#r1 = 

def f(x):
    return x**3 - 3*x - 1

x = linspace(-2, 2, 100)
y = f(x)


xlabel('x')
ylabel('y')
plot(x, y, 'r-', [-10, 10], [0, 0], 'g-')
