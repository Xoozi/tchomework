

#画出参数方程的图像：
#x = 3*sin(2*t)
#y = 1.5*cos(t)

def f(t):
    return 3*sin(2*t)

def g(t):
    return 1.5*cos(t)

t = linspace(0, 2*pi, 100)

x = f(t)
y = g(t)


xlabel('x')
ylabel('y')
plot(x, y, 'r-');
