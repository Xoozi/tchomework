#加工金属薄板
#你的金属加工公司正投标签订加工覆盖房顶的波浪形钢板, 波浪形钢板的横截面形状如曲线
#y = sin(x*3*pi/20), 0 <= x <= 20
#如果屋顶钢板由平板冲压而成, 并且在冲压过程中不延展, 原来材料宽度多少?
#dy/dx = 3*pi/20 * cos(x*3*pi/20)
#W = L 	= ∫(0, 20) sqrt(1 + (dy/dx)**2) dx
#       = ∫(0, 20) sqrt(1 + 9*pi**2/400 * cos(x*3*pi/20)**2) dx
#积不来 改用数值积分


a = 3.0*pi/20.0
b = a*a

def f(x):
    return sqrt(1 + b*cos(a*x))

x = linspace(0, 20, 10000)

y = f(x)

y_int = trapz(y, x, 20.0/10000.0)

print 'y_int:%f' % (y_int)
