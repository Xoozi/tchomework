


# IPython log file
# 求f(x) = (2*x + 1)/(x + 3)的反函数g(x)， 并验证(f ⊙  g)(x) = (g ⊙ f)(x) = x
# 用解x的办法求反函数   y = (2*x + 1) / (x +3)
#                       x*y + 3*y = 2*x + 1
#                       x(y - 2) = 1 - 3*y
#                       x = (1-3*y)/(y-2)

def f(x):
    return (2*x+1.0)/(x+3.0)


def g(x):
    return (1.0-3*x)/(x-2.0)

x = linspace(0, 5, 100)
y = f(x)
x1 = linspace(f(5), f(0), 100)
y1 = g(x1)

xlabel('x')
ylabel('y')
plot(x, y, 'r-', x1, y1)
