
# IPython log file
# 求f(x) = x**2, x <= 0的反函数g(x)， 并验证(f ⊙  g)(x) = (g ⊙ f)(x) = x
# xoozi 注意此题很有意思， 开始我以为g(x) = sqrt(x)
# 这样画出图来很怪， 并不是关于y = x对称的
# 原来g(x) = -sqrt(x)

def f(x):
    return x**2

def m(x):
    return sqrt(x)

def g(x):
    return -sqrt(x)

x = linspace(-10, 0, 100)
y = f(x)
x1 = linspace(0, 100, 100)
y1 = m(x1)
y2 = g(x1)

xlabel('x')
ylabel('y')
plot(x, y, 'r-', x1, y1, 'g-', x1, y2, 'b-')
