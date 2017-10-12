
#(a)画极坐标曲线, (b)能够生成整个图形的θ区间最短长度是多少
#r = theta
#theta 属于全体实数

def rFun(theta):
    return theta

def xFun(theta):
    return rFun(theta)*cos(theta)

def yFun(theta):
    return rFun(theta)*sin(theta)

thetaP = linspace(0, 10*pi, 10000)
thetaN = linspace(-10*pi, 0, 10000)
xP = xFun(thetaP)
yP = yFun(thetaP)
xN = xFun(thetaN)
yN = yFun(thetaN)

plot(xP, yP, '-r', xN, yN, '-g')
