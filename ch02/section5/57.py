#切线
#求曲线 f(x) = 2*tan(pi*x/4) 
#(a)在x = 1处的切线
#(b)求-2 < x < 2上该曲线斜率的最小值

#f(x) = 2*tan(pi*x/4)
#fd(x) = pi/2*sec(pi*x/4)**2
#fd(x) = 的最小值就只能为pi/2 因为sec(pi*x/4)**2 >= 1
def sec(x):
    return 1/cos(x)


def f(x):
    return 2*tan(pi*x/4)

def fd(x):
    return (pi/2.0)*sec(pi*x/4)**2

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

def draw_fd(s, e):

    x = linspace(s, e, 100)
    y = f(x)

    plot(x, y, 'b-')


draw_work(-1.5, 1.5, 1, 1.2)
draw_fd(-1.9, 1.9)
