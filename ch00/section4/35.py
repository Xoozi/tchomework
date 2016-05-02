
#求解方程， 做图
#exp(x) + exp(-x) = 3
#设exp(x) = a
#原方程转变为   a + 1/a = 3
#=>                 a**2 + 1 = 3*a
#=>                 a**2 - 3*a + 1 = 0
#解二次方程用求根公式
#delta = 9 - 4 × 1 × 1 = 5
#=>                 a = (3 ± sqrt(5))/2
#=> x = ln(3 ± sqrt(5))/2)

def f(x):
    return exp(x) + exp(-x)



x = linspace(0, 5, 100)
y = f(x)


xlabel('x')
ylabel('y')
plot(x, y, 'r-')
