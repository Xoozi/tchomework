#区间上的绝对极值
#f(x)   = 2/3 * x - 5,    -2 <= x <= 3
#f'(x)  = 2/3
#所以极值在区间端点取到
#M = f(3) = -3
#m = f(-2)= -6.33
def f(x):
    return (2.0/3.0) * x - 5

x = linspace(-2, 3, 100)
y = f(x)

xlabel('x')
ylabel('y')
plot(x, y, 'r-')

