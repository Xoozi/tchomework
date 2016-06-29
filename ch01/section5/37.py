
#图形研究:垂直切线
#(a)画题中的曲线的图形, 该图形在什么地方看出来有垂直切线?
#(b)计算极限来确认在(a)中的结论
#从图上看, 该图形是没有垂直切线的, 在x=0处貌似有但
#lim(h->0)(f(0 + h) - f(0)) / h
#=lim(h->0)(h**(1/5)  - 0) / h
#=lim(h->0)(1 / h**4/5)
#=lim(h->0+)(1 / h**4/5) = ∞
#=lim(h->0-)(1 / h**4/5) = ∞
#在x = 0处左右极限相等, 故曲线有垂直切线
#f(x) = x**(1/5)
def f(x):
    return (x)**0.2

s1 = -3
e1 = -0.2
s2 = 0.2
e2 = 3

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
