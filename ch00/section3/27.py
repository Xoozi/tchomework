# IPython log file

def f(x):
    index = x - 1991
    return 5422 * (1.018**index)

ff = frompyfunc(f, 1, 1)
x = linspace(1991.0001, 2016, 100)
y = ff(x)
xlabel('x')
ylabel('y')
plot(x, y, 'r-')
