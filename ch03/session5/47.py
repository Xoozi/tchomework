#生产水平
#证明: 如果r(x) = 6*x 而c(x) = x**3 - 6*x**2 + 15*x是你的收入和成本函数
#那么你能做的最好的策略就是不亏不盈
#rd(x) = 6
#cd(x) = 3*x**2 - 12*x + 15
#根据定理6, 最大利润时rd(x) = cd(x) => 3*x**2 - 12*x + 15 = 6
#=> x**2 - 4*x + 3 = 0
#=>(x-1)*(x-3) = 0
#在x = 1 时r(x) = 6 c(x) = 10 亏损
#在x = 3 事r(x) = 18, c(x) = 18 不亏不盈
#xoozi其实这有硬套定理6的感觉
#而官方答案, 又是这样, 用的正规套路, 没有用定理6
#仿佛告诉我们, 定理6只是一个快速判断的概念,
#还是应该用正规手段建模
#p(x) = r(x) - c(x) = -x**3 + 6*x**2 - 9*x
#pd(x) = -3*x**2 + 12*x - 9
#pdd(x) = -6*x + 12
#解方程pd(x) = 0得到两个临界点x = 1和x = 3
#x = 1时, pdd(x) = 6, p(x) got mini
#x = 3, pdd(x) < 0, p(x) got max

def r(x):
    return 6*x

def c(x):
    return x**3 - 6*x**2 + 15*x

def p(x):
    return -x**3 + 6*x**2 - 9*x

def pd(x):
    return -3*x**2 + 12*x - 9

def pdd(x):
    return -6*x + 12

x = linspace(0, 5, 1000)
yr= r(x)
yc= c(x)
yp= p(x)
ypd= pd(x)
ypdd=pdd(x)

plot([0, 5], [0, 0], '-k')
plot(x, yr, '-r', x, yc, '-g')
plot(x, yp, '--r', x, ypd, '--g', x, ypdd,  '--b')

