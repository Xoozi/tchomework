#求平均变化率
def f(x):
    return cos(x) / sin(x)
#(a) [pi/4, 3*pi/4]
#(b) [pi/6, pi/2]
s1 = pi/4.0
e1 = 3.0*pi/4.0
s2 = pi/6.0
e2 = pi/2.0

x1 = linspace(s1, e1, 100)
y1 = f(x1)
x2 = linspace(s2, e2, 100)
y2 = f(x2)

tx1 = (s1 + e1)/2.0
ty1 = f(tx1)

tx2 = (s2 + e2) /2.0
ty2 = f(tx2)

xlabel('x')
ylabel('y')
plot(x1, y1, 'r-', [tx1], [ty1], '*r')
text(tx1, ty1, 'acr:%f' % ((f(e1) - f(s1))/(e1-s1)))

plot(x2, y2, 'g-', [tx2], [ty2], '*g')
text(tx2, ty2, 'acr:%f' % ((f(e2) - f(s2))/(e2-s2)))
