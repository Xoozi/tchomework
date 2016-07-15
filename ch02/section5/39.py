#参数化曲线的切线
#   x = cos(t),	y = 1 + sin(t),	t = pi/2
#   dy/dx	= (dy/dt)/(dx/dt)
#		= cos(t) / -sin(t)
#               = -cot(t)
#       t=pi/2  = 0
#   d2y/dx2     =
#               = (dy'/dt)/(dx/dt)
#               = csc(t)**2/-sin(t)
#               = -csc(t)**3
def xf(t):
    return cos(t)

def yf(t):
    return 1+sin(t)

def yfd(t):
    return cos(t)/-sin(t)


def draw_tangent_line(px, py, slop, sx, ex):
    sy = slop*(sx - px) + py
    ey = slop*(ex - px) + py
    plot([sx, ex], [sy, ey], 'g--')

def draw_work(s, e, at):

    t = linspace(s, e, 100)
    x = xf(t)
    y = yf(t)

    ax = xf(at)
    ay = yf(at)

    xlabel('x')
    ylabel('y')
    plot(x, y, 'r-', [ax], [ay], '*r')
    text(ax, ay, 'a:%f' % (yfd(at)))

    #xoozi 注意这里端点, 不是由t指定的, 而是由x的参数方程决定
    draw_tangent_line(ax, ay, yfd(at), xf(s), xf(e))


draw_work(0+0.1, pi-0.1, pi/2)
