#中心差商
#(f(x + h) - f(x - h))/2h
#在数值计算中用来近似计算df(x)/dx, 因为:
#(1)当df(x)/dx存在时, h->0时其极限等于df(x)/dx
#(2)它通常给出对给定的h值的df(x)/dx的比费马差商(f(x+h)-f(x)/h)更好的近似
#
#(a)为看出f(x) = sin(x)的中心差商收敛到df(x)/dx = cos(x)有多快, 
#在区间[-pi, 2*pi], 把y = cos(x)和中心差商在h=1, 0.5, 0.3的图形画在一起,和45题图比较
#求曲线 画y = cos(x), -pi <= x <= 2*pi的图形
#在同一屏幕上对, h = 1, 0.5, 0.3, 0.1画
#y = (sin(x + h) - sin(x))/h的图形
#xoozi 结论是中心差商, 收敛更快些, 但是中心差商有一个问题, 在f(x)在某处x时无导数的情况下,中心差商的极限仍然存在
#格言: 采用中心差商时, 要确认导数存在

def f(x):
    return cos(x)

def g(x, h):
    return (sin(x + h) - sin(x)) / h

def w(x, h):
    return (sin(x+h) - sin(x-h)) / (2*h)

def draw_f(s, e):

    x = linspace(s, e, 100)
    y = f(x)

    xlabel('x')
    ylabel('y')
    plot(x, y, 'r-')

def draw_g(s, e, h, style):

    x = linspace(s, e, 100)
    y = g(x, h)

    xlabel('x')
    ylabel('y')
    plot(x, y, style)

def draw_w(s, e, h, style):

    x = linspace(s, e, 100)
    y = w(x, h)

    xlabel('x')
    ylabel('y')
    plot(x, y, style)

s = -pi
e = 2*pi

draw_f(s, e)
draw_g(s, e, 1, 'g-')
draw_g(s, e, 0.5, 'g--')
draw_g(s, e, 0.3, 'g^')
draw_g(s, e, 0.1, 'g*')

draw_w(s, e, -1, 'b-')
draw_w(s, e, -0.5, 'b--')
draw_w(s, e, -0.3, 'b^')
draw_w(s, e, -0.1, 'b*')

