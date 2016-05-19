
#求参数方程：
#起点为（2, 3）经过（-1, -1）的射线
#P(t) = (1-t)*P1 + t*P2   0<=t<=+∞
#x(t) = (1-t)*2 + t*-1 = 2-3*t
#y(t) = (1-t)*3 + t*-1 = 3-4*t

def f(t):
    return 2-3*t

def g(t):
    return 3-4*t

t = linspace(0, 2, 100)

x = f(t)
y = g(t)


xlabel('x')
ylabel('y')
plot(x, y, 'r-');
