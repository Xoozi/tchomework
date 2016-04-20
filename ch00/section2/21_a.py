# IPython log file

def f(x):
    return -abs(3-x) + 2

f(1)
x = linspace(-10, 10, 100)
y = f(x)
xlabel('x')
ylabel('y')
plot(x, y, 'r-')
