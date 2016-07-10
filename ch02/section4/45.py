#求曲线 画y = cos(x), -pi <= x <= 2*pi的图形
#在同一屏幕上对, h = 1, 0.5, 0.3, 0.1画
#y = (sin(x + h) - sin(x))/h的图形

def f(x):
    return cos(x)

def g(x, h):
    return (sin(x + h) - sin(x)) / h

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

s = -pi
e = 2*pi

draw_f(s, e)
draw_g(s, e, 1, 'g-')
draw_g(s, e, 0.5, 'g--')
draw_g(s, e, 0.3, 'g^')
draw_g(s, e, 0.1, 'g*')

draw_g(s, e, -1, 'b-')
draw_g(s, e, -0.5, 'b--')
draw_g(s, e, -0.3, 'b^')
draw_g(s, e, -0.1, 'b*')

#xoozi 这个对比很有意思, 虽然我现在根基浅无法有进一步的认识
