
#切线
#把给定区间上的曲线的图形和他们在给定的x值处的切线画在一起
#f(x) = sec(x),     -pi/2 <= x <= pi/2,   x =-pi/3,  pi/4
def sec(x):
    return 1/cos(x)

def f(x):
    return sec(x)

def fd(x):
    return sec(x)*tan(x)

def draw_tangent_line(px, py, slop, sx, ex):
    sy = slop*(sx - px) + py
    ey = slop*(ex - px) + py
    plot([sx, ex], [sy, ey], 'g--')

s = -pi/2+0.1
e = pi/2-0.1

a1x = -pi/3
a2x = pi/4

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

