
# IPython log file
# 求f(x) = x**3 - 1的反函数g(x)， 并验证(f ⊙  g)(x) = (g ⊙ f)(x) = x


def f(x):
    return x**3 - 1

def g(x):
    return (x + 1)**(1.0/3.0)

x = linspace(-3, 3, 100)
y0 = f(x)
x1 = linspace(f(-3), f(3), 100)
y1 = g(x1)
y2 = f(g(x))
y3 = g(f(x))

xlabel('x')
ylabel('y')
plot(x, y0, 'r-', x1, y1, 'g-', x, y2, 'b-', x, y3, 'b.')
