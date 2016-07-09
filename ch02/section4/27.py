#切线
#把给定区间上的曲线的图形和他们在给定的x值处的切线画在一起
#f(x) = sin(x),     -3*pi/2 <= x <= 2*pi,   x =-pi, 0, 3*pi/2
def f(x):
    return sin(x)

def fd(x):
    return cos(x)

def draw_tangent_line(px, py, slop, sx, ex):
    sy = slop*(sx - px) + py
    ey = slop*(ex - px) + py
    plot([sx, ex], [sy, ey], 'g--')

s = -3*pi/2
e = 2*pi

a1x = -pi
a2x = 0
a3x = 3*pi/2

x = linspace(s, e, 100)
y = f(x)

a1y = f(a1x)
a2y = f(a2x)
a3y = f(a3x)

xlabel('x')
ylabel('y')
plot(x, y, 'r-', [a1x], [a1y], '*r', [a2x], [a2y], '*g', [a3x], [a3y], '*b')
text(a1x, a1y, 'a1:%f' % (fd(a1x)))
text(a2x, a2y, 'a2:%f' % (fd(a2x)))
text(a3x, a3y, 'a3:%f' % (fd(a3x)))
draw_tangent_line(a1x, a1y, fd(a1x), s, e)
draw_tangent_line(a2x, a2y, fd(a2x), s, e)
draw_tangent_line(a3x, a3y, fd(a3x), s, e)

