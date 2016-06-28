#求平均变化率
def f(x):
    return e**x
#(a) [-2, 0]
#(b) [1, 3]

x1 = linspace(-2, 0, 100)
y1 = f(x1)
x2 = linspace(1, 3, 100)
y2 = f(x2)

tx1 = -1
ty1 = f(tx1)

tx2 = 2
ty2 = f(tx2)

xlabel('x')
ylabel('y')
plot(x1, y1, 'r-', [tx1], [ty1], '*r')
text(tx1, ty1, 'acr:%f' % ((f(0) - f(-2))/2))

plot(x2, y2, 'r-', [tx2], [ty2], '*r')
text(tx2, ty2, 'acr:%f' % ((f(3) - f(1))/2))
