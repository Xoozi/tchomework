#极大化体积
#求能内接于半径10的球内的最大可能体积的直圆柱的尺寸
#设该圆柱高h, 半径r, 由于圆柱内接半径10的球, 故圆柱过底面圆心的立剖面矩形边分别为2*r, h,
#对角线为20, 故有400 = 4*r**2 + h**2 => (400-h**2)/4 = r**2
#而圆柱体积为V = pi*r**2 * h = pi*(400-h**2)*h

def v(h):
    return pi*(400*h-h**3)

def vd(h):
    return pi*(400 - 3*h**2)

def vdd(h):
    return pi*(-6*h)


x = linspace(2,18, 1000)
y = v(x)
yd= vd(x)
ydd= vdd(x)

plot([0, 20], [0, 0], '-k')
plot(x, y, '-r', x, yd, '-g', x, ydd, '-b')



