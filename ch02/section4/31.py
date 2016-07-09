#切线
#f(x)在0 <= x <= 2pi中有水平切线吗?
#f(x) = x + sin(x)
#fd(x) = 1 + cos(x)
def f(x):
    return x + sin(x)

def fd(x):
    return 1 + cos(x)

def draw_tangent_line(px, py, slop, sx, ex):
    sy = slop*(sx - px) + py
    ey = slop*(ex - px) + py
    plot([sx, ex], [sy, ey], 'g--')

s = 0
e = 2*pi

a1x = 0
a2x = pi

x = linspace(s, e, 100)
y = f(x)

a1y = f(a1x)
a2y = f(a2x)

xlabel('x')
ylabel('y')
plot(x, y, 'r-', [a1x], [a1y], '*r', [a2x], [a2y], '*g')
text(a1x, a1y, 'a1:%f' % (fd(a1x)))
text(a2x, a2y, 'a2:%f' % (fd(a2x)))
draw_tangent_line(a1x, a1y, fd(a1x), s, e)
draw_tangent_line(a2x, a2y, fd(a2x), s, e)

