#三角多项式
#(a)在[-pi, pi]画出它的图形
#(b)求df/dt

def f(t):
    return 0.78540 - 0.63662*cos(2*t) - 0.07074 * cos(6*t) - 0.02546 * cos(10*t) - 0.01299*cos(14*t)

def fd(t):
    return 0.63662*sin(2*t)*2 + 0.07074 * sin(6*t)*6 + 0.02446 * sin(10*t)*10 + 0.01299 * sin(14*t) * 14


def draw_work(s, e):

    t = linspace(s, e, 100)
    y = f(t)
    dy= fd(t)


    xlabel('t')
    ylabel('y')
    plot(t, y, 'r-', t, dy, 'g-')

draw_work(-pi, pi)
