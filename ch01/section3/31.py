


#画有理函数的图形
#y = (x**2 - x + 1)/(x-1)

def f(x):
    return (x**2 - x + 1)/(x - 1)

x1 = linspace(1.1, 10, 100)
y1 = f(x1)
x2 = linspace(-10, 0.9, 100)
y2 = f(x2)


xlabel('x')
ylabel('y')
plot(x1, y1, 'r-', x2, y2, 'g-')
