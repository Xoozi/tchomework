

# IPython log file
# 下表给出了墨西哥的人口数据
#   年份              人口（百万）
#   1950                25.8
#   1960                34.9
#   1970                48.2
#   1980                66.8
#   1990                81.1
#
#(a)设x = 0 表示1900年， x = 1 表示1901年， 对该数据求指数回归方程， 并把它们的图形重叠到数据的散点图上
#(b)利用指数回归方程估计1900年墨西哥的人口， 该估计和1900年墨西哥人口的实际数量13607272有多接近
#(c)利用指数回归方程估计墨西哥人口的年增长率

#xoozi 此题说明两个问题:
#   1 scipy的指数回归方程有问题， t取50, 60, 70, 80, 90这组数据回归出来的系数不正常
#   2 指数回归， 如果样本太稀疏， 回归出来的函数， 在数据的远端差异非常大，基本没有参考价值了

import scipy
from scipy import stats
from scipy import optimize

def model_func(t, A, K, C):
    return A * numpy.exp(K*t) + C




#t = array([50.0, 60.0, 70.0, 80.0, 90.0])
t = array([0, 10, 20, 30, 40])
y = array([25800000, 34900000, 48200000, 66800000, 81100000])

opt_parms , parm_cov = optimize.curve_fit(model_func, t, y)

A, K, C = opt_parms

print 'A:%f, K:%f, C:%f' % (A, K, C)

print '1900:%f' % model_func(-50, A, K, C)


xlabel('t')
ylabel('y')

x = linspace(-50, 50.0, 100)
plot(x, model_func(x, A, K, C), 'r-')
plot(t, y, 'bo--')
