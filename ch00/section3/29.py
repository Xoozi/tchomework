# IPython log file

def f(x):
    return 500000 * (1.0375**x)

ff = frompyfunc(f, 1, 1)
x = linspace(0, 100, 100)
y = ff(x)
xlabel('x')
ylabel('y')
plot(x, y, 'r-')
