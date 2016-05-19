

#画出参数方程的图像：
#x = 7*sin(t) - sin(7*t)
#y = 7*cos(t) - cos(7*t)

def f(t):
    return 7*sin(t) - sin(7*t)

def g(t):
    return 7*cos(t) - cos(7*t)

t = linspace(0, 2*pi, 100)

x = f(t)
y = g(t)


xlabel('x')
ylabel('y')
plot(x, y, 'r-');
