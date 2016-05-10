


#(a)用cos(x)来表示cos(pi + x)
#   从图像可以看出cos(pi + x) = -cos(x)
def f(x):
    return cos(pi+x)

#(b)用sin(x) sin(2*pi - x)
#   从图像看sin(2*pi - x) = -sin(x)
#   推理也可知sin(2*pi - x) = sin(-x)
#       sin(x)是奇函数 => sin(-x) = -sin(x)
def g(x):
    return sin(2*pi - x)


x = linspace(0, 2.0*pi, 100)
y1 = cos(x)
y2 = f(x)
y3 = sin(x)
y4 = g(x)


xlabel('x')
ylabel('y')
plot(x, y1, 'r-', x, y2, 'g-', x, y3, 'b-', x, y4, 'y-')
