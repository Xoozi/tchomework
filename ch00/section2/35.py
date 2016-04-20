# IPython log file
# y = (x+1)/2 + 5

def f(x):
    return (x+1) / 2.0 + 5
def g(x):
    return ((x-1)+1) / 2.0 + 5 - 5

x = linspace(-10, 10, 100)
y1 = f(x)
y2 = g(x)
xlabel('x')
ylabel('y')
plot(x, y1, 'r-', x, y2, 'g--')

