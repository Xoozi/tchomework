#Picard方法
#用皮卡方法解下列方程
#其实书中没有详细描述Picard方法的算法
#通过做题我摸到一点, 就是把方程变形成g(x) = x的样式, 然后开始表演

#27 sqrt(x) = x
def g27(x):
    return sqrt(x)

#29 cosx + x = 0
def g29(x):
    return -cos(x)

#31 x - sinx = 0.1
def g31(x):
    return 0.1 + sin(x)

def picard(gfun, x0):
    xp = x0
    xn = 0.0

    delta = xn - xp
    cnt = 0

    while cnt < 100 and (delta > 0.0000001 or delta < -0.0000001) :
        xn = gfun(xp)
        delta = xn - xp
        xp = xn
        cnt = cnt + 1

    print 'Picard mothed fun:%s, cnt:%d, xn:%f, delta:%f' % (gfun.__name__, cnt, xn, delta)

picard(g27, 1.0);
picard(g29, 1.0);
picard(g31, 1.0);
