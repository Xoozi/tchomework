# IPython log file
import scipy

def f(x):
    return 3 - 2**x 

ff = frompyfunc(f, 1, 1)
x = linspace(-10, 10, 100)
y = ff(x)
xlabel('x')
ylabel('y')
plot(x, y, 'r-')
