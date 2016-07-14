#参数化曲线的切线
#   x = 2*cos(t),	y = 2*sin(t),	t = pi/4
#   dy/dx	= (dy/dt)/(dx/dt)
#		= 2*cos(t)/2*-sin(t)
#		= -cot(t)
#       t=pi/4  = -1
#   d2y/dx2     =
#               = (dy'/dt)/(dx/dt)
#               = csc(t)**2/2*-sin(t)
#       t=pi/4  = -sqrt(2) 
def xf(t):
    return 2*cos(t)

def yf(t):
    return 2*sin(t)

def yfd(t):
    return -1*cos(t)/sin(t)


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


draw_work(0, 2*pi, pi/4)
