#(a)可以证明不等式
#1-x**2/6  < (x*sin(x))/(2-2*cos(x))  < 1
#对于所有接近0的x都成立
#对lim(x->0)(x*sin(x)/(2-2*cos(x))), 有什么可说的
#由夹逼定理可以推断lim(x->0)(x*sin(x)/(2-2*cos(x))) = 1

#(a)对-2<=x<=2, 把y=1-x**2/6, y=(x*sin(x))/(2-2*cos(x))), 和y=1的图形画在一起

def f(x):
    return 1 - x**2/6.0

def g(x):
    return (x*sin(x))/(2-2*cos(x))

def h(x):
    return 1

x = linspace(-2, 2, 100)
y1 = f(x)
y2 = g(x)
y3 = h(x)


xlabel('x')
ylabel('y')
plot(x, y1, 'r-')
plot(x, y2, 'g-')
plot(x, y3, 'b-')
