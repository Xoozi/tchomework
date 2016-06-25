
#图形解方程
#x*(x - 1)**2 = 1
#x**3 - 2*x**2 + x - 1 = 0
#放大后发现, 有一个根
#r=1.78165

def f(x):
    return x**3 - 2*x**2 + x - 1

x = linspace(-0.4, 2.1, 100)
y = f(x)


xlabel('x')
ylabel('y')
plot(x, y, 'r-', [-10, 10], [0, 0], 'g-')
