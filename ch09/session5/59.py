#极图形的对称判别法
#1. 关于x轴对称: 若点(r, θ)在图上, 则点(r, -θ) 或 (-r, pi - θ)在图上
#2. 关于y轴对称: 若点(r, θ)在图上, 则点(r, pi - θ) 或 (-r, -θ)在图上
#3. 关于原点对称:若点(r, θ)在图上, 则点(-r, θ) 或 (r, pi + θ)在图上

#59. r² = 4 cos 2θ
#    先检查1. 由于cos是偶函数, (r, θ) 和 (r, -θ)在图上
#    再检查2. 由于cos是偶函数, 而方程左边是r²故(r, θ)和(-r, -θ)在图上
#    再检查3. 很明显(r, θ)和(-r, θ)在图上

#故图形关于x轴, y轴, 及原点对称, 画出图形来是个倒8字

def rPFun(theta):
    return sqrt(4.0*cos(2.0*theta));

def rNFun(theta):
    return -sqrt(4.0*cos(2.0*theta));

def xPFun(theta):
    return rPFun(theta)*cos(theta)

def xNFun(theta):
    return rNFun(theta)*cos(theta)

def yPFun(theta):
    return rPFun(theta)*sin(theta)

def yNFun(theta):
    return rNFun(theta)*sin(theta)

thetaP = linspace(-0.5*pi, 1.5*pi, 1000)
xP = xPFun(thetaP)
yP = yPFun(thetaP)

thetaN = linspace(0, 2.0*pi, 1000)
xN = xNFun(thetaN)
yN = yNFun(thetaN)

subplot(211)
plot(xP, yP, '-r')

subplot(212)
plot(xN, yN, '-g')
