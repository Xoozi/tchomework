# IPython log file
# y = pow(x, 2/3)

def f(x):
    return pow(x, 2.0/3.0)
def g(x):
    return pow(x-1, 2.0/3.0) - 1

x = linspace(-10, 10, 100)
y1 = f(x)
y2 = g(x)
xlabel('x')
ylabel('y')
plot(x, y1, 'r-', x, y2, 'g--')

