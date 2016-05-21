#用参数做图法画出f(x) anti_f(x) 和 y = x
#f(x) = 2**(-x), x = t, y = 2**(-t)
#
#anti_f(x) = -log2(x), x = t, y = -log2(t)

def fx(t):
    return t
def fy(t):
    return 2**(-t)

def anti_fx(t):
    return t
def anti_fy(t):
    return -1*log(t)/log(2)

def cx(t):
    return t
def cy(t):
    return t

t = linspace(0, 4, 100)

x1 = fx(t)
y1 = fy(t)

x2 = anti_fx(t)
y2 = anti_fy(t)

x3 = cx(t)
y3 = cy(t)


xlabel('x')
ylabel('y')
plot(x1, y1, 'r-', x2, y2, 'g-', x3, y3, 'b-')
