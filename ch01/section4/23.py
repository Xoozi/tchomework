
#lim(x->1)sec(x * sec(x)**2 - tan(x)**2 - 1)
#连续的

def sec(x):
    return 1/cos(x)

def f(x):
    return sec(x * sec(x)**2 - tan(x)**2 - 1)

x = linspace(-2*pi, 2*pi, 1000)
y = f(x)


xlabel('x')
ylabel('y')
plot(x, y, 'r-')
