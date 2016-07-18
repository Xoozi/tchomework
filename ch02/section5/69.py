#sin2x的导数
#在-2 <= x <= 3.5上画函数y = 2*cos(2*x)的图形, 然后在同一屏幕上对h=1.0, 0.5和0.2画:
#y = (sin(2*(x+h)) - sin(2*x))/h
#的图形, 当h->0时发生了什么?
def f(x):
    return sin(2*x)

def fd(x):
    return 2*cos(2*x)

def dd(x, h):
    return (sin(2*(x+h)) - sin(2*x)) / h

def draw_work(s, e):

    x = linspace(s, e, 100)
    y1 = f(x)
    y2 = fd(x)
    y3 = dd(x, 1.0)
    y4 = dd(x, 0.5)
    y5 = dd(x, 0.2)


    xlabel('x')
    ylabel('y')
    plot(x, y1, 'r-', x, y2, 'g-', x, y3, 'b-', x, y4, 'b--', x, y5, 'b*')

draw_work(-2, 3.5)
