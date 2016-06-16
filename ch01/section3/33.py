



#画有理函数的图形
#y = 8 /(x**2 + 4)

def f(x):
    return 8 / (x**2 + 4)

x = linspace(-10, 10, 100)
y = f(x)


xlabel('x')
ylabel('y')
plot(x, y, 'r-')
