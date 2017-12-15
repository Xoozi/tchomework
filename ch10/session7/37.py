'''

y = f(x) = x²,  -2 <= x <= 2

f'(x) = 2x
f''(x) = 2

κ(x) = |f''(x)| / (1 + f'(x)²)**(3/2)
     = 2/(1 + 4x²)**(3/2)
'''

def fun(x):
    return x**2

def kappa(x):
    return 2.0/(1 + 4*x**2)**(3.0/2.0)


x = linspace(-2, 2, 1000)
y = fun(x)
k = kappa(x)

plot(x, y, '-r', x, k, '-g')
