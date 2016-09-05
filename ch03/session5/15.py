#罐的设计
#设计一狗1000立方厘米容积的直圆柱罐, 它的制作要考虑损耗
#切割侧面时无损耗

def a(x):
    return sin(x)

def ad(x):
    return cos(x)

def add(x):
    return -sin(x)


x = linspace(pi/6, 5*pi/6, 1000)
y = a(x)
yd= ad(x)
ydd= add(x)

plot([0, pi], [0, 0], '-k')
plot(x, y, '-r', x, yd, '-g', x, ydd, '-b')


