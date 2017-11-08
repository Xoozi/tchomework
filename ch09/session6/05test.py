
def rFun(theta):
    return 3.0*cos(theta)

def xFun(theta):
    return rFun(theta)*cos(theta)

def yFun(theta):
    return rFun(theta)*sin(theta)

theta = linspace(0, 2.0*pi, 1000)
x = xFun(theta)
y = yFun(theta)


plot(x, y, '-r')

