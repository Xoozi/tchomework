
#求反函数
#f(x) = 100/ (1+2**(-x))
#解方程
#y = 100/ (1+2**(-x))
#1+2**(-x) = 100/y
#2**(-x) = 100/y - 1
#log2(2**(-x)) = log2(100/y - 1)
#x = log2(y/(100-y))
#x = ln(y/(100-y))/ln2

def f(x):
    return 100/(1.0+2.0**(-x))

def g(x):
    return log(x/(100-x))/log(2)


x = linspace(0, 10, 100)
y = f(x)

x1 = linspace(f(10), f(0), 100)
y1 = g(x1)


xlabel('x')
ylabel('y')
plot(x, y, 'r-', x1, y1, 'g-')
