
'''

y = f(x) = x**4/4,  -2 <= x <= 2

f'(x) = x³
f''(x) = 3x²

κ(x) = |f''(x)| / (1 + f'(x)²)**(3/2)
     = 3x²/(1 + x**6)**(3/2)
'''

def fun(x):
    return x**4/4

def kappa(x):
    return 3*x**2/(1 + x**6)**(3.0/2.0)


x = linspace(-2, 2, 1000)
y = fun(x)
k = kappa(x)

plot(x, y, '-r', x, k, '-g')
