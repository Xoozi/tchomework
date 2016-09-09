#梁的刚度
#矩形梁的刚度S和其宽度与深度的立方之积成正比
#(a)求能从直径12英寸的圆柱切下的刚度最高的梁的尺寸
#(b)设比例系数为k = 1, 画S作为w的函数的图形
#(c)画S作为d的函数的图形, 尝试改变k值
#12*12 = d**2 + w**2 => d = sqrt(144 - w**2) => w = sqrt(144 - d**2)
#Sw(w) = d**3 * w = sqrt(144 - w**2)**3 * w
#Sd(d) = d**3 * w = d**3 * sqrt(144 - d**2)
#改变k值对极值尺寸无影响, 

def Sw(w, k):
    return k*sqrt(144 - w**2)**3 * w

def Sd(d, k):
    return k*d**3 * sqrt(144 - d**2)

plot([0, 12], [0, 0], '-k')

x = linspace(2, 12, 100000)
yw = Sw(x, 1.0)
yd = Sd(x, 1.0)
plot(x, yw, '-r', x, yd, '-r')

yw = Sw(x, 3.0)
yd = Sd(x, 3.0)
plot(x, yw, '-g', x, yd, '-g')

yw = Sw(x, 9.0)
yd = Sd(x, 9.0)
plot(x, yw, '-b', x, yd, '-b')

