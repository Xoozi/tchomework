#(a)画极坐标曲线, (b)能够生成整个图形的θ区间最短长度是多少
#r = 2 cos 3θ
#0 - pi

def rFun(theta):
    return 2.0*cos(3*theta)

def xFun(theta):
    return rFun(theta)*cos(theta)

def yFun(theta):
    return rFun(theta)*sin(theta)

theta = linspace(0, pi, 1000)
xP = xFun(theta)
yP = yFun(theta)

plot(xP, yP, '-r')
