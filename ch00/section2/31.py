# IPython log file
# x**2 + y**2 = 49
def f(x):
    return sqrt(49 - x**2)
def g(x):
    return sqrt(49 - (x+2)**2) - 3

x = linspace(-10, 10, 100)
y1 = f(x)
y2 = g(x)
xlabel('x')
ylabel('y')
plot(x, y1, 'r-', x, y2, 'g--')

#xoozi: 答案还真有意思 标准答案是 (x+2)**2 + (y+3)**2 = 49
