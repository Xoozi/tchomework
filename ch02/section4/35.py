#切线
#求曲线 f(x) = tan(x), -pi/2 < x < pi/2的, 与直线 y = 2*x平行的所有点
#f(x) = tan(x)
#fd(x) = sec(x)**2
#fd(x) = 2 => sec(x)=±sqrt(2)
#=>1/cos(x) = ±sqrt(2)
#=>cos(x) = ±1/sqrt(2)
#=>x= ±pi/4
def sec(x):
    return 1/cos(x)

def f(x):
    return tan(x)

def fd(x):
    return sec(x)**2

def draw_tangent_line(px, py, slop, sx, ex):
    sy = slop*(sx - px) + py
    ey = slop*(ex - px) + py
    plot([sx, ex], [sy, ey], 'g--')

def draw_work(s, e, a1x, a2x):

    x = linspace(s, e, 100)
    y = f(x)

    a1y = f(a1x)
    a2y = f(a2x)

    xlabel('x')
    ylabel('y')
    plot(x, y, 'r-', [a1x], [a1y], '*r', [a2x], [a2y], '*b')
    text(a1x, a1y, 'a1:%f' % (fd(a1x)))
    text(a2x, a2y, 'a2:%f' % (fd(a2x)))
    draw_tangent_line(a1x, a1y, fd(a1x), s, e)
    draw_tangent_line(a2x, a2y, fd(a2x), s, e)

draw_work(-pi/2 + 0.1, pi/2 - 0.1, -pi/4, pi/4)
