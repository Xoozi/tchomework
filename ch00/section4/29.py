


#把指数函数表为e的幂函数
#y = 3**x -1
#y = e**(ln(3**x)) - 1
#y = e**(x*ln(3)) - 1

def f(x):
    return exp(x*log(3)) - 1



x = linspace(0, 10, 100)
y = f(x)

xlabel('x')
ylabel('y')
plot(x, y, 'r-')
