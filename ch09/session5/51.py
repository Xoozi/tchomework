#(a)画极坐标曲线, (b)能够生成整个图形的θ区间最短长度是多少
#r² = 1 - sin θ
#0 - pi/2

def rPFun(theta):
    return sqrt(1 + sin(theta))

def rNFun(theta):
    return sqrt(1 + sin(theta))

def xPFun(theta):
    return rPFun(theta)*cos(theta)

def yPFun(theta):
    return rPFun(theta)*sin(theta)

def xNFun(theta):
    return rNFun(theta)*cos(theta)

def yNFun(theta):
    return rNFun(theta)*sin(theta)

theta = linspace(0, pi/2.0, 1000)
xP = xPFun(theta)
yP = yPFun(theta)
xN = xNFun(theta)
yN = yNFun(theta)

plot(xP, yP, '-r', xN, yN, '-g')
