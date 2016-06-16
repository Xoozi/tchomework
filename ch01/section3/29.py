

#画有理函数的图形
#y = (x**4 + 1) / x**2

def f(x):
    return (x**4 + 1) / x**2

x1 = linspace(0.1, 10, 100)
y1 = f(x1)
x2 = linspace(-10, -0.1, 100)
y2 = f(x2)


xlabel('x')
ylabel('y')
plot(x1, y1, 'r-', x2, y2, 'g-')
