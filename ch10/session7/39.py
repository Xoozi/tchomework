
'''

y = f(x) = sin x,  0 <= x <= 2pi

f'(x) = cos x
f''(x) = -sin x

κ(x) = |f''(x)| / (1 + f'(x)²)**(3/2)
     = sqrt(sin²x) / (1 + cos²x)**(3/2)
'''

def fun(x):
    return sin(x)

def kappa(x):
    return sqrt(sin(x)**2) / (1 + cos(x)**2)**(3.0/2.0)


x = linspace(0, 2*pi, 1000)
y = fun(x)
k = kappa(x)

plot(x, y, '-r', x, k, '-g')
