

# IPython log file
# 求f(x) = -(x - 2)**2, x <= 2的反函数g(x)， 并验证(f ⊙  g)(x) = (g ⊙ f)(x) = x
# xoozi 这题有毒
# 有一个隐藏的陷阱
# 用解x的办法求反函数 y = -(x-2)**2
#                       -y = (x - 2)**2
#                       这里就是关键之处
#                       直接开方sqrt(-y) = x - 2就错了
#                       -y = (x - 2)**2 开方后函数变成了
#                       sqrt(-y) = abs(x - 2)
#                       所以开方时先判断x-2的值， 这x-2 <= 0
#                       于是sqrt(-y) = - (x - 2)
#                           sqrt(-y) = -x + 2
#                           x = 2 - sqrt(-y)

def f(x):
    return -(x - 2)**2


def g(x):
    return 2 - sqrt(-x)

x = linspace(-2, 2, 100)
y = f(x)
x1 = linspace(-16, 0, 100)
y1 = g(x1)

xlabel('x')
ylabel('y')
plot(x, y, 'r-', x1, y1, 'g-')
