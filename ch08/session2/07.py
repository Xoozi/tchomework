#Newton方法产生的序列
#应用到一个可微函数f(x)的Newton方法, 从一个初始值x0开始构造序列{xn}, 该序列在适当的条件下收敛到f的零点.
#序列的递归公式是: xn+1 = xn - f(xn)/f'(xn)
#(a)证明对f(x) = x² - a, a > 0, 递归公式可以写成xn+1 = (xn + a/xn)/2
#f'(x) = 2x, xn+1 = xn - (xn²-a)/2xn = xn - xn/2 + a/2xn = xn/2 + a/2xn = (xn + a/xn)/2
#
#(b) 从x0 = 1 和 a = 3开始, 计算序列相继各项, 直到显示开始重复, 序列逼近什么数, 作出解释

def r(xn, a):
    return (xn + a/xn)/2.0

xp = 1.0
xn = 0.0
a = 3.0

delta = xn - xp
cnt = 0

while cnt < 1000000 and (delta > 0.0000001 or delta < -0.0000001) :
    xn = r(xp, a)
    delta = xn - xp
    xp = xn
    cnt = cnt + 1

print 'cnt:%d, xn:%f, delta:%f' % (cnt, xn, delta)

#5次就达到目的了, 收敛的很快嘛
