

# IPython log file
# 求f(x) = 1/(x**2)的反函数g(x)， 并验证(f ⊙  g)(x) = (g ⊙ f)(x) = x
# 用解x的办法求反函数   y = 1/(x**2)
#                       x**2 = 1/y
#                       x = 1/sqrt(y)
# xoozi 我取的这个区间画出来挺漂亮
# 稍稍有违直觉， 函数和它的反函数都是单调递减， 这里反的只是靠近x和y的变化率

def f(x):
    return 1/(x**2)


def g(x):
    return 1/sqrt(x)

x = linspace(0.5, 3, 100)
y = f(x)
x1 = linspace(1.0/9.0, 4, 100)
y1 = g(x1)

xlabel('x')
ylabel('y')
plot(x, y, 'r-', x1, y1, 'g-')
