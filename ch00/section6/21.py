#求参数方程：
#端点为（-1, -3）和 （4, 1）的直线段
#P(t) = (1-t)*P1 + t*P2   0<=t<=1
#x(t) = (1-t)*-1 + t*4 = -1+5t
#y(t) = (1-t)*-3 + t = -3+4t

def f(t):
    return -1+5*t

def g(t):
    return -3+4*t

t = linspace(0, 1, 100)

x = f(t)
y = g(t)


xlabel('x')
ylabel('y')
plot(x, y, 'r-');
