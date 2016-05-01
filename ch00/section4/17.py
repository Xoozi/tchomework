
# IPython log file
# 求f(x) = 2*x + 3的反函数g(x)， 并验证(f ⊙  g)(x) = (g ⊙ f)(x) = x


def f(x):
    return 2 * x + 3

def g(x):
    return (x - 3) / 2

x = linspace(-10, 10, 100)
y0 = f(x)
y1 = g(x)
y2 = f(g(x))
y3 = g(f(x))

xlabel('x')
ylabel('y')
plot(x, y0, 'r-', x, y1, 'g-', x, y2, 'b-', x, y3, 'b.')
