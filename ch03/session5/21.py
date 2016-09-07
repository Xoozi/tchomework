#仅当盒子的长度和腰围的和不超过108英寸时, 美国的邮局才接受国内投递
#(a)盒子有正方形侧面, 因而其尺寸为h*h*w, 腰围为2h+2w, 什么尺寸能给出最大体积
#   108 = 2*h+2*w + h=> w = (108-3h)/2 = 54 - 1.5h
#对v求到得到-4.5*h**2 + 108*h, 求临界点得到0和24, 0在定义域外, 所以在h=24时有最大体积
#(b)作图

def v(h):
    return h*h*(54 - 1.5*h)

def vd(h):
    return 108*h - 4.5*h**2

def vdd(h):
    return 108 - 9*h

x = linspace(15,35, 1000)
y = v(x)
yd= vd(x)
ydd= vdd(x)

plot([0, 50], [0, 0], '-k')
plot(x, y, '-r', x, yd, '-g', x, ydd, '-b')

vdp = poly1d([-4.5, 108, 0])
np.roots(vdp)


