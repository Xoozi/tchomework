#33. 若对[-1,1]上的x有x**4 < f(x) <= x**2 而对 x < -1 和 x > 1的x有 x**2 <= f(x) <= x**4,
#哪个点c你不加思索地就知道lim(x->c)f(x)存在? 关于这些点处的极限你能说明什么?

#此题画了图之后容易多了, 如果说不加思索, 可以看出的c是 -1, 0, 1, 极限分别为 1, 0, 1

def g(x):
    return x**4
def h(x):
    return x**2

x = linspace(-2, 2, 100)
y2 = g(x)
y3 = h(x)


xlabel('x')
ylabel('y')
plot(x, y2, 'r-', x, y3, 'g-')
