#用参数做图法画出f(x) anti_f(x) 和 y = x
#f(x) = e**x, x = t, y = e**t
#
#anti_f(x) = ln(x), x = t, y = ln(t)

def fx(t):
    return t
def fy(t):
    return e**t

def anti_fx(t):
    return t
def anti_fy(t):
    return log(t)

def cx(t):
    return t
def cy(t):
    return t

t = linspace(0, 3, 100)

x1 = fx(t)
y1 = fy(t)

x2 = anti_fx(t)
y2 = anti_fy(t)

x3 = cx(t)
y3 = cy(t)


xlabel('x')
ylabel('y')
plot(x1, y1, 'r-', x2, y2, 'g-', x3, y3, 'b-')
