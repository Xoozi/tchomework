

'''

y = f(x) = e**x,  -1 <= x <= 2

f'(x) = e**x
f''(x) = e**x

κ(x) = |f''(x)| / (1 + f'(x)²)**(3/2)
     = e**x / (1 + e**(2x))**(3/2)
'''

def fun(x):
    return e**x

def kappa(x):
    return e**x / (1 + e**(2*x))**(3.0/2.0)


x = linspace(-1, 2, 1000)
y = fun(x)
k = kappa(x)

plot(x, y, '-r', x, k, '-g')
