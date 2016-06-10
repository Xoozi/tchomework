#(a)画g(x) = x*sin(1/x)的图形来估算lim(x->0)g(x)
#   0

#(b)现在画k(x) = sin(1/x)的图形. 在原点附近比较g和k的性态, 什么是相同的, 什么是不同的
#   g(x)是偶函数, k(x)是奇函数, 且g(x)比k(x)在原点附近要平滑的多

def g(x):
    return x*sin(1/x)
def k(x):
    return sin(1/x)

x = linspace(-0.1, 0.1, 100)
y2 = g(x)
y3 = k(x)


xlabel('x')
ylabel('y')
plot(x, y2, 'r-', x, y3, 'g-')
