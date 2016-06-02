#控制输出 设f(x) = sqrt(3*x - 2)
#    
#(a)证明lim(x->2)f(x) = 2 = f(2)
#   f(x)在其定义域 x > 2/3, 上是连续的, 2>2/3所以, lim(x->2)f(x) = 2 = f(2)
#(b)用图形来估计a和b, 使得只要a<x<b, 就有1.8<f(x)<2.2
#(c)用图形来估计a和b, 使得只要a<x<b, 就有1.99<f(x)<2.01


def f(x):
    return sqrt(3*x - 2)

x = linspace(2/3+0.1, 3, 100)
y = f(x)


xlabel('x')
ylabel('y')
plot(x, y, 'r-')
