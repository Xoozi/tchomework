#斜率于切线
#求Newton蛇形线在原点和点(1,2)的切线j
#f(x) = 4*x/(x**2 + 1)
def f(x):
    return 4*x/(x**2 + 1)
#求fd, 令u(x) = 4*x, v(x) = x**2 + 1
#fd(x) = (ud(x)*v(x) - vd(x)*u(x)) / v(x)**2
#      = (4*x**2 + 4 - 2*x*4*x) / (x**2 + 1)**2
#      = (4*x**2 - 8*x**2 + 4) / (x**2 + 1)**2
#      = 4*(1 - 2*x**2) / (x**2 + 1)**2

def fd(x):
    return 4*(1 - x**2) / (x**2 + 1)**2

def draw_tangent_line(px, py, slop, sx, ex):
    sy = slop*(sx - px) + py
    ey = slop*(ex - px) + py
    plot([sx, ex], [sy, ey], 'g--')

a1x = 0
a2x = 1

x = linspace(-4, 4, 100)
y = f(x)

a1y = f(a1x)
a2y = f(a2x)

xlabel('x')
ylabel('y')
plot(x, y, 'r-', [a1x], [a1y], '*r', [a2x], [a2y], '*g')
text(a1x, a1y, 'a1:%f' % (fd(a1x)))
text(a2x, a2y, 'a2:%f' % (fd(a2x)))
draw_tangent_line(a1x, a1y, fd(a1x), -4.0, 4.0)
draw_tangent_line(a2x, a2y, fd(a2x), -4.0, 4.0)

