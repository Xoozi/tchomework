#参数化曲线的切线
#   x = t,	y = t**(1/2),	t = 1/4
#   dy/dx	= (dy/dt)/(dx/dt)
#		= (1/2*t**(-1/2))/1
#		= 1/2*t**(-1/2)
#       t=1/4   = 1
#   d2y/dx2     =
#               = (dy'/dt)/(dx/dt)
#               = -1/4*t**(-3/2)
#       t=1/4   = -2
def xf(t):
    return t

def yf(t):
    return sqrt(t)

def yfd(t):
    return 0.5 * t**(-0.5)


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
    draw_tangent_line(ax, ay, yfd(at), s, e)


draw_work(0.1, 1, 0.25)
