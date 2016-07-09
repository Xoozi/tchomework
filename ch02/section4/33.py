#切线
#f(x)在0 <= x <= 2pi中有水平切线吗?
#f(x) = x - cot(x)
#fd(x) = 1 - csc(x)**2
def cot(x):
    return cos(x)/sin(x)

def csc(x):
    return 1/sin(x)
def f(x):
    return x - cot(x)

def fd(x):
    return 1 + csc(x)**2

def draw_tangent_line(px, py, slop, sx, ex):
    sy = slop*(sx - px) + py
    ey = slop*(ex - px) + py
    plot([sx, ex], [sy, ey], 'g--')

def draw_work(s, e, ax):

    x = linspace(s, e, 100)
    y = f(x)

    ay = f(ax)

    xlabel('x')
    ylabel('y')
    plot(x, y, 'r-', [ax], [ay], '*r')
    text(ax, ay, 'a:%f' % (fd(ax)))
    draw_tangent_line(ax, ay, fd(ax), s, e)

draw_work(0+0.1, pi-0.1, pi/2)
draw_work(pi+0.1, 2*pi - 0.1, 3*pi/2)
