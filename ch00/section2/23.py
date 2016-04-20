# IPython log file

def f(x):
    if x < 1:
        return 4 - x**2
    elif x > 3:
        return x + 3
    else:
        return 3.0*x/2.0 + 3.0/2.0

ff = frompyfunc(f, 1, 1)
x = linspace(-10, 10, 100)
y = ff(x)
xlabel('x')
ylabel('y')
plot(x, y, 'r-')
