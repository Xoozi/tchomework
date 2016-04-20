# IPython log file

def f(x):
    return 2*abs(x+4) - 3

x = linspace(-10, 10, 100)
y = f(x)
xlabel('x')
ylabel('y')
plot(x, y, 'r-')
