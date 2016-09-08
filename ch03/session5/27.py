#锥的构建
#斜边为sqrt(3)米的直角三角形绕它的一条侧边旋转生成一个直圆锥, 求能使该直圆锥体积
#最大的尺寸
#设直圆锥底部半径r, 高h, 有r**2 + h**2 = 3
#r**2 = 3 - h**2
#而圆锥体积V = 1/3 * pi * r**2 * h = 1/3 * pi * (3-h**2) * h
#h=1时体积有最大值

def v(h):
    return pi*h - pi*h**3/3.0

def vd(h):
    return pi - pi*h**2

def vdd(h):
    return -2*pi*h

x = linspace(0.2,1.2, 1000)
y = v(x)
yd= vd(x)
ydd= vdd(x)

plot([0, 1.2], [0, 0], '-k')
plot(x, y, '-r', x, yd, '-g', x, ydd, '-b')

