#极图形的对称判别法
#1. 关于x轴对称: 若点(r, θ)在图上, 则点(r, -θ) 或 (-r, pi - θ)在图上
#2. 关于y轴对称: 若点(r, θ)在图上, 则点(r, pi - θ) 或 (-r, -θ)在图上
#3. 关于原点对称:若点(r, θ)在图上, 则点(-r, θ) 或 (r, pi + θ)在图上

#61. r = 2 + sin θ
#    先检查1. 不符合
#    再检查2. sin(pi - θ) = sin(θ) => 点(r, θ)和(r, pi - θ)在图上
#    再检查3. 不符合

#故图形关于y轴, 对称, 画出图形来是个梨形

def rFun(theta):
    return 2 + sin(theta)

def xFun(theta):
    return rFun(theta)*cos(theta)

def yFun(theta):
    return rFun(theta)*sin(theta)

theta = linspace(0, 2.0*pi, 1000)
x = xFun(theta)
y = yFun(theta)


plot(x, y, '-r')

