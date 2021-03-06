#求函数图形的拐点, 以及函数的局部极值
#一二阶导数和x轴交点和函数的图形有怎样的关系?
#导数的图形以怎样的另一种形式和函数的图形相关
#y = f(x) = x**5 - 5*x**4 - 240
#y'= 0 的根为 x = 0, x = 4
#y''= 0 的根为x = 0, x = 3

#首先看x = 0处, 由于该处y''等于零, 不能用局部极值的二阶导数检测法, 
#利用一阶导数检测法, y'由正变负, 故x = 0处函数取得局部最大值
#再看x = 4处, 应用局部极值的二阶导数检测法该点取得局部最小值
#拐点, 先看x = 0处, 由于凹性在该点附近不变, 这不是拐点, 再看x = 3处, 凹性改变是拐点

#一阶导函数的根,是可能的局部极值点
#二阶导函数的根, 是可能的凹性改变的地方
#导数图形的增性, 决定了函数图形的凹性

def f(x):
    return x**5 - 5*x**4 - 240

def fd(x):
    return 5*x**4 - 20*x**3

def fdd(x):
    return 20*x**3 - 60*x**2


plot([-3, 5.4], [0, 0], '-k')

x = linspace(-3, 5.4, 10000)
y = f(x)
yd= fd(x)
ydd=fdd(x)
plot(x, y, '-r', x, yd, '-g', x, ydd, '-b')
