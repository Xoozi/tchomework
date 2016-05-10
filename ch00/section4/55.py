#证实乘法法则 设f(x) = ln(ax) g(x) = ln(x) w(x) = f(x) - g(x)
#(a)对a = 2, 3, 4, 5画f(x)和g(x)的图形， f(x)和g(x)有怎样的关系, y轴向平移关系
#(b)通过画w(x)的图形来证明
#(c)代数地证明
#   logb(a*x) = logb(a) + logb(x)
#b**(a*x) =b**a * b**x
#logb(b**(a*x)) = a*x
#logb(b**(a) * b**(x)) = 
#例题的证明简直搞笑， 用乘法法则证明乘法法则

def f(a, x):
    return log(a*x)

def g(x):
    return log(x)

def w(a, x):
    return f(a, x) - g(x)



x = linspace(0, 10, 100)
y1 = f(2, x)
y2 = f(3, x)
y3 = f(4, x)
y4 = f(5, x)
y5 = g(x)
y6 = w(5, x)


xlabel('x')
ylabel('y')
plot(x, y1, 'r-', x, y2, 'g-', x, y3, 'b-', x, y4, 'r--', x, y5, 'g--', x, y6, 'b--')
