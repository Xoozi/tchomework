

#方程(2)
#s(x) = A*sin(2*PI/B(x-C)) + D
#	|A| 为振幅
#	|B| 为周期
#        C  为水平位移
#	 D  为垂直位移

#对题中的正弦函数识别方程(2)中的ABCD， 并画出图形

#(a)f(x) = 2*sin(x+pi) - 1
#   A = 2
#   B = 2*pi
#   C = pi
#   D = -1
def f(x):
    return 2*sin(x+pi) - 1

#(b)g(x) = 0.5*sin(pi*x - pi) + 0.5
#   A = 0.5
#   B = 2
#   C = -2
#   D = 0.5
def g(x):
    return 0.5*sin(pi*x - pi) + 0.5

#玩下叠加
def w(x):
    return f(x) + g(x)


x = linspace(0, 4.0*pi, 100)
y1 = f(x)
y2 = g(x)
y3 = w(x)


xlabel('x')
ylabel('y')
plot(x, y1, 'r-', x, y2, 'g-', x, y3, 'b-')
